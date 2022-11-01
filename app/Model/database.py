from app import db


 
class EmployeeModel(db.Model):
    __tablename__ = 'Employee_Table'
 
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer,unique = True)
    emp_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    position = db.Column(db.String(80))
    

db.create_all()