from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp_auth = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

from . import auth