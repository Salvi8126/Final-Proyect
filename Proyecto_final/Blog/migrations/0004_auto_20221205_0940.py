# Generated by Django 2.2.3 on 2022-12-05 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_libros_venta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros_venta',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
