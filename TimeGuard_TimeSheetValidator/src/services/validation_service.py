from src.utils.date_utils import is_same_day
from src.services.calendar_service import get_calendar_events

def validate_timesheet(timesheet):
    events = get_calendar_events()
    return [
        {
            **entry,
            'isValid': any(is_same_day(event['start'], entry['date']) and float(entry['hours']) == 8 for event in events),
            'discrepancy': 'No matching event' if not any(is_same_day(event['start'], entry['date']) for event in events) else ''
        }
        for entry in timesheet
    ]