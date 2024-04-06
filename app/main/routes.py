import os
from flask import redirect, url_for, render_template, request, flash, current_app
from ..models import db, Cars, Buy
from .forms import VendaForm, CompraForm
from werkzeug.utils import secure_filename

from . import bp_routes


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@bp_routes.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@bp_routes.route('/comprar', methods=('GET', 'POST'))
def compra():
    form = CompraForm()

    cat = Cars.query.all()

    return render_template('comprar.html', form=form, cat=cat)


@bp_routes.route('/vender', methods=('GET', 'POST'))
def venda():
    form = VendaForm(request.form)

    if request.method == 'POST':
        
        arq = request.files['file']
    
        if not allowed_file(arq.filename):
            flash('Tipo de arquivo inválido.')
            return redirect(request.url)
        
        if arq.filename != '':
            filename = secure_filename(arq.filename)
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            arq.save(filepath)
        
            cars = Cars()
        
            cars.nome=form.nome.data
            cars.modelo=form.modelo.data
            cars.marca=form.marca.data
            cars.valor=form.valor.data
            cars.descricao=form.descricao.data
            cars.anexo=filename

            db.session.add(cars)
            db.session.commit()

            flash('Seu anúncio foi criado!')

            return redirect(request.url)
    
    return render_template('vender.html', form=form)

@bp_routes.route('/financiamento', methods=('GET', 'POST'))
def financiamento():
    print(current_app.config['ALLOWED_EXTENSIONS'])

    return render_template('financiamento.html')
