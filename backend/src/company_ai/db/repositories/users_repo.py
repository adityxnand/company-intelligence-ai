from ..models import User
from sqlalchemy.orm import Session

def create_user(session:Session,email:str):
    user = User(email=email)
    session.add(user)
    session.flush()
    session.refresh(user)

