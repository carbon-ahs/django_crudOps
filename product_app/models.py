from django.db import models
from django.db.models.deletion import CASCADE
'''
class newTableName(models.Model):
    clmn_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.clmn_name
'''
class Product(models.Model):
    product_code = models.CharField(max_length = 100)
    product_name = models.CharField(max_length = 100)
    selling_price = models.IntegerField()
    def __str__(self):
        return self.product_name

class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length = 100)
    invoice_date = models.DateField()
    castomer_name = models.CharField(max_length = 100)
    total_amount = models.IntegerField() 

    def __str__(self):
        return self.castomer_name + ' || ' + self.invoice_number

class SalesInvoiceDetail(models.Model):
    sales_invoice_id = models.ForeignKey(SalesInvoice, on_delete=CASCADE)
    line_number = models.IntegerField() 
    quantity =  models.IntegerField() 
    product_id = models.ForeignKey(Product, on_delete=CASCADE)
    unit_price =  models.IntegerField() 
    amount =  models.IntegerField()

    def __str__(self):
        return self.sales_invoice_id
