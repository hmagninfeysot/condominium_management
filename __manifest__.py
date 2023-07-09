# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'condominium_management',
    'version': '14.0.1.0.1',
    'category': '',
    'license': 'AGPL-3',
    'summary': 'Condominium management system',
    'description': """
Condominium Management
======================

This module offers a follow-up of your condominiums:

* TODO: update this list

This module has been written by Honoré Magnin-Feysot from ExNihiloSolution <https://github.com/hmagninfeysot>.
    """,
    'author': 'Honoré Magnin-Feysot',
    'website': 'https://www.exnihilosolution.com/',
    'depends': [
        'base',
        'purchase',
        'account',
        'maintenance',
        'dms',
        'contacts',
        ],
    'data': [
        'data/payment_state_data.xml',
        'data/condominium_management_data.xml',
        'security/ir.model.access.csv',
        'views/apartment_management.xml',
        'views/meeting_attendance.xml',
        'views/meeting.xml',
        'views/payment_approval.xml',
        'views/payment_state.xml',
        ],
    'installable': True,
}
