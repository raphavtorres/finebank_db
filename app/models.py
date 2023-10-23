from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model

from django.core.validators import MaxValueValidator


# CUSTOM USER MODELS
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, register_number, password, **extra_fields):
        if not register_number:
            raise ValueError('Register Number is required')
        user = self.model(register_number=register_number,
                          username=register_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, register_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(register_number, password, **extra_fields)

    def create_superuser(self, register_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser needs the is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser needs the is_staff=True')

        return self._create_user(register_number, password, **extra_fields)


# BASE
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


# USER
class Customer(AbstractUser):
    register_number = models.IntegerField(
        validators=[MaxValueValidator(999999999999999999999999)],
        unique=True,
        primary_key=True
    )
    picture = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'register_number'

    def __str__(self):
        return f'{self.register_number}'

    objects = CustomUserManager()


class NaturalPerson(Base):
    customer = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    birthdate = models.DateField()
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=9)
    social_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Natural Person'
        verbose_name_plural = 'Natural People'

    def __str__(self):
        return f'{self.name}'


class LegalPerson(Base):
    customer = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    fantasy_name = models.CharField(max_length=50)
    legal_nature = models.CharField(max_length=50)
    establishment_date = models.DateField()
    cnpj = models.CharField(max_length=14)
    im = models.CharField(max_length=25)  # inscrição municipal
    ie = models.CharField(max_length=25)  # inscrição estadual

    class Meta:
        verbose_name = 'Legal Person'
        verbose_name_plural = 'Legal People'

    def __str__(self):
        return f'{self.fantasy_name}'


# OTHER
class Email(Base):
    customer = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='email_customer')
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return f'{self.email}'


class Phone(Base):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    phone = models.CharField(max_length=8)
    country_code = models.CharField(max_length=3)
    prefix_number = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Telephone'
        verbose_name_plural = 'Telephones'

    def __str__(self):
        return f'{self.phone}'


class Address(Base):
    customer = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=4)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.cep}'


# ACCOUNT
class Account(Base):
    # corrente
    # poupança
    OPTIONS = [
        ('checking', 'checking'),
        ('savings', 'savings')
    ]

    customer = models.ManyToManyField(get_user_model())
    number = models.CharField(max_length=8)
    agency = models.CharField(max_length=8)
    acc_type = models.CharField(choices=OPTIONS, max_length=9)
    credit_limit = models.DecimalField(max_digits=9, decimal_places=2)
    balance = models.DecimalField(decimal_places=2, max_digits=9)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return f'{self.number}'


# INVESTMENT
class InvestmentBase(Base):
    """Model used in heritage to Investment and AccountInvestment
    to avoid code repetition"""
    OPTIONS = [
        ('Tesouro Direto', 'Tesouro Direto'),
        ('CDB', 'CDB'),
        ('LCI', 'LCI')
    ]

    RISC_RATE = [
        ('Baixo', 'Baixo'),
        ('Médio', 'Médio'),
        ('Alto', 'Alto')
    ]

    investment_type = models.CharField(choices=OPTIONS, max_length=50)
    contribution = models.FloatField()  # valor do investimento
    admin_fee = models.FloatField()  # IR
    period = models.DateField()  # data de vencimento
    risc_rate = models.CharField(
        choices=RISC_RATE, max_length=5)  # alto, médio, baixo
    profitability = models.FloatField()  # rendimento anual


class Investment(InvestmentBase):

    class Meta:
        verbose_name = 'Investment'
        verbose_name_plural = 'Investments'

    def __str__(self):
        return f'{self.investment_type}'


class AccountInvestment(InvestmentBase):
    id_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    income = models.FloatField()  # quanto rendeu

    class Meta:
        verbose_name = 'Account Investment'
        verbose_name_plural = 'Account Investments'

    def __str__(self):
        return f'{self.investment_type}'


class Loan(Base):
    id_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount_request = models.FloatField()
    interest_rate = models.FloatField()
    is_payout = models.BooleanField()
    installment_amount = models.IntegerField(default=1,
                                             validators=[
                                                 MaxValueValidator(10)
                                             ])
    request_date = models.DateTimeField(auto_now_add=True)
    approval_date = models.DateField()
    is_approved = models.BooleanField(default=False)
    observation = models.TextField(max_length=300)

    class Meta:
        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'

    def __str__(self):
        return f'{self.amount_request}'


class Installment(Base):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    number = models.CharField(max_length=8)
    payment_amount = models.FloatField()
    payment_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Installment'
        verbose_name_plural = 'Installments'

    def __str__(self):
        return f'{self.number}'


class Card(Base):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.CharField(max_length=16)
    verification_code = models.CharField(max_length=3)
    flag = models.CharField(max_length=20)
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    def __str__(self):
        return f'{self.number}'


class Transaction(Base):
    OPTIONS = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit')
    ]
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    amount = models.FloatField()
    transaction_type = models.CharField(choices=OPTIONS, max_length=6)
    timestamp = models.DateTimeField()

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'{self.transaction_type}'
