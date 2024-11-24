import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:nishant123@localhost:3306/airline_management_system_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
