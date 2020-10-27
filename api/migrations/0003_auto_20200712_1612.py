# Generated by Django 3.0.5 on 2020-07-12 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200712_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
