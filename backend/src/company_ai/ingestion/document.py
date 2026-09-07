from langchain_core.documents import Document

def create_document(report):
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