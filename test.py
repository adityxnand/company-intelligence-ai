from sqlalchemy import create_engine, delete, select, exists
from sqlalchemy.orm import Session
from backend.src.company_ai.db.models import Base, Company, Document, User, UserSelection
from backend import get_companies

from backend import create_document,extract_filing_documnets
from backend.src.company_ai.db.repositories.docuement_repository import add_document, get_document_object
from backend.src.company_ai.db.repositories.company_repository import search_company_for_ticker

from backend.src.company_ai.db.connection import get_session_lite


# throwaway test database, just a local file
engine = create_engine("sqlite:///test.db")
Base.metadata.create_all(engine)

def delete_all_rows(table):
    with get_session_lite() as session:
        session.execute(delete(table))
    return




companies = get_companies()
with get_session_lite() as session:
    company_all = []
    for company in companies["data"]:
        company_object = Company(
            name=company[1],
            ticker=company[2],
            cik=company[0]
        )
        company_all.append(company_object)

    session.add_all(company_all)


# delete_all_rows(Document)


with get_session_lite() as session:
    name = input("Enter company name : ")
    selected_company = search_company_for_ticker(name, session=session)
    stmt = select(exists().where(Document.company_id == selected_company[0].id))
    result = session.scalar(stmt)
    print(result)
    if not result:
        document_objects = get_document_object(extract_filing_documnets(selected_company[0].ticker),company_id=selected_company[0].id)
        stmt = select(exists().where(Document.company_id == selected_company[0].id))
        result = session.scalar(stmt)
        print(result)
        add_document(document_objects,session=session)
    else:
        print("This company already exists in database")


