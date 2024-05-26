from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, func
from model2 import Student, Course, Enrollment, engine

Session = sessionmaker(bind=engine)
session = Session()

###########################################################################
def add_student():
    std = Student(name="Shaguffta", age=28, gender="female")
    session.add(std)
    session.commit()
    return std
#print("Student is added in Database\n",add_student())

#....................OR.................
def addBook(name, age, gender):
    student = Student(name=name, age=age,gender= gender)
    session.add(student)
    session.commit()
    print("Students are Added")

# addBook("Afnan",16,"male")
# addBook("Alina",21,"female")
# addBook("Bebo Aunty",26,"female")



#############################################################################
def deleteStudent(Student_ID):
    student = session.query(Student).filter(Student.id ==Student_ID ).first()
    if student:
        session.delete(student)
        session.commit()
        print(f"Student with ID {Student_ID} Deleted.")
    else:
        print(f"Student with ID {Student_ID} not found.")
# deleteStudent(6)

############################################################################
def add_courses():
    c1 = Course(title="PF", credit_hour=4)
    c2 = Course(title="PAI", credit_hour=3)
    c3 = Course(title="WE", credit_hour=3)
    c4 = Course(title="DSA", credit_hour=4)
    c5 = Course(title="Databases", credit_hour=4)
    session.add_all([c1,c2,c3,c4,c5])
    session.commit()
    print("All Courses are added in data base")

# add_courses()
############################################################################

def all_students():
    students = session.query(Student).all()
    print("All Students in Data Base\n")
    for std in students:
        print(std.id,std.name,std.age,std.gender)

#all_students()
############################################################################

def all_courses():
    courses = session.query(Course).all()
    print("All Courses in Data Base\n")
    for c in courses:
        print(c.id,c.title,c.credit_hour)

# all_courses()
############################################################################


def enrol_student(studentId,courseId,semesterSession):
    cs = Enrollment(student_id=studentId,course_id=courseId,session=semesterSession)
    session.add(cs)
    session.commit()


# enrol_student(1,4,"Fall_2021")
# enrol_student(1,3,"Fall_2021")
# enrol_student(1,2,"Fall_2021")
#
# enrol_student(2,4,"Fall_2021")
# enrol_student(2,1,"Fall_2022")
# enrol_student(2,2,"Fall_2022")
#
# enrol_student(5,1,"Fall_2023")

# enrol_student(6,1,"Fall_2023")
# enrol_student(6,2,"Fall_2021")
# enrol_student(6,3,"Fall_2022")
#
# enrol_student(8,1,"Fall_2023")
# print("All Enrollements are Added in Data base")




############################################################################

def all_enrollments():
    enrollments = session.query(Enrollment).all()
    for e in enrollments:
        print(e.id,e.student_id,e.course_id)

# print("All Enrollments in Data Base")
# all_enrollments()
############################################################################

def get_enrollements(sid):
    result = session.query()

############################################################################

def student_with_courses():
    # Perform the join and select the desired columns
    query = (
        select(Student.name, Course.title)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .join(Course, Enrollment.course_id == Course.id)
    )

    # Execute the query and fetch the results
    results = session.execute(query).fetchall()

    # Print the results
    for result in results:
        print(f"Student Name: {result.name}, Course Title: {result.title}")


# student_with_courses()


############################################################################

def student_with_courses_ch(ch):
    # Perform the join and select the desired columns
    query = (
        select(Student.name, Course.title)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .join(Course, Enrollment.course_id == Course.id)
        .where(Course.credit_hour==ch)
    )

    # Execute the query and fetch the results
    results = session.execute(query).fetchall()

    # Print the results
    for result in results:
        print(f"Student Name: {result.name}, Course Title: {result.title}")


############################################################################

def students_having_courses():
    # Perform the left outer join and select the desired columns
    query = (
        select(Course.title,Student.name, Course.credit_hour)
        .outerjoin(Enrollment, Course.id == Enrollment.course_id)
         .outerjoin(Student, Enrollment.student_id == Student.id)
        # .outerjoin(Enrollment, Student.id == Enrollment.student_id)
        #  .outerjoin(Course, Enrollment.course_id == Course.id)
    )

    # Execute the query and fetch the results
    results = session.execute(query).fetchall()

    # Print the results
    for result in results:
        print(f"Student Name: {result.name}, Course Title: {result.title}, {result.credit_hour}")

# students_having_courses()


############################################################################

def students_with_courses_count():
    # Perform the join and select the desired columns with count
    query = (
        select(Student.name,func.count(Enrollment.id).label('enrolled_courses'))
        .outerjoin(Enrollment, Student.id == Enrollment.student_id)
        .group_by(Student.id)
    )

    # Execute the query and fetch the results
    results = session.execute(query).fetchall()

    # Print the results
    for result in results:
        print(f"Student Name: {result.name}, Enrolled Courses: {result.enrolled_courses}")


############################################################################

def not_enrolled_yet_in_any():
    # Perform a LEFT JOIN and select students with no enrollments
    query = (
        select(Student)
        .outerjoin(Enrollment, Student.id == Enrollment.student_id)
        .filter(Enrollment.id == None)  # Filter where there is no enrollment
    )

    # Execute the query and fetch the results
    results = session.execute(query).fetchall()

    # Print the results
    for row in results:
        print(f"Student Name: {row[0].name}")

#not_enrolled_yet_in_any()

############################################################################

# students_with_courses_count()
# add_student()
# add_courses()

# enrol_student(6,4,'Spring-23')
# enrol_student(1,3,'Fall-23')
# enrol_student(1,5,'Fall-23')
# student_with_courses_ch(4)
# not_enrolled_yet_in_any()

