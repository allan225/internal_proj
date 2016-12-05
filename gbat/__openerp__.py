# -*- coding:utf-8 -*-
{
   'name' : 'GBAT Report',
   'version' : '1.0',
   'description' : """ Gérer les reports 
   Cette application sera chargée de gérer les reports des modules de:
    - Vente
    - Achat
    - Comptabilité
    """,
   'category': 'Impression de document',
   'sequence': 2,
   'author': 'Africa Performances',
   'depends' : ['base','sale','account','stock','purchase'], # liste des dépendances conditionnant l'ordre de démarrage
   'data' : [ # les fichiers de données à charger lors de l'installation du module
           'view/layouts.xml',
          'gbat_report.xml',
          'gbat_view.xml',
           'report/report_invoice.xml',
           'report/report_invoice_no_header.xml',
           'report/report_purchaseorder.xml',
           'report/report_purchasequotation.xml',
           'report/report_saleorder.xml',
           'report/saleorder_no_header.xml',
           'report/report_stockpicking.xml',
           'report/purchaseorder_no_header.xml',
           'report/purchasequotation_no_header.xml',
           'report/stockpicking_no_header.xml',
           
                  ],
    'installable': True,
    'application': False,
    'auto_install': False,
}