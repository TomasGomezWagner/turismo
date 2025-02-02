# Generated by Django 3.2.14 on 2022-11-28 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tornquist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoConsulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=50, verbose_name='asunto')),
            ],
        ),
        migrations.AddField(
            model_name='actividades',
            name='baja',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='gastronomia',
            name='baja',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='puntosinteres',
            name='baja',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='zonasalojamientos',
            name='baja',
            field=models.BooleanField(default=0),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre_completo')),
                ('telefono', models.CharField(max_length=150, verbose_name='telefono')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('mensaje', models.CharField(max_length=400, verbose_name='mensaje')),
                ('pendiente', models.BooleanField(default=0)),
                ('asunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tornquist.tipoconsulta', verbose_name='asunto')),
            ],
        ),
    ]