from flask import Blueprint, render_template, request, flash, url_for, redirect

from app.models.personaje import Personaje
from app.db import db

bp_personaje = Blueprint('bp_personaje', __name__)


@bp_personaje.route('/')
def index():
    personajes = db.personaje.find()
    return render_template('index.html', personajes=personajes)


@bp_personaje.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        lista_p = []
        cantidad_pages = int(request.form.get('cantidad_pages'))

        if cantidad_pages == 42:
            cantidad_pages = (cantidad_pages * 20) - 14
        else:
            cantidad_pages = cantidad_pages * 20

        for i in range(1, cantidad_pages + 1):
            lista_p.append(i)

        count_personajes = ",".join([str(num) for num in lista_p])

        personaje = Personaje("", "", "", "", "")
        lista_personajes = personaje.obtener_personajes(count_personajes)

        db.personaje.insert_many(lista_personajes)

        flash('Felicidades!, Se generó la BD correctamente.', 'success')
        # return redirect(url_for('bp_personaje.index'))

    return render_template('insertar.html')


@bp_personaje.route('/perfil')
def perfil():
    id = request.args.get('id')

    personaje = db.personaje.find_one({'id': int(id)})
    return render_template('perfil.html', personaje=personaje)
