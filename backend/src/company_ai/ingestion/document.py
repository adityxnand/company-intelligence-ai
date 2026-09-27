from langchain_core.documents import Document as LCDocuments
from typing import List, Dict

# Created for TEST Purposes do not have any uses

def create_document(report:List[Dict])->LCDocuments:
    document = []

    for record in report:
        document.append(
            LCDocuments(
                page_content=record['text'],
                metadata={
                    "company": record["company"],
                    "form": record["form"],
                    "filing_date": record["filing_date"],
                    "item": record["item"],
                    }
            )
        )
    return document