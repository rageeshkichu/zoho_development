# Generated by Django 4.2.7 on 2024-04-30 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        ('Company_Staff', '0017_auto_20240418_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='EwayBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_sub_type', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('gst_type', models.CharField(blank=True, max_length=100, null=True)),
                ('gstin', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('eway_billing_address', models.CharField(blank=True, max_length=100, null=True)),
                ('eway_bill_number', models.CharField(blank=True, max_length=100, null=True)),
                ('reference_no', models.BigIntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('transaction_type', models.CharField(blank=True, max_length=100, null=True)),
                ('transportation', models.CharField(blank=True, max_length=100, null=True)),
                ('kilometers', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('document', models.FileField(null=True, upload_to='images/')),
                ('subtotal', models.IntegerField(default=0, null=True)),
                ('igst', models.FloatField(blank=True, default=0.0, null=True)),
                ('cgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('sgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('tax_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('adjustment', models.FloatField(blank=True, default=0.0, null=True)),
                ('shipping_charge', models.FloatField(blank=True, default=0.0, null=True)),
                ('grandtotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('status', models.CharField(choices=[('Saved', 'Saved')], max_length=10)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.customer')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
    ]
