from . import bp


@bp.route('/login', methods=('GET', 'POST'))
def login():
    return 'Rota de login'


@bp.route('/logout', methods=('GET', 'POST'))
def logout():
    return 'Rota de logout/index'


@bp.route('/register', methods=('GET', 'POST'))
def register():
    return 'Rota de registro'