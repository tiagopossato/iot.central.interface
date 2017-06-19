# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, max_length=48, null=True)),
                ('codigoAlarme', models.CharField(max_length=36)),
                ('mensagemAlarme', models.CharField(max_length=255)),
                ('prioridadeAlarme', models.IntegerField()),
                ('ativo', models.BooleanField(default=False)),
                ('tempoAtivacao', models.DateTimeField()),
                ('syncAtivacao', models.BooleanField(default=False)),
                ('tempoInativacao', models.DateTimeField(null=True)),
                ('syncInativacao', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Alarmes',
                'verbose_name': 'Alarme',
            },
        ),
        migrations.CreateModel(
            name='AlarmeAnalogico',
            fields=[
                ('codigoAlarme', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('mensagemAlarme', models.CharField(max_length=255, verbose_name='Mensagem do alarme')),
                ('prioridadeAlarme', models.IntegerField(verbose_name='Prioridade do alarme')),
                ('valorAlarmeOn', models.FloatField(verbose_name='Valor para ativar o alarme')),
                ('valorAlarmeOff', models.FloatField(verbose_name='Valor para desativar o alarme')),
            ],
            options={
                'verbose_name_plural': 'Alarmes Analógicos',
                'verbose_name': 'Alarme Analógico',
            },
        ),
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('uid', models.CharField(blank=True, max_length=48, null=True)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Ambientes',
                'verbose_name': 'Ambiente',
            },
        ),
        migrations.CreateModel(
            name='Configuracoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uidCentral', models.CharField(max_length=48, unique=True)),
                ('maxAlarmes', models.IntegerField()),
                ('portaSerial', models.CharField(default='/dev/ttyAMA0', max_length=20)),
                ('taxa', models.IntegerField(default=115200)),
            ],
            options={
                'verbose_name_plural': 'Configurações',
                'verbose_name': 'Configuração',
            },
        ),
        migrations.CreateModel(
            name='EntradaDigital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nome', models.CharField(max_length=255)),
                ('estado', models.BooleanField(default=False)),
                ('triggerAlarme', models.BooleanField(default=False, verbose_name='Estado para alarme')),
                ('codigoAlarme', models.CharField(default=None, max_length=36)),
                ('mensagemAlarme', models.CharField(max_length=255, verbose_name='Mensagem do alarme')),
                ('prioridadeAlarme', models.IntegerField(verbose_name='Prioridade do alarme')),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('sync', models.BooleanField(default=False)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Ambiente')),
            ],
            options={
                'verbose_name_plural': 'Entradas digitais',
                'verbose_name': 'Entrada digital',
            },
        ),
        migrations.CreateModel(
            name='Grandeza',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('unidade', models.CharField(max_length=15, unique=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('sync', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Grandezas',
                'verbose_name': 'Grandeza',
            },
        ),
        migrations.CreateModel(
            name='Leitura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('sync', models.BooleanField(default=False)),
                ('ambiente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='central.Ambiente')),
                ('grandeza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Grandeza')),
            ],
            options={
                'verbose_name_plural': 'Leituras',
                'verbose_name': 'Leitura',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=6)),
                ('mensagem', models.CharField(max_length=255)),
                ('sync', models.BooleanField(default=False)),
                ('tempo', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Logs',
                'verbose_name': 'Log',
            },
        ),
        migrations.CreateModel(
            name='PlacaExpansaoDigital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRede', models.IntegerField(unique=True)),
                ('descricao', models.CharField(max_length=255, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Placas de expansão digital',
                'verbose_name': 'Placa de expansão digital',
            },
        ),
        migrations.CreateModel(
            name='SaidaDigital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nome', models.CharField(max_length=255)),
                ('ativa', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=False)),
                ('tempoLigado', models.IntegerField(verbose_name='Tempo ligado em segundos')),
                ('tempoDesligado', models.IntegerField(verbose_name='Tempo desligado em segundos')),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('ultimoAcionamento', models.DateTimeField(null=True)),
                ('sync', models.BooleanField(default=False)),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Ambiente')),
                ('placaExpansaoDigital', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.PlacaExpansaoDigital', to_field='idRede', verbose_name='Placa de expansão digital')),
            ],
            options={
                'verbose_name_plural': 'Saidas digitais',
                'verbose_name': 'Saida digital',
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idRede', models.IntegerField(unique=True)),
                ('uid', models.CharField(blank=True, max_length=48, null=True)),
                ('descricao', models.CharField(default='', max_length=255, unique=True)),
                ('intervaloAtualizacao', models.IntegerField(default=2)),
                ('intervaloLeitura', models.IntegerField(default=2)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('sync', models.BooleanField(default=False)),
                ('ambiente', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='central.Ambiente')),
            ],
            options={
                'verbose_name_plural': 'Sensores',
                'verbose_name': 'Sensor',
            },
        ),
        migrations.CreateModel(
            name='SensorGrandeza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obs', models.CharField(blank=True, max_length=255, null=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('curvaCalibracao', models.CharField(max_length=255)),
                ('sync', models.BooleanField(default=False)),
                ('grandeza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Grandeza')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Sensor', to_field='idRede')),
            ],
            options={
                'verbose_name_plural': 'Grandezas dos Sensores',
                'verbose_name': 'Grandeza do Sensor',
            },
        ),
        migrations.AddField(
            model_name='sensor',
            name='grandezas',
            field=models.ManyToManyField(through='central.SensorGrandeza', to='central.Grandeza'),
        ),
        migrations.AddField(
            model_name='leitura',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Sensor', to_field='idRede'),
        ),
        migrations.AddField(
            model_name='entradadigital',
            name='placaExpansaoDigital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.PlacaExpansaoDigital', to_field='idRede', verbose_name='Placa de expansão digital'),
        ),
        migrations.AddField(
            model_name='alarmeanalogico',
            name='ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Ambiente'),
        ),
        migrations.AddField(
            model_name='alarmeanalogico',
            name='grandeza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Grandeza'),
        ),
        migrations.AddField(
            model_name='alarme',
            name='ambiente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='central.Ambiente'),
        ),
        migrations.AlterUniqueTogether(
            name='sensorgrandeza',
            unique_together=set([('grandeza', 'sensor')]),
        ),
        migrations.AlterUniqueTogether(
            name='saidadigital',
            unique_together=set([('placaExpansaoDigital', 'numero')]),
        ),
        migrations.AlterUniqueTogether(
            name='entradadigital',
            unique_together=set([('placaExpansaoDigital', 'numero')]),
        ),
    ]
