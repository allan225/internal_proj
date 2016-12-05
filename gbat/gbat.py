# -*- coding:utf-8 -*-
import openerp
from openerp.osv import fields, osv
from openerp.tools.translate import _


class sale_order(osv.osv):
    _inherit="sale.order"
    _columns={
    'code_projet2': fields.many2one('account.analytic.account','Code projet2'),
    }

class purchase_order(osv.osv):
	_inherit="purchase.order"

	_columns ={
				'payment_mode': fields.selection([('espece','Especes'),
              ('virement','Virement'),('cheque','Chèque')],'Mode de Paiement',required=True),
				
				'order_responsible_id': fields.many2one('hr.employee','Responsable de la reception'),
				'code_projet': fields.many2one('account.analytic.account', 'Code Projet'),
				'date_order2': fields.date('Date de commande', required=True),
				'warehoure_name': fields.many2one('stock.warehouse','Livrer à'),
				
	}

class stock_picking(osv.osv):
    _inherit="stock.picking"
    _columns={
    'code_projet2': fields.many2one('account.analytic.account','Code projet2'),
    }

class account_invoice(osv.osv):
    _inherit="account.invoice"
    _columns={
    'code_projet2': fields.many2one('account.analytic.account','Code projet2'),
    }

class purchase_order_line(osv.osv):
    _inherit="purchase.order.line"
    _columns={
            'ref_product': fields.char('Réf', size=64),
    }


class account_analytic_account(osv.osv):
    _inherit = 'account.analytic.account'


    def name_get(self, cr, uid, ids, context=None):
        res = []
        if not ids:
            return res
        if isinstance(ids, (int, long)):
            ids = [ids]
        for id in ids:
            elmt = self.browse(cr, uid, id, context=context)
            if context.get('models')=="achat":
            	res.append((id, self._get_one_full_name(elmt, 'ctx')))
            else:
            	res.append((id, self._get_one_full_name(elmt)))
        return res


    def _get_one_full_name(self, elmt, analytic=None, level=6):
        if level<=0:
            return '...'
        if elmt.parent_id and not elmt.type == 'template' and not analytic=='ctx':
            parent_path = self._get_one_full_name(elmt.parent_id, level-1) + " / "
        else:
            parent_path = ''

        return parent_path + elmt.name