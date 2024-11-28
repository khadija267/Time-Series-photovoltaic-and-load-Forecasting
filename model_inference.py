
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

@app.get("/")
async def read_root():
    return {"message": "Hello World, Use POST /predict/ to make load predictions."}
@app.post("/predict/")
async def predict(input_data: InputData):
    try:
        input_df = pd.read_csv(input_data.file)
        if 'y' not in input_df.columns or 'ds' not in input_df.columns:
            raise ValueError("Input DataFrame must contain 'y' and 'ds' columns.")
        
        input_df['ds'] = pd.to_datetime(input_df['ds'], errors='coerce')
        # test_data=pd.read_csv('test.csv')
        # print(input_df.head())

        input_df[ 'ds']=input_df[ 'ds'].dt.tz_localize(None)

        # input_data_array = np.array(input_df['y']).reshape(-1, 1)
        future = model.make_future_dataframe(len(input_df))
        # print("Input DataFrame:", input_df)
        # print("Future DataFrame:", future)
        forecast = model.predict(future)
        # print("forecast:", forecast.columns)

        
        
        output_df = pd.DataFrame({
            'Timestamp': forecast['ds'], 
            'Input': input_df['y'],
            'Prediction': forecast['yhat']
        })
        # print('output_df',output_df.head())
        output_df.to_excel('prophet_load_predictions.xlsx', index=False)
        predictions_list = forecast['yhat'].tolist()
        # print('predictions_list',predictions_list)
        return {"prediction": predictions_list}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))