# Generated by Django 3.2.5 on 2021-09-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_alter_jobmodel_work_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='work_category',
            field=models.CharField(choices=[('ИТ', 'ИТ'), ('Ремонтни Дейности', 'Ремонтни Дейности'), ('Монтажни Дейности', 'Монтажни Дейности'), ('Занаяти', 'Занаяти'), ('Поддръжка на автомобили', 'Поддръжка на автомобили'), ('Здраве и фитнес', 'Здраве и фитнес'), ('Транспорт и логистика', 'Транспорт и логистика'), ('Продажби, Маркетинг, ПР', 'Продажби, Маркетинг, ПР'), ('Финанси/Счетоводни услуги', 'Финанси/Счетоводни услуги'), ('Друго', 'Друго')], default='IT', max_length=50),
        ),
    ]
