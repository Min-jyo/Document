# Generated by Django 2.2.9 on 2019-12-23 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0002_auto_20191219_0904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instructor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name'], 'verbose_name': '학생', 'verbose_name_plural': '학생 목록'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='Abstract_Student_Table',
        ),
    ]
