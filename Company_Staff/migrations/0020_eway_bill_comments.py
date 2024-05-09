# Generated by Django 4.2.7 on 2024-05-09 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        ('Company_Staff', '0019_ewaybillhistory_eway_bill_reference_eway_bill_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eway_Bill_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('eway_bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.ewaybill')),
            ],
        ),
    ]
