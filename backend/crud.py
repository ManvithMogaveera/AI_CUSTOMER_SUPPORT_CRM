from sqlalchemy.orm import Session

from models import Ticket

import uuid


def create_ticket(
    db: Session,
    customer_name,
    customer_email,
    subject,
    description,
    category
):

    ticket = Ticket(

        ticket_id=f"TKT-{str(uuid.uuid4())[:8]}",

        customer_name=customer_name,

        customer_email=customer_email,

        subject=subject,

        description=description,

        category=category,

        status="Open"
    )

    db.add(ticket)

    db.commit()

    db.refresh(ticket)

    return ticket

def get_ticket(
    db: Session,
    ticket_id: str
):

    return (
        db.query(Ticket)
        .filter(Ticket.ticket_id == ticket_id)
        .first()
    )

def get_tickets(
    db,
    status=None,
    search=None
):

    query = db.query(Ticket)

    if status:

        query = query.filter(
            Ticket.status == status
        )

    if search:

        query = query.filter(
            (
                Ticket.customer_name.contains(search)
            )
            |
            (
                Ticket.customer_email.contains(search)
            )
            |
            (
                Ticket.subject.contains(search)
            )
            |
            (
                Ticket.description.contains(search)
            )
            |
            (
                Ticket.ticket_id.contains(search)
            )
        )

    return query.all()
def update_status(
    db: Session,
    ticket_id: str,
    status: str
):

    ticket = (
        db.query(Ticket)
        .filter(Ticket.ticket_id == ticket_id)
        .first()
    )

    if ticket:

        ticket.status = status

        db.commit()

        db.refresh(ticket)

    return ticket
from models import Note


def add_note(
    db,
    ticket_id,
    note_text
):

    note = Note(
        ticket_id=ticket_id,
        note_text=note_text
    )

    db.add(note)

    db.commit()

    db.refresh(note)

    return note
def delete_ticket(
    db: Session,
    ticket_id: str
):

    ticket = (
        db.query(Ticket)
        .filter(
            Ticket.ticket_id == ticket_id
        )
        .first()
    )

    if not ticket:
        return False

    if ticket.status != "Closed":
        return False

    db.delete(ticket)

    db.commit()

    return True