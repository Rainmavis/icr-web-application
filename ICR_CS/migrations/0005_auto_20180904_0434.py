# Generated by Django 2.0.5 on 2018-09-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ICR_CS', '0004_auto_20180904_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='foto',
            field=models.ImageField(default='images/recursos/None/no-img.jpg', upload_to='images/'),
        ),
    ]