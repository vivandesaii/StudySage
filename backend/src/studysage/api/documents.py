from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from studysage.db import get_db
from studysage.models import Document
from studysage.schemas import DocumentCreate, DocumentRead

router = APIRouter(prefix="/documents", tags=["documents"])

SessionDep = Annotated[Session, Depends(get_db)]


@router.post("", status_code=status.HTTP_201_CREATED, response_model=DocumentRead)
def accept_document(document: DocumentCreate, db: SessionDep):
    db_doc = Document(title=document.title, description=document.description)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)

    return db_doc


@router.get("", response_model=list[DocumentRead], status_code=status.HTTP_200_OK)
def list_documents(db: SessionDep):
    stmnt = select(Document)
    documents = db.scalars(statement=stmnt).all()
    return documents


@router.get("/{id}", response_model=DocumentRead, status_code=status.HTTP_200_OK)
def get_document_by_id(id: int, db: SessionDep):
    document = db.get(Document, id)
    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document with this id does not exist.",
        )
    return document
