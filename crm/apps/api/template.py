# -*- coding: utf-8 -*-
"""
    crm.api.template
    ----------------

    Template endpoints
"""

from flask import Blueprint, request

from . import route


bp = Blueprint('template', __name__, url_prefix='/templates')


#
#   CRUD TEMPLATE PROCESOS
#   ----------------------
#
@route(bp, '/')
def process_templates():
    """Regresa una lista con todos los templates de procesos
    de una empresa"""
    #return products.all()
    return {'process_template': 'all'}


@route(bp, '/show/<template_id>')
def process_template_detail(template_id):
    """Regresa una instancia de template de proceso
    de una empresa"""
    # return products.get_or_404(product_id)
    return {'process_template': 'detail'}


@route(bp, '/update/<template_id>', methods=['POST'])
def process_template_update(template_id):
    """Actualiza una instancia de template de proceso
    de una empresa"""
    return {'process_template': 'update'}


@route(bp, '/create', methods=['POST'])
def process_template_create():
    """Crea una instancia de template de proceso de una empresa """
    return {'process_template': 'create'}


@route(bp, '/destroy/<template_id>')
def process_template_destroy(template_id):
    """Elimina una instancia de template de proceso
    de una empresa"""
    # return products.get_or_404(product_id)
    return {'process_template': 'destroy'}
