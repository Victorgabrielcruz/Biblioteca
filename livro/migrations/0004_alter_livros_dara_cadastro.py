# Generated by Django 5.0.3 on 2024-03-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0003_livros_co_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='dara_cadastro',
            field=models.DateField(auto_now=True),
        ),
    ]
