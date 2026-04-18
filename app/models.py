from app import db

class Year(db.Model):
    __tablename__ = 'years'

    id = db.Column(db.Integer, primary_key=True)
    year_number = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Year {self.year_number}>"

class Section(db.Model):
    __tablename__ = 'sections'

    id = db.Column(db.Integer, primary_key=True)
    section_name = db.Column(db.String(10), nullable=False)
    year_id = db.Column(db.Integer, db.ForeignKey('years.id'))

    def __repr__(self):
        return f"<Section {self.section_name}>"
 
class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(20), nullable=False)

    year_id = db.Column(db.Integer, db.ForeignKey('years.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))

    def __repr__(self):
        return f"<Student {self.name}>"

class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(50), nullable=False)
    room_type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Room {self.room_name}>"

class Timetable(db.Model):
    __tablename__ = 'timetable'

    id = db.Column(db.Integer, primary_key=True)

    year_id = db.Column(db.Integer, db.ForeignKey('years.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))

    session_number = db.Column(db.Integer)

    start_time = db.Column(db.String(10))
    end_time = db.Column(db.String(10))

    subject_name = db.Column(db.String(100))

    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))

    def __repr__(self):
        return f"<Session {self.session_number}>"