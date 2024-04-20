# Generated by Django 3.2.25 on 2024-04-11 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        ('Company_Staff', '0006_recurr_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_billing_address', models.CharField(max_length=255)),
                ('customer_gst_type', models.CharField(max_length=255)),
                ('customer_gst_number', models.CharField(max_length=255)),
                ('customer_place_of_supply', models.CharField(max_length=255)),
                ('credit_note_date', models.DateField()),
                ('invoice_type', models.CharField(max_length=255)),
                ('invoice_number', models.CharField(max_length=255)),
                ('reference_number', models.IntegerField()),
                ('credit_note_number', models.CharField(max_length=255)),
                ('payment_method', models.CharField(max_length=255)),
                ('cheque_number', models.CharField(max_length=255)),
                ('upi_number', models.CharField(max_length=255)),
                ('bank_account_number', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('terms_and_condition', models.CharField(max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('sub_total', models.FloatField()),
                ('cgst', models.FloatField()),
                ('sgst', models.FloatField()),
                ('taxAmount_igst', models.FloatField()),
                ('shipping_charge', models.FloatField()),
                ('adjustment', models.FloatField()),
                ('grand_total', models.FloatField()),
                ('advance_paid', models.FloatField()),
                ('balance', models.FloatField()),
                ('status', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.customer')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.invoice')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('recurring_invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.recurringinvoice')),
            ],
        ),
        migrations.CreateModel(
            name='Credit_Note_Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Credit_Note_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('tax_rate', models.IntegerField()),
                ('discount', models.FloatField()),
                ('total', models.FloatField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('credit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.credit_note')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Credit_Note_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('action', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('credit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.credit_note')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Credit_Note_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('credit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.credit_note')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
    ]
