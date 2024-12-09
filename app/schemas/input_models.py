from pydantic import BaseModel
import pandas as pd
from typing import Tuple, Date, List

class InputRow(BaseModel):
    ds:Date
    
class BaseDataFrameValidator(BaseModel):
    df:List[InputRow]
    
    # def validate(self) -> Tuple[bool, str]:
    #     """Basic validation any DataFrame should pass"""
    #     if self.df is None:
    #         return False, "DataFrame cannot be None"
            
    #     if self.df.empty:
    #         return False, "DataFrame is empty"
            
    #     if len(self.df) < 2:
    #         return False, "DataFrame must have at least 2 rows"
            
    #     return True, ""

class ProphetValidator(BaseDataFrameValidator):
    """Specific validator for Prophet time series data"""
    def validate(self) -> Tuple[bool, str]:
        # First run base validation
        is_valid, message = super().validate()
        if not is_valid:
            return False, message
        
        # Check required columns
        if not all(col in self.df.columns for col in ['ds', 'y']):
            return False, "DataFrame must contain 'ds' and 'y' columns"
        
        # Check for nulls
        if self.df['ds'].isnull().any() or self.df['y'].isnull().any():
            return False, "Data contains null values"
            
        # Validate dates
        try:
            pd.to_datetime(self.df['ds'])
        except Exception:
            return False, "Column 'ds' contains invalid dates"
            
        return True, ""

def validate_input_data(df: pd.DataFrame) -> Tuple[bool, str]:
    """Main validation function to use in API endpoints"""
    validator = ProphetValidator(df)
    return validator.validate()
