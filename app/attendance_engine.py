from datetime import datetime
from app import db
from app.models import AttendanceSession

class AttendanceEngine:

    def mark_presence(self, student_id, session_number):
        today = datetime.now().date()

        record = AttendanceSession.query.filter_by(
            student_id=student_id,
            date=today,
            session_number=session_number
        ).first()

        if record:
            # update last seen
            record.last_seen = datetime.now()
        else:
            # first time seen
            record = AttendanceSession(
                student_id=student_id,
                date=today,
                session_number=session_number,
                first_seen=datetime.now(),
                last_seen=datetime.now()
            )
            db.session.add(record)

        db.session.commit()
    def calculate_attendance(self):
        from app.models import AttendanceSession

        records = AttendanceSession.query.all()

        for record in records:

            if record.first_seen and record.last_seen:

                # ⏱ calculate duration (minutes)
                duration = (record.last_seen - record.first_seen).total_seconds() / 60
                record.duration_minutes = duration

                # ✅ Present / Absent
                if duration >= 60:
                    if entry_time > "09:15":
                        record.status = "Late"
                    else:
                        record.status = "Present"
                else:
                    record.status = "Absent"

        db.session.commit()