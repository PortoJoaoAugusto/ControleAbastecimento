# Generated by Django 4.0.6 on 2022-10-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Abastecimento', '0002_bomba_rename_abastecimentos_abastecimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='descricao',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
