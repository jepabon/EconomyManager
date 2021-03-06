# Generated by Django 2.2 on 2019-05-01 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categoria_cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('nombre', models.CharField(max_length=50, null=True, verbose_name='Nombre')),
                ('balance', models.FloatField(null=True, verbose_name='Balance')),
                ('categoria_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria_cuenta.CategoriaCuenta', verbose_name='Categoria Cuenta')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Propietario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
