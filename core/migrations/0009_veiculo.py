# Generated by Django 5.2 on 2025-05-06 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_modelo_site_modelo_categoria_modelo_marca_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ano', models.IntegerField(blank=True, default=0, null=True)),
                ('Preco', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('Acessorio', models.ManyToManyField(blank=True, null=True, related_name='veiculos', to='core.acessorio')),
                ('Cor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='core.cor')),
                ('Modelo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='veiculos', to='core.modelo')),
            ],
        ),
    ]
