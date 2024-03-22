from flask import Blueprint, render_template, g
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/')
@login_required
def user_profile():
    # Retrieve the user's information from the database
    user = g.user

    # Render the profile template with the user's information
    return render_template('profile.html', user=user)


