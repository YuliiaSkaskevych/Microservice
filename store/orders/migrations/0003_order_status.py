# Generated by Django 4.0.7 on 2022-09-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivering', 'Delivering'), ('Packed', 'Packed'), ('In_progress', 'In_progress'), ('Received', 'Received')], default='In_progress', max_length=30, verbose_name='Status'),
        ),
    ]
