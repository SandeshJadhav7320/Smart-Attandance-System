from datetime import datetime
from app.models import Timetable

class SessionManager:

    def get_current_session(self):
        # Current time (like 10:15)
        now = datetime.now().strftime("%H:%M")

        # Get all timetable entries
        timetable_entries = Timetable.query.all()

        for entry in timetable_entries:
            if entry.start_time <= now <= entry.end_time:
                return entry

        return None