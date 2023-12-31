# Generated by Django 4.2.4 on 2023-08-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0008_veiculo_acessorio_alter_veiculo_modelo"),
    ]

    operations = [
        migrations.AddField(
            model_name="veiculo",
            name="description",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="veiculo",
            name="image",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="veiculo",
            name="name",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
