from google.oauth2 import service_account
from googleapiclient.discovery import build




SERVICE_ACCOUNT_FILE = 'service_account.json'  # update this filename
SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('calendar', 'v3', credentials=credentials)

def create_event(summary, start_time, end_time):
    print("[DEBUG] Creating event:")
    print("Summary:", summary)
    print("Start:", start_time)
    print("End:", end_time)

    try:
        event = {
            'summary': summary,
            'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'}
        }

        created_event = service.events().insert(calendarId='keerthipriyab72@gmail.com', body=event).execute()

        print("[DEBUG] Created Event:", created_event)
        return created_event.get('htmlLink')
    except Exception as e:
        print("[ERROR] Google Calendar API error:", str(e))
        return f"Failed to create event: {str(e)}"
