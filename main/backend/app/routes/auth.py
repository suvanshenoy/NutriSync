from flask import (Blueprint,jsonify,
                   request,render_template,
                   redirect,url_for)
from app import db
from app.models.user import User
from app.models.sign_in import SignIn
from app.models.meal import Meal
from app.models.calorie import Calorie
from colorama import Fore,Style
from datetime import datetime,timedelta
import json
import requests





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
        response['redirect'] = f'http://localhost:3000/NutriSync/dashboard/{signed_in_user.name}'
        db.session.add(signed_in_user)
        print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}\t\n",end="")
        print(f"{Fore.RED}{json.dumps(response,indent=4)}\n{Style.RESET_ALL}")
        db.session.commit()
        return jsonify(response)
    else:
        response={}
        response['message'] = 'User not found'
        print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}\t\n",end="")
        print(f"{Fore.RED}{json.dumps(response,indent=4)}\n{Style.RESET_ALL}")
        return jsonify(response), 401

@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    data = request.get_json()
    user_name = data.get('user_name', '')

    # Remove the user from the SignIn table
    signed_in_user = SignIn.query.filter_by(name=user_name).first()
    if signed_in_user:
        db.session.delete(signed_in_user)
        db.session.commit()

        response={}
        response['message'] = 'Logout successful'
        response['redirect'] = 'http://localhost:5000/NutriSync/landing-page'
        print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}\t\n",end="")
        print(f"{Fore.RED}{json.dumps(response,indent=4)}\n{Style.RESET_ALL}")
        return jsonify(response)
    else:
        response = {'message': 'User not found in the SignIn table'}
        return jsonify(response), 404

meals_data = [
  "Chicken Salad"
  "Vegetarian Pizza",
  "Biryani",
  "Paneer Butter Masala",
  "Dosa",
  "Samosa",
  "Tandoori Chicken",
  "Chole Bhature",
  "Palak Paneer",
  "Butter Chicken",
  "Rajma Chawal",
  "Masala Dosa",
  "Aloo Paratha",
  "Fish Curry",
  "Mutton Curry",
  "Gulab Jamun",
  "Jalebi",
  "Rasgulla",
  "Pav Bhaji",
  "Dal Makhani"
]
@auth_bp.route('/NutriSync/dashboard/<name>')
def dashboard(name):
    user = SignIn.query.filter_by(name=name).first()
    if user:
        user_count = User.query.count()
        last_week = datetime.utcnow() - timedelta(days=7)
        new_signups_count = User.query.filter(User.signup_date >= last_week).count()
        return render_template('dashboard.html',
                           meals_data = meals_data,
                           user_count=user_count,
                           user_name = user.name,
                           new_signups_count=new_signups_count)
    else:
        return render_template('dashboard.html',user_name="guest".capitalize())

@auth_bp.route('/api/add_meal', methods=['POST'])
def add_meal():
        data = request.get_json()
        user_name = data.get('user_name')
        selected_meal = data.get('selected_meal')

        meal = Meal.query.filter_by(name=selected_meal).first()
        if meal:
           calories = meal.calories
           print(f"\n{Fore.GREEN}[status]{Style.RESET_ALL}\n",end="")
           print(f"\n{Fore.RED} User {user_name} selected  {selected_meal}{Fore.WHITE}\n")
           print(f"{Fore.RED} User {user_name} selected {selected_meal} with {calories} calories{Fore.WHITE}\n")
           return jsonify({'calories': calories}), 200
        else:
          return ""





auth_bp.route('/NutriSync/contact')
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


