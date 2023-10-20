from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = True
    TESTING = True

    # Configuración base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{os.getenv("USER")}:{os.getenv("PASSWORD")}@localhost:{os.getenv("PORT")}/blog_db'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    SECRET_KEY = {os.getenv("SECRET_KEY")}
