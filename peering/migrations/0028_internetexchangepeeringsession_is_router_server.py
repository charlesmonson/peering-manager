# Generated by Django 2.1.4 on 2019-01-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("peering", "0027_auto_20190105_1600")]

    operations = [
        migrations.AddField(
            model_name="internetexchangepeeringsession",
            name="is_route_server",
            field=models.BooleanField(blank=True, default=False),
        )
    ]