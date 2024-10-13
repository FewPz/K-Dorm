# Generated by Django 5.1.1 on 2024-10-11 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('uid', models.TextField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('secret', models.TextField()),
                ('salt', models.TextField()),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('isDisabled', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('handle', models.TextField()),
                ('name', models.TextField()),
                ('visibleToStudents', models.BooleanField(default=False)),
                ('visibleToStaffs', models.BooleanField(default=False)),
                ('visibleToSecurityStaffs', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'activity_category',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'building',
            },
        ),
        migrations.CreateModel(
            name='RecruitmentWave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('announcementText', models.TextField(default=None, null=True)),
            ],
            options={
                'db_table': 'recruitment_wave',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'task',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.TextField()),
                ('note', models.TextField(default=None, null=True)),
                ('date', models.DateTimeField()),
                ('location', models.TextField()),
                ('earnedVolunteerHours', models.FloatField(default=None, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='domain.activitycategory')),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='IdentificationKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('key', models.TextField()),
                ('expiredAt', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identificationKeys', to='domain.account')),
            ],
            options={
                'db_table': 'identification_key',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='maintenanceStaff', to='domain.account')),
            ],
            options={
                'db_table': 'maintenance_staff',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('floor', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='domain.building')),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.CreateModel(
            name='SecurityStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='securityStaff', to='domain.account')),
            ],
            options={
                'db_table': 'security_staff',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='domain.account')),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('studentId', models.CharField(max_length=255)),
                ('isOnBoarded', models.BooleanField(default=False)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='domain.account')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField(default=None, null=True)),
                ('isEvicted', models.BooleanField(default=False)),
                ('recruitmentWave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residences', to='domain.recruitmentwave')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='residences', to='domain.room')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residences', to='domain.student')),
            ],
            options={
                'db_table': 'residence',
            },
        ),
        migrations.CreateModel(
            name='RentBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('cycle', models.DateTimeField()),
                ('isPaid', models.BooleanField(default=False)),
                ('paidDate', models.DateTimeField(default=None, null=True)),
                ('deadline', models.DateTimeField(default=None, null=True)),
                ('fineRate', models.FloatField()),
                ('rentCost', models.FloatField()),
                ('fineCost', models.FloatField()),
                ('extraCost', models.FloatField()),
                ('extraCostNote', models.TextField(default=None, null=True)),
                ('ref', models.TextField(default=None, null=True)),
                ('residence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentBillings', to='domain.residence')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentBillings', to='domain.student')),
            ],
            options={
                'db_table': 'rent_billing',
            },
        ),
        migrations.CreateModel(
            name='MaintenanceTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('location', models.TextField(default=None, null=True)),
                ('resolvedAt', models.DateTimeField(default=None, null=True)),
                ('isResolved', models.BooleanField(default=False)),
                ('maintenanceStaff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenanceTickets', to='domain.maintenancestaff')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenanceTickets', to='domain.student')),
            ],
            options={
                'db_table': 'maintenance_ticket',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('handle', models.TextField()),
                ('note', models.TextField()),
                ('path', models.TextField()),
                ('publiclyVisible', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='domain.activity')),
                ('visibleToMaintenanceStaffs', models.ManyToManyField(related_name='accessToFiles', to='domain.maintenancestaff')),
                ('maintenanceTicket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='domain.maintenanceticket')),
                ('visibleToSecurityStaffs', models.ManyToManyField(related_name='accessToFiles', to='domain.securitystaff')),
                ('visibleToStaffs', models.ManyToManyField(related_name='accessToFiles', to='domain.staff')),
                ('visibleToStudents', models.ManyToManyField(related_name='accessToFiles', to='domain.student')),
            ],
            options={
                'db_table': 'file',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='domain.student'),
        ),
        migrations.CreateModel(
            name='UsageBilling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('deletedAt', models.DateTimeField(blank=True, default=None, null=True)),
                ('cycle', models.DateTimeField()),
                ('deadline', models.DateTimeField(default=None, null=True)),
                ('fineRate', models.FloatField()),
                ('electricityUsage', models.FloatField()),
                ('waterUsage', models.FloatField()),
                ('electricityCost', models.FloatField()),
                ('waterCost', models.FloatField()),
                ('fineCost', models.FloatField()),
                ('extraCost', models.FloatField()),
                ('extraCostNote', models.TextField(default=None, null=True)),
                ('ref', models.TextField(default=None, null=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('paidDate', models.DateTimeField(default=None, null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usageBilling', to='domain.room')),
            ],
            options={
                'db_table': 'usage_billing',
            },
        ),
    ]