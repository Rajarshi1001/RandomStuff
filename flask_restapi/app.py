from flask import Flask
from flask_restful import Resource, Api, abort, marshal_with, reqparse, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///sqlite.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Peep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    hall_no = db.Column(db.Integer)
    dept = db.Column(db.String(10))
    clubs = db.Column(db.String(100))

    def __repr__(self):
        return (self.id, self.name, self.hall_no, self.dept, self.club)
db.create_all()

post_args = reqparse.RequestParser()
post_args.add_argument("name", type=str, required=True, help="Name is required")
post_args.add_argument("hall_no", type=int, required=True, help="Hall is required")
post_args.add_argument("dept", type=str, required=True, help="department is required")
post_args.add_argument("clubs", type=str, required=True, help="Clubs are required")

update_args = reqparse.RequestParser()
update_args.add_argument("name", type=str)
update_args.add_argument("hall_no", type=int)
update_args.add_argument("dept", type=str)
update_args.add_argument("clubs", type=str)

resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'hall_no' : fields.Integer,
    'dept' : fields.String,
    'clubs' : fields.String
}

class all_members(Resource):
    def get(self):
        members = Peep.query.all()
        students = {}
        for member in members:
            students[member.id] = {"name": member.name, "dept": member.dept, "hall_no": member.hall_no, "clubs": member.clubs} 
        return students

class hall_member(Resource):

    @marshal_with(resource_fields)
    def get(self, student_id):
        student = Peep.query.filter_by(id=student_id).first()
        if not student:
            abort(404, "Student ID not found")
        return student
    
    @marshal_with(resource_fields)
    def post(self, student_id):
        args = post_args.parse_args()
        student = Peep.query.filter_by(id=student_id).first()
        if student:
            abort(409, message = "Student ID is taken....")
        student = Peep(id = student_id, name = args['name'], hall_no = args['hall_no'], dept = args['dept'] , clubs = args['clubs'])
        db.session.add(student)
        db.session.commit()
        return student,201    
    
    @marshal_with(resource_fields)
    def put(self, student_id):
        args = post_args.parse_args()
        student = Peep.query.filter_by(id=student_id).first()
        if not student:
            abort(404, "Student ID not found")
        if args['name']:
            student.name = args['name']
        if args['hall_no']:
            student.hall_no = args['hall_no']
        if args['dept']:
            student.dept = args['dept']
        if args['clubs']:
            student.clubs = args['clubs']     
        db.session.commit()
        return student    

    def delete(self, student_id):
        student = Peep.query.filter_by(id=student_id).first()
        db.session.delete(student)
        db.session.commit()

api.add_resource(hall_member,'/hall_peep/<int:student_id>')
api.add_resource(all_members, '/all_peeps')

if __name__ == '__main__':
    app.run(debug=True)
