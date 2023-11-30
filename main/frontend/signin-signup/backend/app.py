from flask import  Flask , jsonify , render_template , request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from mod import get_files
from colorama import Fore,Style
import os
import subprocess

# class DATABASE_INPUT():
#     def __init__(self,user_name,password,database_name,port):
#         self.user_name = user_name
#         self.password  = password
#         self.database_name = database_name
#         self.port = port

#     def set_user_name(self):
#         return self.user_name
#     def set_password(self):
#         return self.password
#     def set_database_name(self):
#         return self.database_name
#     def set_port(self):
#         return self.port


        

HOST = 'localhost'
DEBUG = True
PORT = int(input(f"{Fore.CYAN}enter the port number\n=> "))

# database_input = DATABASE_INPUT('root','string name','nutrisyncdb',PORT)

app = Flask(__name__, static_folder='static/js', template_folder='templates')

# print("DATABASE INFO")

# USER=database_input.set_user_name()
# PWD=database_input.set_password()
# DB_NAME=database_input.set_database_name()

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///users.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app,methods=['GET','POST'])

get_files = get_files.GetFiles()

db = SQLAlchemy(app)





'''
DATABASE CLASS FOR SIGN-UP PAGE
'''
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    dob = db.Column(db.Date)
    gender = db.Column(db.String(10))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password




'''
DATABASE CLASS FOR SIGN-IN PAGE
'''
class SignIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password

    
@app.route('/')
def index():

    js_files = get_files.get_js_files()
    css_files = get_files.get_css_files()

    return render_template('index.html', js_files=js_files,css_files=css_files)

'''
/api/test is for testing whether the server works
'''


@app.route("/api/test",methods=['POST'])
def test_data():

    try:
        data  = request.get_json()
        received_data = data.get('data','')

        print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}",end="")
        print(f"{Fore.RED}  Received data:   {received_data}{Style.RESET_ALL}{Fore.WHITE}\n")

        response_mesg = 'Hello from flask!!'
        response_data = {'message': f'Received data :  {response_mesg}'}
        return jsonify(response_data)

    except Exception as e:
         return jsonify({'error' : str(e)}),500



@app.route('/api/sign-up', methods=['POST','GET'])
def sign_up():
    try:
        data = request.get_json()
        # hashed_password = generate_password_hash(data.get('password'),method='sha256')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        age = data.get('age', '')
        dob = data.get('dob', '')
        gender = data.get('gender', '')
        email = data.get('email', '')
        password = data.get('password', '')

        new_user = User(
            name=f"{first_name} {last_name}",
            email=email,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        print(jsonify({'message' : 'Sign-up successful'}))
        return jsonify({'message': 'Sign-up successful'})

    except Exception as e:
        db.session.rollback()
        print(jsonify({'error' : str(e)}))
        return jsonify({'error': str(e)}), 500



@app.route('/api/sign-in', methods=['POST','GET'])
def sign_in():
    try:
        data = request.get_json()
        email = data.get('email','')
        password = data.get('password','')

        user = User.query.filter_by(email=email,password=password).first()

        if user:
            new_sign_in = SignIn(name=f"{user.first_name} {user.last_name}", email=user.email,password=user.password)
            db.session.add(new_sign_in)
            db.session.commit()
            return jsonify({'message': 'Sign-in successful'})
        else:
            return jsonify({'message': 'User not found'}), 401

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=PORT,host=HOST,debug=DEBUG)

