{
    'name': 'Payroll - Bosnia and Herzegovina',
    'version': '1.0',
    'author': "bring.out Sarajevo, BiH",
    'category': 'Human Resources/Payroll',
    'icon': '/l10n_bs_hr_payroll/static/description/icon.png',
    'sequence': 120,
    'summary': 'Bosnian Payroll data (FBiH).',
    'depends': ['hr', 'payroll'],
    'data': [
        'data/hr_payroll_rules.xml',
        'data/hr_payroll_rules_delete.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
