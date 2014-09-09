# -*- coding: utf-8 -*-
"""
    cancan.website.views
    
"""

from flask import Blueprint, render_template, redirect, request, current_app, session, flash, url_for
from flask_security import  current_user, login_required, login_user, LoginForm
from flask_social.utils import get_provider_or_404
from flask_social.views import connect_handler
from forms import RegisterForm

#from ..forms import NewProductForm, UpdateProductForm
#from ..services import products
#from . import route

#bp = Blueprint('website', __name__, url_prefix='/products')
bp = Blueprint('website', __name__)


# @app.route('/login')
# def login():
#     #if current_user.is_authenticated():
#     #    return redirect(request.referrer or '/')
# 
#     return render_template('login.html', form=LoginForm())

# @bp.route('/profile')
# @login_required
# def profile():
#     return render_template(
#         'profile.html',
#         content='Profile Page',
#         twitter_conn=core.social.twitter.get_connection(),
#         facebook_conn=core.social.facebook.get_connection(),
#         foursquare_conn=core.social.foursquare.get_connection())


@bp.route('/', methods=['GET']) 
def index():
    return render_template(
        'index.html')
    
@bp.route('/perdidos', methods=['GET']) 
@bp.route('/reportados', methods=['GET']) 
@bp.route('/encontrados', methods=['GET']) 
@login_required
def list():
    """Returns a list of lost, find or seen instances."""
    
    #si esta logeado a huevo le mandas la barra de la izquierda
    #ajax -> mandas la pura lista 
    return render_template(
        'list.html')

#lo mismo de arriba pero con el id del ultimo que se mostro PARA PUSH

@bp.route('/buscar', methods=['GET'])
@login_required
def search():
    #solo ajax
    """Returns a list of product instances."""
    return render_template(
        'list.html')
    

@bp.route('/<username>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def profile(username=None):
    """Perros reportados, perros encontrados, rescates, foto, nombre, etc"""
    #si no es ajax llamas a la lista para que te de todo y agregas el perfil
    return render_template(
        'profile.html')


@bp.route('/reportes', methods=['GET'])
@bp.route('/busquedas', methods=['GET'])
@login_required
def domain():
    return render_template()


@bp.route('/reporte/<report_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@bp.route('/busqueda/<search_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@login_required
def detail():
    return render_template()

    
@bp.route('/reporte/<report_id>/coincidencias', methods=['GET'])
@bp.route('/busqueda/<search_id>/coincidencias', methods=['GET'])
@login_required
def match():
    #ajax o no
    #si es mi perro (reportado o buscado) solamente
    return render_template()


@bp.route('/busqueda/<search_id>/predicciones', methods=['GET'])
@login_required
def prediction():
    #ajax o no
    #si es mi perro (reportado o buscado) solamente
    return render_template()
    

@bp.route('/register', methods=['GET', 'POST'])
@bp.route('/register/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')
    

    form = RegisterForm()

    if provider_id:
        provider = get_provider_or_404(provider_id)
        connection_values = session.get('failed_login_connection', None)
    else:
        provider = None
        connection_values = None

    if form.validate_on_submit():
        ds = current_app.extensions['security'].datastore
        user = ds.create_user(email=form.email.data, password=form.password.data)
        ds.commit()

        # See if there was an attempted social login prior to registering
        # and if so use the provider connect_handler to save a connection
        connection_values = session.pop('failed_login_connection', None)

        if connection_values:
            connection_values['user_id'] = user.id
            connect_handler(connection_values, provider)

        if login_user(user):
            ds.commit()
            flash('Account created successfully', 'info')
            return redirect(url_for('website.index'))

        return render_template('thanks.html', user=user)

    login_failed = int(request.args.get('login_failed', 0))

    return render_template('register.html',
                           form=form,
                           provider=provider,
                           login_failed=login_failed,
                           connection_values=connection_values)



#     """Creates a new product. Returns the new product instance."""
#     form = NewProductForm()
#     if form.validate_on_submit():
#         return products.create(**request.json)
#     raise OverholtFormError(form.errors)
# 
# 
# @route(bp, '/<product_id>')
# def show(product_id):
#     """Returns a product instance."""
#     return products.get_or_404(product_id)
# 
# 
#     """Updates a product. Returns the updated product instance."""
#     form = UpdateProductForm()
#     if form.validate_on_submit():
#         return products.update(products.get_or_404(product_id), **request.json)
#     raise(OverholtFormError(form.errors))
# 
# 
# 
#     """Deletes a product. Returns a 204 response."""
#     products.delete(products.get_or_404(product_id))
#     return None, 204
