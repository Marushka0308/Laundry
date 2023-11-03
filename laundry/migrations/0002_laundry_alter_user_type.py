# Generated by Django 4.1.3 on 2023-11-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='laundry/files/laundries')),
                ('phone_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(default='customer', max_length=10),
        ),
    ]