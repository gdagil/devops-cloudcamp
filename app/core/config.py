import socket

from uuid import UUID, uuid4

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    _hostname: str = socket.gethostname()
    
    author: str = "cloudru"
    uuid:UUID = uuid4()
    
    
    class Config:
        env_file = "./.env.dev"
        

settings = Settings()