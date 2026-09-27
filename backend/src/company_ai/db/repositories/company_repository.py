from ..models import Company
from typing import List
from ...ingestion.search import get_companies

def search_company_for_ticker(partial_name,session)->List[Company]:
    # To search the company from our database to fetch their reports 
    return session.query(Company).filter(
        Company.name.ilike(f"{partial_name}%")).all()  # Returns a list of Company Objects


def load_companies(session, raw_company_data=get_companies()):

    # Gets Dict of all companies data and stores in companies table in db
    company_all = []
    for company in raw_company_data["data"]:
        company_object = Company(
            name=company[1],
            ticker=company[2],
            cik=company[0]
        )
        company_all.append(company_object)

    session.add_all(company_all)