from flask import (Blueprint,jsonify,
                   request,render_template,
                   redirect,url_for)
from app import db
from app.models.user import User
from app.models.sign_in import SignIn
from colorama import Fore,Style
from datetime import datetime,timedelta


auth_bp = Blueprint('auth',__name__)


@auth_bp.route('/api/sign-up', methods=['POST','GET'])
def sign_up():
    data = request.get_json()
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    age = data.get('age', '')
    dob = data.get('dob', '')
    gender = data.get('gender', '')
    email = data.get('email', '')
    password = data.get('password', '')

    new_user = User(
         first_name=first_name,
         last_name=last_name,
         email=email,
         password=password,
         age=age,
         dob=dob,
         gender=gender,
     )
    dict_success_data={}
    dict_success_data['message'] = 'User succesfully registered'
    db.session.add(new_user)
    print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}",end="")
    print(f"{Fore.RED}\t{dict_success_data}{Style.RESET_ALL}\n")
    db.session.commit()
    return jsonify(dict_success_data)



@auth_bp.route('/api/sign-in', methods=['POST','GET'])
def sign_in():
    data = request.get_json()
    email = data.get('email','')
    user = User.query.filter_by(email=email).first()

    
    if user:
        signed_in_user = SignIn(
            name = f"{user.first_name} {user.last_name}",
            email = user.email,
            password = user.password,
        )
        response={}
        response['message'] = 'Sign-in successful'
        db.session.add(signed_in_user)
        print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}\t",end="")
        print(f"{Fore.RED}{response}\n{Style.RESET_ALL}")
        db.session.commit()
        return jsonify(response),200
    else:
        response={}
        response['message'] = 'User not found'
        print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}\t",end="")
        print(f"{Fore.RED}{response}\n{Style.RESET_ALL}")
        return jsonify(response), 401

    

@auth_bp.route('/NutriSync/dashboard')
def dashboard():
    user_count = User.query.count()
    # active_users_count = User.query.filter_by(active=True).count()
    last_week = datetime.utcnow() - timedelta(days=7)
    new_signups_count = User.query.filter(User.signup_date >= last_week).count()

    return render_template('dashboard.html',
                           user_count=user_count,
                           # active_users=active_users_count
                           new_signups_count=new_signups_count)


@auth_bp.route('/NutriSync/contact')
def contact():
    return render_template('contact.html')

@auth_bp.route('/NutriSync/about')
def about():
    return render_template('about.html')

@auth_bp.route('/NutriSync/faq')
def faq():
    return render_template('faq.html')

@auth_bp.route('/NutriSync/plan')
def plan():
    return render_template('plan.html')
