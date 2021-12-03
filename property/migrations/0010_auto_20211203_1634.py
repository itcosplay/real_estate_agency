# Generated by Django 2.2.24 on 2021-12-03 13:34
import phonenumbers

from django.db import migrations


def get_pure_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        phone_number = flat.owners_phonenumber
        phone_number = phonenumbers.parse(phone_number, 'RU')
        # phone_number = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
        phone_number = phone_number.national_number
        flat.owner_pure_phone = phone_number
        flat.save()


def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20211203_1630'),
    ]

    operations = [
        migrations.RunPython(get_pure_phone_number, move_backward),
    ]
