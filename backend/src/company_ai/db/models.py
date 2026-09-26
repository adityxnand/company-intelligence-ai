from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import DateTime, ForeignKey
from datetime import datetime
from typing import Optional

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
    filing_date:Mapped[DateTime] = mapped_column(DateTime)
    item:Mapped[str]
    content:Mapped[str]

    company_id:Mapped[int] = mapped_column(ForeignKey("companies.id"))
    company: Mapped["Company"] = relationship(back_populates="documents")


# class Chunk(Base):
#     __tablename__ = "chunks"

#     id:Mapped[int] = mapped_column(primary_key=True)
#     document_id:Mapped[int] = mapped_column(ForeignKey("documents.id"))
#     chunk:Mapped[str] = mapped_column(nullable=False)
#     vector:Mapped[]

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