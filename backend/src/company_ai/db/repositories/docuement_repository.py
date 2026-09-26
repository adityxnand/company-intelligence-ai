from ..models import Document
from datetime import datetime
from ..connection import get_session_lite

def get_document_object(Report:list[Document],company_id:int,model=Document):
    report = Report
    doc_obj_list = []
    for report in report:
        document = model(
            form= report['form'],
            item= report['item'],
            filing_date= datetime.strptime(report['filing_date'], "%Y-%m-%d").date(),
            content=report['text'],
            company_id=company_id
        )

        doc_obj_list.append(document)

    return doc_obj_list

def add_document(documents,session):
    session.add_all(documents)








