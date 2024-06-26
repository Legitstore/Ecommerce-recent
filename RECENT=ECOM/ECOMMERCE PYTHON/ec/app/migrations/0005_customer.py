# Generated by Django 4.2.4 on 2023-08-28 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_product_category_alter_product_compisition_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Delta', 'Delta'), ('Edo', 'Edo'), ('Ebonyi', 'Ebonyi'), ('Imo', 'Imo'), ('Uyo', 'Uyo'), ('Oyo', 'Oyo'), ('Lagos', 'Lagos'), ('Ekiti', 'Ekiti'), ('Abia', 'Abia'), ('Bayelsa', 'Bayelsa'), ('Rivers', 'Rivers'), ('Cross River', 'Cross River'), ('Ondo', 'Ondo'), ('Ogun', 'Ogun'), ('Osun', 'Osun'), ('Gobe', 'Gobe'), ('Kano', 'Kano'), ('Kaduna', 'Kaduna'), ('Kebbi', 'Kebbi'), ('Adamawa', 'Adamawa'), ('Akwaibom', 'Akwaibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Benue', 'Benue'), ('Bonue', 'Bonue')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
