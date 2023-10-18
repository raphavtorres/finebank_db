# Generated by Django 4.2.5 on 2023-10-18 19:33

import app.models
from django.conf import settings
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('register_number', models.IntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(999999999999999999999999)])),
                ('picture', models.CharField(max_length=255)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', app.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('number', models.CharField(max_length=8)),
                ('agency', models.CharField(max_length=8)),
                ('acc_type', models.CharField(choices=[('checking', 'checking'), ('savings ', 'savings ')], max_length=9)),
                ('credit_limit', models.DecimalField(decimal_places=2, max_digits=9)),
                ('is_active', models.BooleanField(default=True)),
                ('customer', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('number', models.CharField(max_length=16)),
                ('verification_code', models.CharField(max_length=3)),
                ('flag', models.CharField(max_length=20)),
                ('expiration_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('investment_type', models.CharField(max_length=50)),
                ('contribution', models.FloatField()),
                ('income', models.FloatField()),
                ('admin_fee', models.FloatField()),
                ('period', models.DateField()),
                ('risc_rate', models.FloatField()),
                ('profitability', models.FloatField()),
            ],
            options={
                'verbose_name': 'Investment',
                'verbose_name_plural': 'Investments',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('amount', models.FloatField()),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=6)),
                ('timestamp', models.DateTimeField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.card')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=8)),
                ('country_code', models.CharField(max_length=3)),
                ('prefix_number', models.CharField(max_length=3)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Telephone',
                'verbose_name_plural': 'Telephones',
            },
        ),
        migrations.CreateModel(
            name='NaturalPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=9)),
                ('social_name', models.CharField(max_length=50)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Natural Person',
                'verbose_name_plural': 'Natural People',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('amount_request', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('is_payout', models.BooleanField()),
                ('installment_amount', models.IntegerField()),
                ('request_date', models.DateField()),
                ('approval_date', models.DateField()),
                ('observation', models.TextField(max_length=300)),
                ('id_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
            options={
                'verbose_name': 'Loan',
                'verbose_name_plural': 'Loans',
            },
        ),
        migrations.CreateModel(
            name='LegalPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('fantasy_name', models.CharField(max_length=50)),
                ('legal_nature', models.CharField(max_length=50)),
                ('establishment_date', models.DateField()),
                ('cnpj', models.CharField(max_length=14)),
                ('im', models.CharField(max_length=25)),
                ('ie', models.CharField(max_length=25)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Legal Person',
                'verbose_name_plural': 'Legal People',
            },
        ),
        migrations.CreateModel(
            name='Installment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('number', models.CharField(max_length=8)),
                ('payment_amount', models.FloatField()),
                ('payment_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.loan')),
            ],
            options={
                'verbose_name': 'Installment',
                'verbose_name_plural': 'Installments',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email',
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('neighborhood', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=4)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='AccountInvestment',
            fields=[
                ('investment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.investment')),
                ('id_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
            options={
                'verbose_name': 'Account Investment',
                'verbose_name_plural': 'Account Investments',
            },
            bases=('app.investment',),
        ),
    ]
