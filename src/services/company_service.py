from src.unit_of_work.unit_of_work import UnitOfWork
from src.schemas.company import AddCompany


class CompanyService:
    def __init__(self, uow_factory: UnitOfWork):
        self.uow_factory = uow_factory

