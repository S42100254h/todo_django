# Generated by Django 4.1.6 on 2023-02-11 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['completed', '-created_at'],
            },
        ),
    ]
