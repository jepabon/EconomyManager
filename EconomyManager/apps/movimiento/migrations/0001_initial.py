# Generated by Django 2.2 on 2019-05-01 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha', models.DateTimeField(null=True, verbose_name='Fecha')),
                ('monto', models.FloatField(null=True, verbose_name='Monto')),
                ('naturaleza', models.BooleanField(default=1, verbose_name='Naturaleza')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.Categoria', verbose_name='Categoría')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuenta.Cuenta', verbose_name='Cuenta')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propietario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
