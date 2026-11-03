# Initial migration for the Motoriec Spare model.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Spare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('stock', models.CharField(max_length=50)),
            ],
        ),
    ]
