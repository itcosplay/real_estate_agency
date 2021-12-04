# Generated by Django 2.2.24 on 2021-12-04 13:38

from django.db import migrations


def get_owner_flats(owner, model):
    owner_flats = model.objects.filter (
        owner=owner.owner, 
        owners_phonenumber=owner.owners_phonenumber, 
        owner_pure_phone=owner.owner_pure_phone
    )

    return owner_flats


def bind_owner_flat(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    
    for owner in Owner.objects.all():
        owner_flats = get_owner_flats(owner, Flat)

        for owner_flat in owner_flats:
            owner.flats.add(owner_flat)

        owner.save()


def move_backward(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    
    for owner in Owner.objects.all():
        owner_flats = owner.flats.all()

        for owner_flat in owner_flats:
            owner.flats.remove(owner_flat)

        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20211204_1537'),
    ]

    operations = [
        migrations.RunPython(bind_owner_flat, move_backward),
    ]
