# Generated by Django 4.2.7 on 2024-05-11 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        ('Company_Staff', '0022_ewaybill_hsn_ewaybill_sac'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails'),
            preserve_default=False,
        ),
    ]
