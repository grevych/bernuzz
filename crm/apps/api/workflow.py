# -*- coding: utf-8 -*-
"""
    crm.api.workflow
    ----------------

    Workflow endpoints
"""

from flask import Blueprint, request

from crm.services import process, stage, task
from . import route


bp = Blueprint('workflow', __name__, url_prefix='/processes')


#
#   CRUD PROCESOS
#   -------------
#
@route(bp, '/')
def processes():
    """Regresa una lista con todos los procesos de una empresa"""
    #return products.all()
    return {'processes': 'all'}


@route(bp, '/show/<process_id>')
def process_detail(process_id):
    """Regresa una instancia de proceso de una empresa"""
    # return products.get_or_404(product_id)
    return {'processes': 'detail'}


@route(bp, '/update/<process_id>', methods=['POST'])
def process_update(process_id):
    """Actualiza una instancia de proceso de una empresa"""
    # form = NewProductForm()
    # if form.validate_on_submit():
    #     return products.create(**request.json)
    # raise OverholtFormError(form.errors)
    return {'processes': 'update'}


@route(bp, '/create', methods=['POST'])
def process_create():
    """Crea una instancia de proceso de una empresa"""
    # form = NewProductForm()
    # if form.validate_on_submit():
    #     return products.create(**request.json)
    # raise OverholtFormError(form.errors)
    return {'processes': 'create'}


@route(bp, '/destroy/<process_id>')
def process_destroy(process_id):
    """Elimina una instancia de proceso de una empresa"""
    # return products.get_or_404(product_id)
    return {'processes': 'destroy'}


#
#   CRUD STAGE
#   ----------
#
@route(bp, '/stage/show/<stage_id>')
def stage_detail(stage_id):
    """Regresa una instancia de stage de proceso
    de una empresa"""
    # return products.get_or_404(product_id)
    return {'stage': 'detail'}


@route(bp, '/stage/update/<stage_id>', methods=['POST'])
def stage_update(stage_id):
    """Actualiza una instancia de stage de proceso
    de una empresa"""
    return {'stage': 'update'}


@route(bp, '/stage/create', methods=['POST'])
def stage_create():
    """Crea una instancia de stage de proceso de una empresa """
    return {'stage': 'create'}


@route(bp, '/stage/destroy/<stage_id>')
def stage_destroy(stage_id):
    """Elimina una instancia de stage de proceso
    de una empresa"""
    # return products.get_or_404(product_id)
    return {'stage': 'destroy'}


#
#   CRUD TASK
#   ---------
#
@route(bp, '/task/show/<task_id>')
def task_detail(task_id):
    """Regresa una instancia de stage de proceso
    de una empresa"""
    # return products.get_or_404(product_id)
    return {'task': 'detail'}


@route(bp, '/task/update/<task_id>', methods=['POST'])
def task_update(task_id):
    """Actualiza una instancia de stage de proceso
    de una empresa"""
    return {'task': 'update'}


@route(bp, '/task/create', methods=['POST'])
def task_create():
    """Crea una instancia de stage de proceso de una empresa """
    return {'task': 'create'}


@route(bp, '/task/destroy/<task_id>')
def task_destroy(task_id):
    """Elimina una instancia de stage de proceso
    de una empresa"""
    # return products.get_or_404(product_id)
    return {'task': 'destroy'}
