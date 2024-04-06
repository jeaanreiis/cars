from flask import render_template

from . import bp_auth


@bp_auth.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')


@bp_auth.route('/logout', methods=('GET', 'POST'))
def logout():
    return 'Rota de logout/index'


@bp_auth.route('/register', methods=('GET', 'POST'))
def register():
    return 'Rota de registro'