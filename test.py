from sqlalchemy import create_engine,select, exists, delete
from backend.src.company_ai.db.models import Base,Document,Company

from backend import extract_filing_documnets
from backend.src.company_ai.db.repositories.company_repository import search_company_for_ticker

from backend.src.company_ai.db.connection import get_session
from backend.src.company_ai.db.repositories.company_repository import load_companies
from backend.src.company_ai.services.ingestion_pipeline import ingest_documents
from dotenv import load_dotenv
import os

from backend.src.company_ai.embeddings.embeder import get_embedding_model, embed_texts


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



def delete_all_rows(table):
    with get_session() as session:
        session.execute(delete(table))
    return

# delete_all_rows(Document)


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

        print(" ALL SET !")






essay = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam. Pellentesque ut neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. In ac felis quis tortor malesuada pretium. Pellentesque auctor neque nec urna. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Aenean viverra rhoncus pede. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut non enim eleifend felis pretium feugiat. Vivamus quis mi. Phasellus a est. Phas"





# docs = ["viral kohli is the husband of anushka sharma and he plays for Royal challengers Banglore rcb",
#         "Mahindra singh DHONI MSD, he plays for Chennai super kings CSK, and he is from Ranchi "]

# from backend.src.company_ai.ingestion.chunker import create_chunks
# chunk = create_chunks(essay)



# vector = embed_texts(chunk)
# print(len(vector))
# print(len(vector[0]))

# query = input("Enter Your Query : ")
# query_vector = embedding_model.embed_query(query)

# print(len(vector))
# print(len(vector[0]))
# print("\n"*8)
# print(len(query_vector))