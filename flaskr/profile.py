from flask import Blueprint, render_template, g, request, redirect, url_for, flash
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('profile', __name__, url_prefix='/profile')


@bp.route('/')
@login_required
def user_profile():
    # Retrieve the user's information from the database
    user = g.user

    # Render the profile template with the user's information
    return render_template('profile/profile.html', user=user)

@bp.route('/edit_profile', methods=('GET', 'POST'))
@login_required
def edit_profile():
    db = get_db()
    user = g.user

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        bio = request.form['bio']

        # Update the user's profile information in the database
        db.execute(
            'UPDATE user SET username = ?, email = ?, bio = ? WHERE id = ?',
            (username, email, bio, user['id'])
        )
        db.commit()
        return redirect(url_for('profile.user_profile'))

    return render_template('profile/edit_profile.html', user=user)
