from ..db.repositories.docuement_repository import get_document_row
from ..ingestion.chunker  import create_chunks
from ..db.repositories.chunk_repository import get_chunk_rows


def ingest_documents(session, raw_report_data:str, company_id:int):
    for item in raw_report_data:
        doc = get_document_row(item, company_id)
        session.add(doc)
        session.flush()
        pieces = create_chunks(doc.content)
        chunk_objs = get_chunk_rows(pieces, doc.id)
        session.add_all(chunk_objs)