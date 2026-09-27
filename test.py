from sqlalchemy import create_engine,select, exists
from backend.src.company_ai.db.models import Base,Document,Company

from backend import extract_filing_documnets
from backend.src.company_ai.db.repositories.company_repository import search_company_for_ticker

from backend.src.company_ai.db.connection import get_session
from backend.src.company_ai.db.repositories.company_repository import load_companies
from backend.src.company_ai.services.ingestion_pipeline import ingest_documents
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# throwaway test database, just a local file
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

with get_session() as session:
    stmt = select(exists().where(Company.id.isnot(None)))  # "does at least one company exist?"
    already_seeded = session.scalar(stmt)
    if not already_seeded:
        load_companies(session=session)



        
with get_session() as session:
    name = input("Enter company name : ")
    selected_company = search_company_for_ticker(name, session=session)

    if not selected_company:
        print("No matching company found.")
    else:
        stmt = select(exists().where(Document.company_id == selected_company[0].id))
        result = session.scalar(stmt)

        if not result:
            raw_report_data = extract_filing_documnets(selected_company[0].ticker)

            if not raw_report_data:
                print(f"{selected_company[0].name} does not have US-domestic 10-K/10-Q/8-K filings available.")
            else:
                ingest_documents(session=session, raw_report_data=raw_report_data, company_id=selected_company[0].id)
        else:
            print("This company already exists in database")

# def delete_all_rows(table):
#     with get_session_lite() as session:
#         session.execute(delete(table))
#     return

# # delete_all_rows(Document)