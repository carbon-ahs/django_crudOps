# Generated by Django 3.2 on 2021-08-12 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=100)),
                ('invoice_date', models.DateField()),
                ('castomer_name', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesInvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.product')),
                ('sales_invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.salesinvoice')),
            ],
        ),
    ]
