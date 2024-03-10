{
    'name': 'Library App',
    'summary': 'Library',
    'description': 'Libr',
    'author': 'Amr Aboelmagd',
    'category': 'Library',
    'version': '17.0.1.0.0',
    'depends': ['base', 'mail', 'sale'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/book.xml',
        'views/base_menus.xml',
        'views/publiisher.xml'
        # 'views/base_menu.xml',
        # 'views/book_view.xml',
        # 'views/sale_order_view.xml',
        # 'views/publisher_view.xml',
        # 'reports/book_report_view.xml'
    ]
}
