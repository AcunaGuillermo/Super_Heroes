# Generated by Django 4.1.1 on 2022-09-05 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poder',
            name='super_heroes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='heroes.superheroes'),
        ),
    ]
