from edgar import set_identity, Company

_IDENTITY = "Aditya Anand adianand@gmail.com"
_identity_set = False


def _ensure_identity():
    """Call set_identity() at most once, lazily, on first real use."""
    global _identity_set
    if not _identity_set:
        set_identity(_IDENTITY)
        _identity_set = True


def extract_filing(filing, company):
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


def extract_filing_documnets(ticker):
    """Fetch latest 10-K/10-Q/8-K filings for `ticker` and extract their items.

    All network calls happen here, inside the function, not at import time.
    """
    _ensure_identity()

    company = Company(ticker)

    filings = company.get_filings(form=["10-K", "10-Q", "8-K"])

    latest_10k = filings.filter(form=["10-K"]).latest(1)
    latest_10q = filings.filter(form=["10-Q"]).latest(8)
    latest_8k = filings.filter(form=["8-K"]).latest(6)

    documents = []

    # 10-K
    documents.extend(extract_filing(latest_10k, company))

    # 10-Q
    for filing in latest_10q:
        documents.extend(extract_filing(filing, company))

    # 8-K
    for filing in latest_8k:
        documents.extend(extract_filing(filing, company))

    return documents