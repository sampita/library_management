# Generated by Django 3.0.3 on 2020-02-06 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='librarian',
            new_name='librarian_id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='location',
            new_name='location_id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='yearpublished',
            new_name='year_published',
        ),
        migrations.RenameField(
            model_name='librarian',
            old_name='location',
            new_name='location_id',
        ),
    ]
