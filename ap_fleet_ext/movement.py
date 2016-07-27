# -*- coding: utf-8 -*-

import openerp
from openerp.osv import fields, osv
from openerp.tools.translate import _
import time

class movement(osv.osv):
    _name = 'movement'
    _order = 'vehicle'

    _columns = {
        'vehicle': fields.many2one('fleet.vehicle.model', 'vehicle'),		
        'project_name': fields.many2one('project.project', 'projet'),
        'movement_object': fields.char('object of movement', size=128, required=True),
		'license_plate': fields.many2one('fleet.vehicle', 'immatriculation vehicule'),
        'driver_id': fields.many2one('res.partner', 'Conducteur'),
        'start_date': fields.datetime('date depart', required=True),
        'return_date': fields.datetime('date retour', required=True),
		'km_start': fields.float('Km depart', digits=(2,1)),
		'return_km': fields.float('Km retour', digits=(2,1)),
		'traveled_km': fields.float('Km parcourus', digits=(2,1)),
		'leasing_duraton': fields.float('Duree location', digits=(2,1)),
		'price_list': fields.float('Tarif', digits=(2,1)),
		'leasing_amount': fields.float('montant location', digits=(2,1)),
		'maintenance_amount': fields.float('montant entretien', digits=(2,1)),
    }

    _defaults = {
        'active' : True
    }

    _sql_constraints = [
        ('uniq_license_plate', 'unique(license_plate)', "A movement already exists with this license_plate in database. license_plate must be unique!"),
        ('uniq_driver_id', 'unique(driver_id)', "A driver_id already exists with this name in database. driver_id must be unique!"),
    ]
	
    def calcul_solde(self, cr, uid, ids, rechargement, context=None):
        bonus=rechargement+0
        solde=rechargement*bonus
        valeur={'bonus_fcfa':bonus,'amount_after_reloading':solde}
        return {"value":valeur}
	
class movement_fleet(osv.osv):
    _name ='fleet.vehicle.odometer'
    _inherit ='fleet.vehicle.odometer'
	
    _columns={
        'movement_object': fields.char('object of movement', size=128, required=True),
        'project_name': fields.many2one('project.project', 'projet'),	
        'driver_id': fields.many2one('res.partner', 'Conducteur'),
        'start_date': fields.datetime('date depart', required=True),
        'return_date': fields.datetime('date retour', required=True),
        'km_start': fields.float('Km depart', digits=(2,1)),
        'return_km': fields.float('Km retour', digits=(2,1)),
        'traveled_km': fields.float('Km parcourus', digits=(2,1)),
        'leasing_duraton': fields.float('Duree location', digits=(2,1)),
        'price_list': fields.float('Tarif', digits=(2,1)),
        'leasing_amount': fields.float('montant location', digits=(2,1)),
        'maintenance_amount': fields.float('montant entretien', digits=(2,1)),		
    }
	  
