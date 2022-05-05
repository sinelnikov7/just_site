# Generated by Django 4.0.4 on 2022-04-28 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models1', '0004_alter_profession_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profession',
            name='human',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.PROTECT, to='models1.poduct', unique=True),
        ),
        migrations.AlterField(
            model_name='profession',
            name='profession',
            field=models.IntegerField(choices=[(1, 'Электрик'), (2, 'Сварщик'), (3, 'Конструктор'), (4, 'Пилот'), (5, 'Проект менеджер'), (6, 'Строитель')], default=1, help_text='Выберите профессию'),
        ),
    ]
