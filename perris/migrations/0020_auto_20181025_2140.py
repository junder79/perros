# Generated by Django 2.1.2 on 2018-10-26 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perris', '0019_auto_20181024_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perros_rescatados',
            name='estado',
            field=models.CharField(choices=[('1', 'Rescatado'), ('2', 'Disponible'), ('3', 'Adoptado')], default='', max_length=30),
        ),
    ]
