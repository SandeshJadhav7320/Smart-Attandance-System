from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Year, Section, Student, Timetable, Room
main = Blueprint('main', __name__)

# 🏠 HOME PAGE
@main.route("/")
def home():
    return render_template("home.html")


# 📘 YEAR + SECTION PAGE
@main.route("/manage")
def manage():
    years = Year.query.all()
    sections = Section.query.all()
    return render_template("manage.html", years=years, sections=sections)


# ➕ ADD YEAR
@main.route("/add_year", methods=["POST"])
def add_year():
    year_number = request.form.get("year_number")
    db.session.add(Year(year_number=year_number))
    db.session.commit()
    return redirect(url_for("main.manage"))


# ➕ ADD SECTION
@main.route("/add_section", methods=["POST"])
def add_section():
    section_name = request.form.get("section_name")
    year_id = request.form.get("year_id")

    db.session.add(Section(section_name=section_name, year_id=year_id))
    db.session.commit()

    return redirect(url_for("main.manage"))


# 🎓 STUDENT PAGE
@main.route("/students")
def students():
    years = Year.query.all()
    sections = Section.query.all()
    students = Student.query.all()

    return render_template(
        "students.html",
        years=years,
        sections=sections,
        students=students
    )


# ➕ ADD STUDENT
@main.route("/add_student", methods=["POST"])
def add_student():
    name = request.form.get("name")
    roll_number = request.form.get("roll_number")
    year_id = request.form.get("year_id")
    section_id = request.form.get("section_id")

    db.session.add(Student(
        name=name,
        roll_number=roll_number,
        year_id=year_id,
        section_id=section_id
    ))
    db.session.commit()

    return redirect(url_for("main.students"))


# ❌ DELETE STUDENT
@main.route("/delete_student/<int:id>")
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()

    return redirect(url_for("main.students"))

# 📘 ROOMS PAGE
@main.route("/rooms")
def rooms():
    rooms = Room.query.all()
    return render_template("rooms.html", rooms=rooms)


# ➕ ADD ROOM
@main.route("/add_room", methods=["POST"])
def add_room():
    room_name = request.form.get("room_name")
    room_type = request.form.get("room_type")

    db.session.add(Room(room_name=room_name, room_type=room_type))
    db.session.commit()

    return redirect(url_for("main.rooms"))


# ❌ DELETE ROOM
@main.route("/delete_room/<int:id>")
def delete_room(id):
    room = Room.query.get(id)
    db.session.delete(room)
    db.session.commit()

    return redirect(url_for("main.rooms"))

# 📘 VIEW TIMETABLE
@main.route("/timetable")
def timetable():
    timetable = Timetable.query.all()
    years = Year.query.all()
    sections = Section.query.all()
    rooms = Room.query.all()

    return render_template(
        "timetable.html",
        timetable=timetable,
        years=years,
        sections=sections,
        rooms=rooms
    )


# ➕ ADD TIMETABLE
@main.route("/add_timetable", methods=["POST"])
def add_timetable():
    db.session.add(Timetable(
        year_id=request.form.get("year_id"),
        section_id=request.form.get("section_id"),
        session_number=request.form.get("session_number"),
        start_time=request.form.get("start_time"),
        end_time=request.form.get("end_time"),
        subject_name=request.form.get("subject_name"),
        room_id=request.form.get("room_id")
    ))

    db.session.commit()

    return redirect(url_for("main.timetable"))


# ❌ DELETE
@main.route("/delete_timetable/<int:id>")
def delete_timetable(id):
    entry = Timetable.query.get(id)
    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for("main.timetable"))