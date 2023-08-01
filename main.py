from flask import Flask  # request
from flask_restful import Resource, Api, reqparse, abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
class StudentsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dept = db.Column(db.String(100), nullable=False)
    session = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"student(name={name},dept={dept},session={session})"

api = Api(app)

student_info = reqparse.RequestParser()
student_info.add_argument("name", type=str, help="name value", required=True)
student_info.add_argument("dept", type=str, help="dept value", required=True)
student_info.add_argument("session", type=str, help="session value", required=True)

resource_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'dept':fields.String,
    'session':fields.String

}
class Students(Resource):
    @marshal_with(resource_fields)
    def put(self, student_no):
        student = student_info.parse_args()
        result = StudentsModel.query.filter_by(id=student_no).first()
        if result:
            abort(400,messege="id already exist")
        student_db =StudentsModel(id=student_no,name=student['name'],dept=student['dept'],session=student['session'])
        db.session.add(student_db)
        db.session.commit()
        return student_db, 201

    @marshal_with(resource_fields)
    def get(self, student_no):
        result=StudentsModel.query.filter_by(id=student_no).first()
        if not result:
            abort(404,messege="id dont exist")
        return result,200
    @marshal_with(resource_fields)
    def patch(self,student_no) :
        student = student_info.parse_args()
        result = StudentsModel.query.filter_by(id=student_no).first()
        if not result:
            abort(404, messege="not valid id")
        if 'name' in student:
            result.name=student['name']
        if 'dept' in student:
            result.dept=student['dept']
        if 'session' in student:
            result.session=student['session']
        db.session.add(result)
        db.session.commit()
        return result

    def delete(self, student_no):
        student = StudentsModel.query.filter_by(id=student_no).first()
        if not student:
            abort(404, message="Student not found")
        db.session.delete(student)
        db.session.commit()

        return "Student deleted successfully", 200


api.add_resource(Students, "/add_student/<int:student_no>")


if __name__ == "__main__":
    app.run(debug=True)
