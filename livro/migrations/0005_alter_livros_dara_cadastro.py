# Generated by Django 5.0.3 on 2024-03-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0004_alter_livros_dara_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='dara_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
