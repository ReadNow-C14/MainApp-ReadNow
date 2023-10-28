# Generated by Django 4.2.6 on 2023-10-27 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0002_auto_20231024_1251'),
        ('main', '0002_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
            options={
                'verbose_name': 'Homepage',
                'verbose_name_plural': 'Homepage',
            },
        ),
    ]
