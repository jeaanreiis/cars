from flask import redirect, url_for, render_template, request, flash
from ..models import db, Cars, Buy
from .forms import VendaForm

from . import bp_routes


@bp_routes.route('/comprar', methods=('GET', 'POST'))
def compra():
    form = None

    cat = Cars.query.all()

    return render_template('comprar.html', form=form, cat=cat)


@bp_routes.route('/vender', methods=('GET', 'POST'))
def venda():
    form = VendaForm(request.form)

    if request.method == 'POST':
        
        cars = Cars()
    
        cars.nome=form.nome.data
        cars.modelo=form.modelo.data
        cars.marca=form.marca.data
        cars.valor=form.valor.data
        cars.descricao=form.descricao.data

        db.session.add(cars)
        db.session.commit()

        return redirect(request.url)
    
    return render_template('vender.html', form=form)

@bp_routes.route('/financiamento', methods=('GET', 'POST'))
def financiamento():

    return render_template('financiamento.html')
