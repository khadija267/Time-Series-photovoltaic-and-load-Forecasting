# The EMSx dataset: historical photovoltaic and load Prediction deployed by FastAPI 

A FastAPI application for making predictions using a trained prophet model.

## Data Link:
https://www.kaggle.com/datasets/adri1g/the-emsx-dataset-historical-photovoltaic-and-load?select=1.csv

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pandas
- Pickle (if using a pickled model)


## Setup

1. Clone the repository:
git clone [your-repository-url]
cd Time-Series-photovoltaic-and-load-Forecasting

2. Create and activate virtual environment:
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

## Running the API

Start the server:
python app/main.py
The API will be available at http://localhost:8000

## Testing the API

### 1. Health Check
- Open http://localhost:8000/health in your browser
- Should receive a response confirming the service is healthy

### 2. Making Predictions
Using Swagger UI (Recommended):
1. Visit http://localhost:8000/docs
2. Click on POST /predict endpoint
3. Click "Try it out"
4. Upload your CSV file (from data/input folder)
5. Click "Execute"

### Input Data Format
Your CSV file should contain:
- 'ds' column: datetime values
- 'y' column: target values

Example data files are provided in `data/input/`:
- test.csv
- train.csv

## API Endpoints
- `/health`: Check if service is running
- `/predict`: Make time series predictions
- `/docs`: Interactive API documentation

## Directory Structure
├── app/
│   ├── main.py         # Main API code
│   └── config.py       # Configuration
├── data/
│   └── input/          # Input data files
└── requirements.txt    # Dependencies
