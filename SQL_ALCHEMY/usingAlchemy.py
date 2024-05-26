from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_,not_, tuple_,func
from models import User, Department, engine

Session = sessionmaker(bind=engine)
session = Session()

#add single user to Database
def addUser():
    user = User(name='Kareem', age=22)
    session.add(user)
    session.commit()

#add bulk users to Database
def addBulkUsers():
    users = []
    users.append(User(name='Ana', age=20))
    users.append(User(name='Ahmed', age=19))
    users.append(User(name='Rizwan', age=21))
    session.add_all(users)
    session.commit()

def addBulkDepartments():
    depts = []
    depts.append(Department(name='Computer'))
    depts.append(Department(name='Administration'))
    depts.append(Department(name='Accounts'))
    session.add_all(depts)
    session.commit()

#print all users from Database
def allUsers():
    users = session.query(User).order_by(User.name).all()
    for user in users:
        print(user.name)

#search user
def searchUser(_name):
    users = session.query(User).filter_by(name=_name)
    for user in users:
        print(user)


#search user
def searchUser(_name,_age):
    users = session.query(User).filter(or_(name=_name,_age=19))
    users = session.query.filter(User.name.in_['Ana','Rizwan'])
    for user in users:
        print(user)

#search user
def searchUserIn():
    users = session.query(User.age,User.name).filter(User.name.in_(['Ana','Rizwan']))
    for user in users:
        #print(user.name,user.age)
        print(user)


def groupByName():
    users = session.query(User.name,func.count(User.id)).group_by(User.name)
    for user in users:
        #print(user.name,user.age)
        print(user)

#search user
def searchUser():
    users = session.query(User).filter(tuple_(User.name,User.age).in_(['Ali','Khalid'],[12,32,12]))
    for user in users:
        print(user)


#search and get first user detail only
def searchFirstUser(_name):
    user = session.query(User).filter(User.name.like(_name)).first()
    count = session.query(User).filter(User.name.like(_name)).count()
    print(user)

#remove user from Database
def deleteuser(_id):
    user = session.query(User).filter_by(id=_id).one_or_none()
    if user is None:
        print("not found")
    else:
        print(user)
        session.delete(user)
        print('Deleted')
        session.commit()


addBulkDepartments()
# groupByName()

