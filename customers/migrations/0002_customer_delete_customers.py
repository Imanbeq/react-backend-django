# Generated by Django 4.2.5 on 2023-09-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Customers',
        ),
    ]