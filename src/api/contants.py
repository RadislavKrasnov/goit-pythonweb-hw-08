from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.db import get_db
from src.schemas import ContactModel, ContactResponse
from src.services.contacts import ContactService
from pydantic import EmailStr

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def read_contacts(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    service = ContactService(db)
    return await service.get_contacts(skip, limit)


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    contact = await service.get_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactModel, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    return await service.create_contact(body)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(
    contact_id: int, body: ContactModel, db: AsyncSession = Depends(get_db)
):
    service = ContactService(db)
    contact = await service.update_contact(contact_id, body)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    contact = await service.delete_contact(contact_id)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.get("/search/", response_model=List[ContactResponse])
async def search_contacts(
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    email: Optional[EmailStr] = None,
    db: AsyncSession = Depends(get_db),
):
    service = ContactService(db)
    return await service.search_contacts(first_name, last_name, email)


@router.get("/upcoming_birthdays/", response_model=List[ContactResponse])
async def upcoming_birthdays(db: AsyncSession = Depends(get_db)):
    service = ContactService(db)
    return await service.get_upcoming_birthdays()
