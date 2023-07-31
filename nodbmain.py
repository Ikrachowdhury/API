from flask import Flask #request
from flask_restful import Resource,Api,reqparse,abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# names ={ "nowkshi":{"age":25,"gender":"female"},
#          "arman":{"age":25,"gender":"male"}}
student_info = reqparse.RequestParser()
student_info.add_argument("name", type=str, help="name value", required=True)
student_info.add_argument("dept", type=str, help="dept value", required=True)
student_info.add_argument("session", type=str, help="session value", required=True)

students_dictionary = {}
def not_correct_student_id_thn_abort(student_no):
    if student_no not in students_dictionary:
        abort(400,messege="student id not valid")

def  student_exits(student_no):
    if student_no  in students_dictionary:
        abort(400,messege="student already exist")
class Students(Resource):
    def put(self, student_no):
        student_exits(student_no)
        student = student_info.parse_args()
        students_dictionary[student_no] = student
        # print(students_dictionary[student_no])
        return students_dictionary[student_no], 201

    def get(self,student_no):
        not_correct_student_id_thn_abort(student_no)
        return students_dictionary[student_no]

    def delete(self,student_no):
        not_correct_student_id_thn_abort(student_no)
        del students_dictionary[student_no]
        return "deleted succesfully",200

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

