# Generated by Django 4.2.11 on 2024-04-24 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('ACCOUNT_ID', models.AutoField(primary_key=True, serialize=False)),
                ('FIRST_NAME', models.CharField(max_length=100)),
                ('LAST_NAME', models.CharField(max_length=100)),
                ('USER_NAME', models.CharField(max_length=100, unique=True)),
                ('BIRTHDATE', models.DateField()),
                ('PHONE_NUMBER', models.CharField(max_length=20)),
                ('EMAIL', models.EmailField(max_length=254, unique=True)),
                ('PASSWORD', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='EquipmentCategory',
            fields=[
                ('CATEGORY_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CATEGORY_NAME', models.TextField()),
            ],
            options={
                'db_table': 'equipment_category',
            },
        ),
        migrations.CreateModel(
            name='EquipmentDetails',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('NAME', models.CharField(max_length=100)),
                ('DESCRIPTION', models.TextField()),
                ('IS_ONSITE_ONLY', models.BooleanField()),
                ('WARRANTY_YEARS', models.IntegerField()),
            ],
            options={
                'db_table': 'equipment_details',
            },
        ),
        migrations.CreateModel(
            name='EquipmentInventory',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('LENT', models.IntegerField()),
                ('AVAILABLE', models.IntegerField()),
            ],
            options={
                'db_table': 'equipment_inventory',
            },
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('RESERVATION_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CREATED_DATE', models.TextField()),
                ('CREATED_TIME', models.TextField()),
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.accounts')),
            ],
            options={
                'db_table': 'reservations',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('ROLE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('ROLE_TYPE', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=10)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='ReservationStatus',
            fields=[
                ('RESERVATION_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inventory.reservations')),
                ('STATUS', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=10)),
            ],
            options={
                'db_table': 'reservation_status',
            },
        ),
        migrations.CreateModel(
            name='UserSignupStatus',
            fields=[
                ('USER_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inventory.accounts')),
                ('STATUS', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=10)),
            ],
            options={
                'db_table': 'user_signup_status',
            },
        ),
        migrations.CreateModel(
            name='EquipmentReservations',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('BORROW_DATE', models.TextField()),
                ('RETURN_DATE', models.TextField()),
                ('PURPOSE', models.TextField()),
                ('RESERVATION_TYPE', models.CharField(choices=[('onsite', 'Onsite'), ('borrow', 'Borrow')], max_length=10)),
                ('EQUIPMENT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.equipmentdetails')),
                ('RESERVATION_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.reservations')),
            ],
            options={
                'db_table': 'equipment_reservations',
            },
        ),
        migrations.AddField(
            model_name='equipmentdetails',
            name='AVAILABILITY_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.equipmentinventory'),
        ),
        migrations.AddField(
            model_name='equipmentdetails',
            name='CATEGORY_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.equipmentcategory'),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('STREET', models.CharField(max_length=100)),
                ('CITY', models.CharField(max_length=100)),
                ('PROVINCE', models.CharField(max_length=100)),
                ('POSTAL_CODE', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'addresses',
                'unique_together': {('STREET', 'CITY', 'PROVINCE', 'POSTAL_CODE')},
            },
        ),
        migrations.AddField(
            model_name='accounts',
            name='ADDRESS_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.addresses'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='ROLE_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.roles'),
        ),
    ]