# Generated by Django 3.1.5 on 2022-04-15 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coloring', '0003_alter_drawing_drawingfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drawing',
            old_name='drawingFile',
            new_name='drawing',
        ),
    ]
