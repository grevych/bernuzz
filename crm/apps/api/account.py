# -*- coding: utf-8 -*-
"""
    crm.api.account
    ----------------

    Account endpoints
"""

from flask import Blueprint, request

from . import route


bp = Blueprint('account', __name__, url_prefix='/account')


@route(bp, '/')
def account():
    """Returns a list of product instances."""
    return products.all()


@route(bp, '/', methods=['POST'])
def account_create():
    """Creates a new product. Returns the new product instance."""
    form = NewProductForm()
    if form.validate_on_submit():
        return products.create(**request.json)
    raise OverholtFormError(form.errors)


@route(bp, '/settings')
def show(product_id):
    """Returns a product instance."""
    return products.get_or_404(product_id)


@route(bp, '/settings', methods=['POST'])
def update(product_id):
    """Updates a product. Returns the updated product instance."""
    form = UpdateProductForm()
    if form.validate_on_submit():
        return products.update(products.get_or_404(product_id), **request.json)
    raise(OverholtFormError(form.errors))


@route(bp, '/<product_id>', methods=['DELETE'])
def delete(product_id):
    """Deletes a product. Returns a 204 response."""
    products.delete(products.get_or_404(product_id))
    return None, 204
