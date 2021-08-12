from django.contrib import admin

from .models import Product, SalesInvoiceDetail, SalesInvoice
'''
admin.site.register(NewTableName)
'''
admin.site.register(Product)
admin.site.register(SalesInvoice)
admin.site.register(SalesInvoiceDetail)
