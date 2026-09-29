from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, ForeignKey
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Company(Base):
    __tablename__ = "companies"

    ''' features of table '''
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=False)
    ticker:Mapped[str] = mapped_column(nullable=False, unique=True)
    cik:Mapped[str] = mapped_column(nullable=False)

    documents: Mapped[list["Document"]] = relationship(back_populates="company")



class Document(Base):
    __tablename__ = "documents"

    id:Mapped[int] = mapped_column(primary_key=True)
    form:Mapped[str] = mapped_column(nullable=False)
    filing_date:Mapped[datetime] = mapped_column(DateTime)
    item:Mapped[str] = mapped_column(nullable=False)
    content:Mapped[str] = mapped_column(nullable=False)

    company_id:Mapped[int] = mapped_column(ForeignKey("companies.id"))
    company: Mapped["Company"] = relationship(back_populates="documents")
    chunk: Mapped[list["Chunk"]] = relationship(back_populates="document")

class Chunk(Base):
    __tablename__ = "chunks"

    id:Mapped[int] = mapped_column(primary_key=True)
    document_id:Mapped[int] = mapped_column(ForeignKey("documents.id"))
    chunk:Mapped[str] = mapped_column(nullable=False)
    embedding: Mapped[list[float]] = mapped_column(Vector(384))

    document:Mapped["Document"] = relationship(back_populates="chunk")

class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(primary_key=True)
    email:Mapped[str] = mapped_column(nullable=False, unique=True)

    user_selection:Mapped[list["UserSelection"]]= relationship(back_populates="user")



class UserSelection(Base):
    __tablename__ = "user_selection"

    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    company_id:Mapped[int] = mapped_column(ForeignKey("companies.id"))

    user:Mapped["User"] = relationship(back_populates="user_selection")
    company:Mapped["Company"] = relationship()