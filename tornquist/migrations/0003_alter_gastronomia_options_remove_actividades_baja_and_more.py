# Generated by Django 4.1.2 on 2022-12-05 00:23

from django.db import migrations, models
import tornquist.validaciones


class Migration(migrations.Migration):

    dependencies = [
        ('tornquist', '0002_alter_consulta_options_remove_consulta_respondido_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gastronomia',
            options={'verbose_name_plural': 'Gastronomia'},
        ),
        migrations.RemoveField(
            model_name='actividades',
            name='baja',
        ),
        migrations.RemoveField(
            model_name='actividades',
            name='url_img',
        ),
        migrations.RemoveField(
            model_name='gastronomia',
            name='baja',
        ),
        migrations.RemoveField(
            model_name='gastronomia',
            name='url_img',
        ),
        migrations.RemoveField(
            model_name='puntosinteres',
            name='baja',
        ),
        migrations.RemoveField(
            model_name='puntosinteres',
            name='url_img',
        ),
        migrations.RemoveField(
            model_name='zonasalojamientos',
            name='baja',
        ),
        migrations.RemoveField(
            model_name='zonasalojamientos',
            name='url_img',
        ),
        migrations.AddField(
            model_name='actividades',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AddField(
            model_name='gastronomia',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AddField(
            model_name='gastronomia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='gastronomia/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='puntosinteres',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AddField(
            model_name='zonasalojamientos',
            name='estado',
            field=models.CharField(choices=[('Aceptada', 'Aceptada'), ('Baja', 'Baja')], default='Aceptada', max_length=15),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='mensaje',
            field=models.TextField(max_length=300, validators=[tornquist.validaciones.clean_mensaje]),
        ),
    ]