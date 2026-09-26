from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def check_connection():
    if engine:
        with get_session() as session:
            result = session.execute(text("SELECT 1"))
            print("Database connection successful. Result:", result.scalar())



engine_lite = create_engine("sqlite:///test.db")
SessionLite = sessionmaker(bind=engine_lite)

@contextmanager
def get_session_lite():
    session = SessionLite()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

