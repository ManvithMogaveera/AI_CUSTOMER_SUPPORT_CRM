from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

import joblib

print("LOADING APP.PY FROM BACKEND FOLDER")
classifier = joblib.load(
    "ticket_classifier.pkl"
)

from database import (
    SessionLocal,
    engine,
    Base
)

import crud
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Support CRM API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/")
def home():

    return {
        "message": "Support CRM Running"
    }


# CREATE TICKET

@app.post("/api/tickets")
def create_ticket(
    ticket: schemas.TicketCreate,
    db: Session = Depends(get_db)
):

    text = ticket.subject + " " + ticket.description

    predicted_category = classifier.predict([text])[0]

    return crud.create_ticket(
        db,
        ticket.customer_name,
        ticket.customer_email,
        ticket.subject,
        ticket.description,
        predicted_category
    )

# GET ALL TICKETS


# GET SINGLE TICKET

@app.get("/api/tickets/{ticket_id}")
def get_ticket(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    ticket = crud.get_ticket(
        db,
        ticket_id
    )

    if not ticket:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket


# UPDATE STATUS

# GET ALL TICKETS

@app.get("/api/tickets")
def get_tickets(
    status: str = None,
    search: str = None,
    db: Session = Depends(get_db)
):

    return crud.get_tickets(
        db,
        status,
        search
    )


# UPDATE STATUS

@app.put("/api/tickets/{ticket_id}")
def update_ticket(
    ticket_id: str,
    ticket: schemas.TicketUpdate,
    db: Session = Depends(get_db)
):

    updated = crud.update_status(
        db,
        ticket_id,
        ticket.status
    )

    if not updated:

        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return updated
@app.post(
    "/api/tickets/{ticket_id}/notes"
)
def create_note(
    ticket_id: str,
    note: schemas.NoteCreate,
    db: Session = Depends(get_db)
):

    return crud.add_note(
        db,
        ticket_id,
        note.note_text
    )
@app.delete("/api/tickets/{ticket_id}")
@app.delete("/api/tickets/{ticket_id}")
def delete_ticket(
    ticket_id: str,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_ticket(
        db,
        ticket_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Ticket must be closed before deletion"
        )

    return {
        "message":"Ticket deleted successfully"
    }
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI(
#     title="Support CRM API"
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
@app.get("/test123")
def test123():
    return {"message": "hello"}