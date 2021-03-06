# -*- coding:utf-8 -*-
{
   'name' : 'PME Leader',
   'version' : '1.0',
   'description' : """ Gérer les reports 
   Cette application sera chargée de gérer les reports des modules de:
    - Vente
    - Achat
    - Entrepôt
    - Comptabilité
    """,
   'category': 'Impression de document',
   'sequence': 2,
   'author': 'Africa Performances',
   'depends' : ['base','sale','account','stock','purchase'], # liste des dépendances conditionnant l'ordre de démarrage
   'data' : [ # les fichiers de données à charger lors de l'installation du module
           'view/layouts.xml',
          'pme_report.xml',
          'purchaseorder_no_header.xml',
          'purchasequotation_no_header.xml',
           'report_invoice.xml',
           'report_invoice_no_header.xml',
           'report_purchaseorder.xml',
           'report_purchasequotation.xml',
           'report_saleorder.xml',
           'report_stockpicking.xml',
           'saleorder_no_header.xml',
           'stockpicking_no_header.xml',
            ],
    'installable': True,
    'application': False,
    'auto_install': False,
}