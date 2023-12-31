# Generated by Django 4.2.5 on 2023-10-28 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_return_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pinjam_buku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Borrow',
        ),
    ]
