# Generated by Django 4.1.2 on 2022-12-05 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tornquist', '0004_solicitud_respuestasolicitud'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actividades',
            old_name='pagina_web',
            new_name='sitio',
        ),
        migrations.RenameField(
            model_name='gastronomia',
            old_name='pagina_web',
            new_name='sitio',
        ),
        migrations.RenameField(
            model_name='puntosinteres',
            old_name='pagina_web',
            new_name='sitio',
        ),
        migrations.RenameField(
            model_name='zonasalojamientos',
            old_name='pagina_web',
            new_name='sitio',
        ),
    ]