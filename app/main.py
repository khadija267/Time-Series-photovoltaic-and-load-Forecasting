from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
import io
import uvicorn
from schemas.input_models import validate_input_data
from utils.helpers import prepare_prophet_data, format_prophet_output, load_model,save_predictions
from config import Settings
from pathlib import Path
#####################################################3

settings = Settings()
model_path = settings.MODEL_PATH
model = load_model(model_path)

app = FastAPI(
    title="Time Series Prediction API",
    description="API for making load predictions using Prophet model",
    version="1.0.0"
)

##############################33 prediction from a file
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Make predictions using uploaded time series data
    
    The input file should be a CSV with at least 'ds' and 'y' columns
    - ds: datetime column
    - y: target variable column
    """
    try:
        input_df = pd.read_csv(file.file)
        is_valid, error_message = validate_input_data(input_df)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_message)
        processed_df, future = prepare_prophet_data(input_df, model)
        forecast = model.predict(future)
        
        output_df = format_prophet_output(forecast, processed_df)
        output_path = str(Path(settings.DATA_OUTPUT_PATH) / "prophet_predictions.xlsx")

        save_predictions(output_df, output_path)
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="The uploaded file is empty")
    
    except pd.errors.ParserError:
        raise HTTPException(status_code=400, detail="Invalid CSV file format")
    
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred during prediction: {str(e)}"
        )

@app.get("/")
async def health_check():
    """Check if the service is healthy and model is loaded"""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)