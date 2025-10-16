from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  
    type = Column(String, nullable=False)     
    details = Column(Text, nullable=False)    
    carbon_kg = Column(Float, nullable=False)  
    date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)


class Recommendation(Base):
    __tablename__ = "recommendations"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)  
    address = Column(String, nullable=False)
    description = Column(Text)
    lat = Column(Float, nullable=False)       
    lng = Column(Float, nullable=False)        
    distance_km = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    eco_score = Column(Integer, nullable=False)  
    website = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)