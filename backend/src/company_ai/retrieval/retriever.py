from ...company_ai import Chunk,Document
from sqlalchemy.orm import Session



def retrieve_chunks(session:Session, embedded_text:list[float], company_id:int, top_n=4):

    return (
        session.query(Chunk)
        .join(Document, Chunk.document_id == Document.id)
        .filter(Document.company_id == company_id)
        .order_by(Chunk.embedding.cosine_distance(embedded_text))
        .limit(top_n)
        .all()
    )