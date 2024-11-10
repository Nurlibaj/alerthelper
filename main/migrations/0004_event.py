# Generated by Django 5.1.3 on 2024-11-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_restroom_floor_restroom_status_alter_restroom_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('people_count', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='events_images/')),
            ],
        ),
    ]