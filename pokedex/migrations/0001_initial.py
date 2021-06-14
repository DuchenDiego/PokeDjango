# Generated by Django 3.2.4 on 2021-06-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDpoke', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=300)),
                ('Peso', models.DecimalField(decimal_places=2, max_digits=2)),
                ('Altura', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]