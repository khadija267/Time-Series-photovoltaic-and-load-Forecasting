
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import pickle
import numpy as np
import pandas as pd

app = FastAPI()

# test_data=pd.read_csv('test.csv')
# print(test_data.head())


with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


class InputData(BaseModel):
    file: str


@app.post("/predict/")
async def predict(input_data: InputData):
    try:
        input_df = pd.read_csv(input_data.file)
        if 'y' not in input_df.columns or 'ds' not in input_df.columns:
            raise ValueError("Input DataFrame must contain 'y' and 'ds' columns.")
        
        # input_data_array = np.array(input_df['y']).reshape(-1, 1)
        future = model.make_future_dataframe(len(input_df))
        prediction = model.predict(input_df)
        forecast = model.predict(future)

        
        
        output_df = pd.DataFrame({
            'Timestamp': forecast['ds'], 
            'Input': forecast['y'],
            'Prediction': forecast['yhat']
        })
        output_df.to_excel('prophet_load_predictions.xlsx', index=False)
        predictions_list = forecast['yhat'].tolist()
        return {"prediction": predictions_list}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))