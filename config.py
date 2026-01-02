
from pydantic_settings import BaseSettings
 
class Settings(BaseSettings):
     
    NEO4J_AUTH:str
    NEO4J_PASSWORD:str
    NEO4J_URI:str
    


     
    class Config:
        env_file=".env"


setting=Settings()

