from app import app, db
from app import engine
from sqlalchemy.engine import create_engine
from app import db_connection
from flask import json, jsonify, request

@app.route('/insert', methods=['POST'])
def insert():
    jsonData = request.json
    print(jsonData)
    employee_id = jsonData['empid']
    name = jsonData['name']
    age = jsonData['age']
    position = jsonData['position']
    db.engine.execute("INSERT INTO Employee_Table(emp_id,emp_name,age, position) VALUES ("+str(employee_id)+",'"+name+"',"+str(age)+",'"+position+"')")
    return jsonify({'message': 'success'})

@app.route('/read', methods=['GET'])
def show():
    sql = db.engine.execute("SELECT * FROM Employee_Table")
    return jsonify([dict(row) for row in sql])

@app.route('/update', methods=['PUT'])
def update():
    jsonData = request.json
    print(jsonData)
    employee_id = jsonData['empid']
    name = jsonData['name']
    age = jsonData['age']
    position = jsonData['position']
    #native query
    db.engine.execute("UPDATE Employee_Table SET emp_id = "+str(employee_id)+", emp_name='"+name+ "', age="+str(age)+", position='"+position+"' WHERE emp_id="+str(employee_id))
    return jsonify({'message': 'successfully updated'})

@app.route('/delete/<int:employee_id>', methods=['DELETE'])
def delete(employee_id):
    db.engine.execute("DELETE FROM Employee_Table WHERE emp_id="+str(employee_id))
    return jsonify({'messsage':'deleted successfully'})

      