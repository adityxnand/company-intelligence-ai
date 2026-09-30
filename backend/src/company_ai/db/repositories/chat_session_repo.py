from ..models import ChatSession
from sqlalchemy.orm import Session

def create_chat_session(user_id: int, company_id: int, session: Session) -> ChatSession:
    chat = ChatSession(user_id=user_id, companies=[company_id])
    session.add(chat)
    session.flush()
    session.refresh(chat)
    return chat


def get_chat_session(session_id: int, session: Session) -> ChatSession | None:
    return session.get(ChatSession, session_id)


def add_company_to_chat_session(session_id: int, company_id: int, db: Session):
    chat = db.get(ChatSession, session_id)
    if company_id not in chat.companies:
        chat.companies = [*chat.companies, company_id] 
        db.flush()
        db.refresh(chat)
    return chat