# -*- coding:utf-8 -*-
import openerp
from openerp.osv import fields, osv

class sale_order(osv.osv):
	_inherit="sale.order"

class purchase_order(osv.osv):
	_inherit="purchase.order"

class purchase_order(osv.osv):
	_inherit="purchase.order"


class stock_picking(osv.osv):
	_inherit="stock.picking"
	
