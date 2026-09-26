from ..models import Company

def search_company_for_ticker(partial_name,session):
    return session.query(Company).filter(
        Company.name.ilike(f"{partial_name}%")).all()