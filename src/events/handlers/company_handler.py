from src.events.company_events import CompanyCreatedEvent
from src.tasks.email_task import dispatch_email



def handle_company_created(event: CompanyCreatedEvent):
    assert isinstance(event, CompanyCreatedEvent)
    company = event
    print("I'm here")

    dispatch_email.delay(   
        email_list=[company.email],
        subject="Welcome to xPenseiq!",
        template_name="test_template.html",
        context={"NAME": company.name, "VERIFICATION_TOKEN": company.verification_token}
    )
