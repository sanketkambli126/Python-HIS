# Generated by Django 2.1.15 on 2020-02-01 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('claim_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_closed', models.BooleanField(null=True)),
                ('is_cancelled', models.BooleanField(null=True)),
                ('is_approved', models.BooleanField(null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(null=True)),
                ('pretreatment_date', models.DateTimeField(null=True)),
                ('pretreatment_amount', models.DecimalField(decimal_places=4, max_digits=18, null=True)),
                ('postreatment_amount', models.DecimalField(decimal_places=4, max_digits=18, null=True)),
                ('posttreatment_date', models.DateTimeField(null=True)),
                ('is_paid', models.BooleanField()),
            ],
            options={
                'db_table': 'Claim',
            },
        ),
        migrations.CreateModel(
            name='ClaimSettlementinfo',
            fields=[
                ('claimsettlement_id', models.AutoField(primary_key=True, serialize=False)),
                ('claim_settlement_amount', models.DecimalField(decimal_places=4, max_digits=18, null=True)),
                ('claim_settlement_date', models.DateTimeField(auto_now=True)),
                ('is_claimfullypaid', models.BooleanField(null=True)),
                ('claim_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HIS.Claim')),
            ],
            options={
                'db_table': 'ClaimSettlementinfo',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('company_email', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('startd_ate', models.DateTimeField()),
            ],
            options={
                'db_table': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Hospital',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('member_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('contact_details', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'Member',
            },
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('premium', models.DecimalField(decimal_places=4, max_digits=18)),
                ('sum_assured', models.DecimalField(decimal_places=4, max_digits=18)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField()),
                ('company_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='HIS.Company')),
            ],
            options={
                'db_table': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('policy_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(null=True)),
                ('is_renewed', models.BooleanField()),
                ('total_amount_canclaim', models.DecimalField(decimal_places=4, max_digits=18)),
                ('issued_date', models.DateTimeField(null=True)),
                ('inception_date', models.DateTimeField(null=True)),
                ('expiry_date', models.DateTimeField()),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HIS.Member')),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HIS.Plans')),
            ],
            options={
                'db_table': 'Policy',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('treatment_id', models.AutoField(primary_key=True, serialize=False)),
                ('admission_date', models.DateField()),
                ('discharge_date', models.DateField()),
                ('treatment_cost', models.DecimalField(decimal_places=4, max_digits=18, null=True)),
                ('claim_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HIS.Claim')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HIS.Hospital')),
            ],
            options={
                'db_table': 'Treatment',
            },
        ),
    ]