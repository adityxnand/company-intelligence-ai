from langchain_core.documents import Document
from .fetcher import extract_filing_documnets

def create_document(ticker="AAPL"):
    report = extract_filing_documnets(ticker=ticker)
    document = []

    for record in report:
        document.append(
            Document(
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