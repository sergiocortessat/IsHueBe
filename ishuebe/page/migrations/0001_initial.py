# Generated by Django 3.0.7 on 2020-06-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Emotion')),
                ('group', models.CharField(blank=True, max_length=120)),
                ('ref', models.CharField(max_length=200, verbose_name='Link ref:')),
                ('refType', models.CharField(max_length=120, verbose_name='type of link')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Emotion')),
                ('group', models.CharField(blank=True, max_length=120)),
                ('ref', models.CharField(max_length=200, verbose_name='Link ref:')),
                ('refType', models.CharField(max_length=120, verbose_name='type of link')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disgusted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Emotion')),
                ('group', models.CharField(blank=True, max_length=120)),
                ('ref', models.CharField(max_length=200, verbose_name='Link ref:')),
                ('refType', models.CharField(max_length=120, verbose_name='type of link')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fearful',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Emotion')),
                ('group', models.CharField(blank=True, max_length=120)),
                ('ref', models.CharField(max_length=200, verbose_name='Link ref:')),
                ('refType', models.CharField(max_length=120, verbose_name='type of link')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Happy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Emotion')),
                ('group', models.CharField(blank=True, max_length=120)),
                ('ref', models.CharField(max_length=200, verbose_name='Link ref:')),
                ('refType', models.CharField(max_length=120, verbose_name='type of link')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Emotion')),
                ('group', models.CharField(blank=True, max_length=120)),
                ('ref', models.CharField(max_length=200, verbose_name='Link ref:')),
                ('refType', models.CharField(max_length=120, verbose_name='type of link')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Surprised',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Emotion')),
                ('group', models.CharField(blank=True, max_length=120)),
                ('ref', models.CharField(max_length=200, verbose_name='Link ref:')),
                ('refType', models.CharField(max_length=120, verbose_name='type of link')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
