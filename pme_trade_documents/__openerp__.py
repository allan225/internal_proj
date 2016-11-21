# -*- coding:utf-8 -*-
{
   'name' : 'Report PME Leader',
   'version' : '1.0',
   'description' : """ Gérer les reports 
   =========================================================================================
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
           'account_view/report_account.xml',
           'report_pme_leader_report.xml'
                  ],
    'installable': True,
    'application': False,
    'auto_install': False,
       
}