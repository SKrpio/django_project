# Generated by Django 4.2.2 on 2023-07-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField(null=True)),
                ('pub_date', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
    ]
