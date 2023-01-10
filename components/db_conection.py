from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engie = create_engine("mysql+pymysql://root:nub78@db:3306/test")
Session = sessionmaker(bind=engie)
DATABASE = declarative_base()
