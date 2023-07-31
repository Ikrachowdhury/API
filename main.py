from flask import Flask  # request
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy


def create_app():
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

    with app.app_context():
        db.create_all()

    return app


app = create_app()
api = Api(app)

# names ={ "nowkshi":{"age":25,"gender":"female"},
#          "arman":{"age":25,"gender":"male"}}
student_info = reqparse.RequestParser()
student_info.add_argument("name", type=str, help="name value", required=True)
student_info.add_argument("dept", type=str, help="dept value", required=True)
student_info.add_argument("session", type=str, help="session value", required=True)

class Students(Resource):
    def put(self, student_no):
        student_exits(student_no)
        student = student_info.parse_args()
        students_dictionary[student_no] = student
        # print(students_dictionary[student_no])
        return students_dictionary[student_no], 201

    def get(self, student_no):
        result=studenModel
        return students_dictionary[student_no]

    def delete(self, student_no):
        not_correct_student_id_thn_abort(student_no)
        del students_dictionary[student_no]
        return "deleted succesfully", 200


api.add_resource(Students, "/add_student/<string:student_no>")

# class First(Resource):
#     def get(self,name):
#        print(names[name])
# api.add_resource(First, "/first/<string:name>")
#
# class Second(Resource):

#     def put(self):
#         print(request.form["nowkshi"])
# api.add_resource(Second,"/second")

if __name__ == "__main__":
    app.run(debug=True)
