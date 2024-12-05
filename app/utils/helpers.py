### Utility functions ###
## "Data preprocessing","Date handling","Error handling"

import pickle
import pandas as pd
from typing import Tuple
import logging
from pathlib import Path
from config import Settings
settings = Settings()
#################################33 model loading

def load_model(model_path: str = 'model.pkl'):

    try:
        logging.info(f"Loading model ...")
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        logging.info("Model loaded successfully")
        return model

    except Exception as e:
        logging.error(f"Failed to load model: {str(e)}")
        raise
############3 prepare data for prophet model
def prepare_prophet_data(input_df: pd.DataFrame, model) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Prepare data for Prophet model prediction
    
    Args:
        input_df: Raw input DataFrame
        
    Returns:
        Tuple containing:
        - Processed input DataFrame
        - Future DataFrame for predictions
    """
    # Prepare input data
    processed_df = input_df.copy()
    processed_df['ds'] = pd.to_datetime(processed_df['ds'], errors='coerce')
    processed_df['ds'] = processed_df['ds'].dt.tz_localize(None)
    
    # Create future DataFrame
    future = model.make_future_dataframe(len(processed_df))
    
    return processed_df, future
########## format output results

def format_prophet_output(forecast_df: pd.DataFrame, input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Format Prophet forecast results
    
    Args:
        forecast_df: Prophet forecast DataFrame
        input_df: Original input DataFrame with actual values
        
    Returns:
        Formatted output DataFrame
    """
    output_df = pd.DataFrame({
        'Timestamp': forecast_df['ds'],
        # 'Input': input_df['y'],
        'Prediction': forecast_df['yhat']
    })
    
    return output_df

##### save output result into the specified path

def save_predictions(output_df: pd.DataFrame, filename: str = "predictions.xlsx") -> str:
    """
    Save prediction results to specified output path
    
    Args:
        output_df: DataFrame with predictions
        filename: Name of output file (default: predictions.xlsx)
        
    Returns:
        str: Path where file was saved
    """
    try:
        # Create output directory if it doesn't exist
        output_dir = Path(settings.DATA_OUTPUT_PATH)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Construct full output path
        output_path = output_dir / filename
        
        # Save file
        output_df.to_excel(output_path, index=False)
        logging.info(f"Predictions saved to {output_path}")
        
        return str(output_path)
        
    except Exception as e:
        logging.error(f"Failed to save predictions: {str(e)}")
        raise