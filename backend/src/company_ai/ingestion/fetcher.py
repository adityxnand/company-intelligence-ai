import edgar
from edgar import set_identity, Company

set_identity("Aditya Anand adianand@gmail.com")

company_ticker = "AAPL"
company = Company(company_ticker)

filings = company.get_filings(form=["10-K","10-Q","8-K"])

latest_10k = filings.filter(form=["10-K"]).latest(1)
latest_10q = filings.filter(form=["10-Q"]).latest(8)
latest_8k = filings.filter(form=["8-K"]).latest(6)

def extract_filing(filing):
    report = filing.obj()

    documents = []

    for item in report.items:
        documents.append({
            "company": company.name,
            "form": filing.form,
            "filing_date": str(filing.filing_date),
            "item": item,
            "text": str(report[item])
        })

    return documents

def extract_filing_documnets():
    documents = []

    # 10-K
    documents.extend(extract_filing(latest_10k))

    # 10-Q
    for filing in latest_10q:
        documents.extend(extract_filing(filing))

    # 8-K
    for filing in latest_8k:
        documents.extend(extract_filing(filing))

    return documents


