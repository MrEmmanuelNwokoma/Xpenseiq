from src.events.bus import event_bus
from src.events.notification_event import NotificationCreatedEvent
from events.company_events import CompanyCreatedEvent
# from src.events.handlers.notificaton_handler import handle_notification_created
from events.handlers.company_handler import handle_company_created



def bootstrap_event_initializer():
    # event_bus.subscribe(NotificationCreatedEvent, handle_notification_created)
    event_bus.subscribe(CompanyCreatedEvent, handle_company_created)


    