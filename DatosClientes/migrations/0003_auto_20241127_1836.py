# Generated by Django 3.2.25 on 2024-11-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DatosClientes', '0002_alter_cliente_nivel_de_satisfaccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Cliente_ID',
        ),
        migrations.AddField(
            model_name='cliente',
            name='id',
            field=models.BigAutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
