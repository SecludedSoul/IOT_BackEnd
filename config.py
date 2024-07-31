from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# การตั้งค่าการเชื่อมต่อกับ PostgreSQL
DATABASE_URL = "postgresql://default:qZYpx9XNahG6@ep-bitter-band-a1mb4con.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

