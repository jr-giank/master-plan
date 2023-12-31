# Generated by Django 4.2.2 on 2023-06-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_plan', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterplan',
            name='status',
            field=models.CharField(choices=[('A', 'Activo'), ('B', 'Cerrado')], default='A', max_length=7, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=70, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=70, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('A', 'admin'), ('B', 'responsable')], default='A', max_length=5, verbose_name='Rol'),
        ),
    ]
