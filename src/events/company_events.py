from src.events.base import DomainEvent



class CompanyCreatedEvent(DomainEvent):
    name: str
    verification_token: str
    email: str

