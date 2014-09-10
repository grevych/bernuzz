# -*- coding: utf-8 -*-
"""
    crm.api.products
    ----------------

    Process endpoints
"""

from flask import Blueprint, request

from crm.services import process, stage, task
from . import route


bp = Blueprint('workflow', __name__)


@route(bp, '/processes')
def list_processes():
    """Returns a list of process instances."""
    #return products.all()
    return {'prueba': 'all'}


@route(bp, '/process', methods=['POST'])
def create_process():
    """Creates a new process. Returns the new process instance."""
    # form = NewProductForm()
    # if form.validate_on_submit():
    #     return products.create(**request.json)
    # raise OverholtFormError(form.errors)
    pass


@route(bp, '/process/<process_id>')
def detail_process(product_id):
    """Returns a process instance."""
    # return products.get_or_404(product_id)
    pass


@route(bp, '/process/<product_id>', methods=['PUT'])
def update_process(product_id):
    """Updates a process. Returns the updated process instance."""
    # form = UpdateProductForm()
    # if form.validate_on_submit():
    #     return products.update(products.get_or_404(product_id), **request.json)
    # raise(OverholtFormError(form.errors))
    pass


@route(bp, '/process/<product_id>', methods=['DELETE'])
def delete_process(product_id):
    """Deletes a process. Returns a 204 response."""
    # products.delete(products.get_or_404(product_id))
    # return None, 204
    pass


@route(bp, '/stage', methods=['POST'])
def create_stage():
    """Creates a new stage. Returns the new stage instance."""
    pass


@route(bp, '/stage/<stage_id>')
def detail_stage(product_id):
    """Returns a stage instance."""
    pass


@route(bp, '/stage/<stage_id>', methods=['PUT'])
def update_stage(product_id):
    """Updates a stage. Returns the updated stage instance."""
    pass


@route(bp, '/stage/<stage_id>', methods=['DELETE'])
def delete_stage(product_id):
    """Deletes a stage. Returns a 204 response."""
    pass


@route(bp, '/task', methods=['POST'])
def create_task():
    """Creates a new task. Returns the new task instance."""
    pass


@route(bp, '/task/<task_id>')
def detail_task(product_id):
    """Returns a task instance."""
    pass


@route(bp, '/task/<task_id>', methods=['PUT'])
def update_task(product_id):
    """Updates a task. Returns the updated task instance."""
    pass


@route(bp, '/task/<task_id>', methods=['DELETE'])
def delete_task(product_id):
    """Deletes a task. Returns a 204 response."""
    pass
