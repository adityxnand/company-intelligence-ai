from ..models import Document
from datetime import datetime

def get_document_row(report_item:dict,company_id:int,model=Document)->Document:
    document = model(
            form= report_item['form'],
            item= report_item['item'],
            filing_date= datetime.strptime(report_item['filing_date'], "%Y-%m-%d").date(),
            content=report_item['text'],
            company_id=company_id
        )

    return document

def add_document(documents,session):
    session.add_all(documents)








