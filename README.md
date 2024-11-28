# FastAPI Prediction API

A FastAPI application for making predictions using a trained model.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pandas
- Pickle (if using a pickled model)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your username/fastapi-prediction-api.git
   cd fastapi-prediction-api
2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate
    # Windows use `venv\Scripts\activate`

3. **Install the required packages:**
    ```bash
    pip install fastapi uvicorn pandas

4. **Running the Application**

**Start the server:**
    ```bash
    uvicorn model_inference:app --reload
    ```


- The application will be running at http://127.0.0.1:8000.
- You can access the API documentation at http://127.0.0.1:8000/docs.
## Usage
To make a prediction, send a POST request to /predict/ with a JSON payload containing the file path to your CSV.

### Example

**You can use curl to make a request:**

   ```bash

      curl -X POST "http://127.0.0.1:8000/predict/" -H "Content-Type: application/json" -d '{"file": "test.csv"}'
   ```

## CSV File Structure
Your CSV file should contain the following columns:

- ds: Dates in a format recognized by pandas (e.g., YYYY-MM-DD HH:MM:SS).
- y: Numeric values to be predicted.
Example of a valid CSV file:

### csv


ds,y
- 2023-01-01 10:00:00,10
- 2023-01-02 10:00:00,15
- 2023-01-03 10:00:00,20
  
## License
This project is licensed under the MIT License - see the LICENSE file for details.


### Instructions for Use

1. Replace `your-username` in the clone command URL with your actual GitHub username.
2. Save this content in a file named `README.md` in your project directory.

This README provides clear instructions on setting up and running your FastAPI application. If you have any additional information or features to add, feel free to modify it as needed!
