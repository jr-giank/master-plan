# Generated by Django 4.2.2 on 2023-06-22 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master_plan', '0004_masterplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schude_date', models.DateField()),
                ('completed_date', models.DateField()),
                ('evaluation', models.TextField(blank=True, null=True)),
                ('observations', models.TextField()),
                ('activity', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='master_plan.activitie')),
                ('master_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master_plan.masterplan')),
                ('responsible', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='master_plan.responsible')),
                ('work_axe', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='master_plan.workaxe')),
            ],
        ),
    ]