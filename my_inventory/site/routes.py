from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from my_inventory.forms import LegoForm
from my_inventory.models import Lego, db


site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    legoform = LegoForm()

    try:
        if request.method == 'POST' and legoform.validate_on_submit():
            name = legoform.name.data
            description = legoform.description.data
            price = legoform.price.data
            difficulty = legoform.price.data
            piece_count = legoform.piece_count.data
            lego_category = legoform.lego_category.data
            user_token = current_user.token

            lego = Lego(name, description, price, difficulty, piece_count, lego_category, user_token)

            db.session.add(lego)
            db.session.commit()

            return redirect(url_for('site.profile'))
        
    except:
        raise Exception('Lego set could not be created. Please try again.')
    
    user_token = current_user.token
    legos = Lego.query.filter_by(user_token=user_token)

    return render_template('profile.html', form=legoform, legos=legos)
