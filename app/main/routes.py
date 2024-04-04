from flask import redirect, url_for, render_template

from . import bp


@bp.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
