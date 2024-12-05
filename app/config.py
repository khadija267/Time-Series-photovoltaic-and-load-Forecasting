### Configuration settings ###
# "Environment variables","Model parameters","API settings

from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Get the absolute path of the project root
    BASE_DIR: Path = Path(__file__).parent.parent
    
    # Define paths relative to the project root
    MODEL_PATH: str = str(BASE_DIR / "ml_models" / "model.pkl")
    DATA_INPUT_PATH: str = str(BASE_DIR / "data" / "input")
    DATA_OUTPUT_PATH: str = str(BASE_DIR / "data" / "output")
    
    # class Config:
    #     env_file = ".env"