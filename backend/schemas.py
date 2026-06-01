from pydantic import BaseModel
from pydantic import EmailStr

class TicketCreate(BaseModel):

    customer_name: str

    customer_email: EmailStr

    subject: str

    description: str

class TicketUpdate(BaseModel):

    status: str
class TicketResponse(BaseModel):

    ticket_id: str

    customer_name: str

    customer_email: str

    subject: str

    description: str
    category: str
    status: str
    

    class Config:
        from_attributes = True
class NoteCreate(BaseModel):

    note_text: str