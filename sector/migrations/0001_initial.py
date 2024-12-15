# Generated by Django 5.1.4 on 2024-12-12 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('poligono_coordenadas', models.TextField()),
            ],
        ),
    ]
