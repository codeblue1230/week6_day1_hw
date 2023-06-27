from flask import Blueprint, render_template


auth = Blueprint('authentication', __name__, template_folder='auth')


@auth.route('/auth')
def home():
    return 'You made it to my other blueprint page. Congratulations'