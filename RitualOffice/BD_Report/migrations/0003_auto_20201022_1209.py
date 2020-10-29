# Generated by Django 3.1.2 on 2020-10-22 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BD_Report', '0002_remove_productorder_sum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='sum',
        ),
        migrations.AddField(
            model_name='productorder',
            name='discountID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='BD_Report.productdiscounts'),
            preserve_default=False,
        ),
    ]
