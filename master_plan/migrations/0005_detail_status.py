# Generated by Django 4.2.2 on 2023-06-28 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_plan', '0004_masterplan_status_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='status',
            field=models.CharField(choices=[('A', 'No Completado'), ('B', 'Completado')], default='A', max_length=13, verbose_name='Estado'),
        ),
    ]
