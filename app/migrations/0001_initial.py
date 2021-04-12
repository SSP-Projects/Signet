from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('center_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('CIF', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user_id', models.UUIDField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='user'))),
                ('dni', models.CharField(max_length=50)),
                ('ss_number', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Signing',
            fields=[
                ('signing_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('employee_id', models.UUIDField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='employee'))),
                ('date', models.DateField(auto_now_add=True)),
                ('start_work', models.TimeField(auto_now_add=True)),
                ('start_rest', models.TimeField(blank=True)),
                ('end_rest', models.TimeField(blank=True)),
                ('end_work', models.TimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('permission', models.IntegerField(choices=[(0, 'Employee'), (1, 'Center'), (2, 'Admin')])),
                ('center_id', models.UUIDField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='centers'))),
                ('password_changed', models.BooleanField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
