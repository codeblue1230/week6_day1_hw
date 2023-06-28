from flask import Blueprint, render_template, request, redirect, url_for, flash
from my_inventory.forms import UserLoginForm
from my_inventory.models import User, db


auth = Blueprint('authentication', __name__, template_folder='auth')


@auth.route('/auth', methods = ['GET', 'POST'])
def home():
    userform = UserLoginForm()

    try:
        if request.method == 'POST' and userform.validate_on_submit():
            email = userform.email.data
            username = userform.username.data
            password = userform.password.data
            print(email, password)

            user = User(email, username, password)

            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'user-created')

            return redirect(url_for('site.home'))

        
    except:
        raise Exception('Invalid Form Data. Please Check your form')
    
    return render_template('signup.html', form=userform)