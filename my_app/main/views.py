from datetime import datetime
from flask import render_template, session, redirect, url_for
from .. import db
from ..models import User
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['username'] = form.username.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, username=session.get('username'),
                           password=session.get('password'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
