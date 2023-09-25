from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# CUSTOM USER MODELS
class CustomUserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self):
    ...

  def create_user(self):
    ...

  def create_superuser(self):
    ...


# USER
class Client(AbstractUser):
  register_number = models.CharField()
  # password = models.CharField()
  picture = models.ImageField()

  def __str__(self):
    return self.register_number


class NaturalPerson():
  client = models.OneToOneField(Client, on_delete=models.CASCADE)
  name = models.CharField()
  birthdate = models.DateField()
  cpf = models.CharField()
  rg = models.CharField()
  social_name = models.CharField()

  class Meta:
    verbose_name = 'Natural Person'
    verbose_name_plural = 'Natural People'

  def __str__(self):
    return self.name


class LegalPerson():
  client = models.OneToOneField(Client, on_delete=models.CASCADE)
  fantasy_name = models.CharField()
  establishment_date = models.DateField()
  cnpj = models.CharField()
  im = models.CharField()  # inscrição municipal
  ie = models.CharField()  # inscrição estadual
  legal_nature = models.CharField()

  class Meta:
    verbose_name = 'Legal Person'
    verbose_name_plural = 'Legal People'

  def __str__(self):
    return self.fantasy_name


# OTHER
class Email():
  client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='email_client')
  email = models.EmailField(null=True, blank=True)

  class Meta:
    verbose_name = 'Email'
    verbose_name_plural = 'Emails'

  def __str__(self):
    return self.email
  

class Phone():
  client = models.OneToOneField(Client, on_delete=models.CASCADE)
  phone = models.CharField(max_length=8)
  country_code = models.CharField(max_length=3)
  prefix_number = models.CharField(max_length=3)

  class Meta:
    verbose_name = 'Telephone'
    verbose_name_plural = 'Telephones'

  def __str__(self):
    return self.phone


class Address():
  client = models.OneToOneField(Client, on_delete=models.CASCADE)
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
    return self.cep
  

# ACCOUNT
class Account():
  OPTIONS = (
    ('checking', 'checking'),
    ('savings ', 'savings ')
  )

  client = models.ManyToManyField(Client)
  number = models.CharField(max_length=8)
  agency = models.CharField(max_length=8)
  acc_type = models.CharField(choices=OPTIONS)
  credit_limit = models.FloatField()
  is_active = models.BooleanField()

  class Meta:
    verbose_name = 'Account'
    verbose_name_plural = 'Accounts'

  def __str__(self):
    return self.number
  

class Investment():
  account = models.ManyToOneRel(Account, on_delete=models.CASCADE)
  investment_type = models.CharField(max_length=50)
  contribution = models.FloatField()  # amount
  income = models.FloatField()
  admin_fee = models.FloatField()
  period = models.DateField()
  risc_rate = models.FloatField()
  profitability = models.FloatField()

  class Meta:
    verbose_name = 'Investment'
    verbose_name_plural = 'Investments'

  def __str__(self):
    return self.investment_type
  

class Loan():
  account = models.ManyToOneRel(Account, on_delete=models.CASCADE)
  amount_request = models.FloatField()
  interest_rate = models.FloatField()
  is_payout = models.BooleanField()
  installment_amount = models.IntegerField()
  request_date = models.DateField()
  approval_date = models.DateField()
  observation = models.TextField(max_length=300)

  class Meta:
    verbose_name = 'Loan'
    verbose_name_plural = 'Loans'

  def __str__(self):
    return self.amount_request


class Installment():
  loan = models.ManyToOneRel(Loan, on_delete=models.CASCADE)
  number = models.CharField(max_length=8)
  payment_amount = models.FloatField()
  payment_date = models.DateField()
  expiration_date = models.DateField()

  class Meta:
    verbose_name = 'Installment'
    verbose_name_plural = 'Installments'

  def __str__(self):
    return self.number


class Card():
  account = models.ManyToOneRel(Account, on_delete=models.CASCADE)
  number = models.CharField(max_length=16)
  verification_code = models.CharField(max_length=3)
  flag = models.CharField(max_length=20)
  expiration_date = models.DateField()
  is_active = models.BooleanField()

  class Meta:
    verbose_name = 'Card'
    verbose_name_plural = 'Cards'

  def __str__(self):
    return self.number
  

class Transaction():
  OPTIONS = (
    ('Credit', 'Credit'),
    ('Debit', 'Debit')
  )
  card = models.ManyToOneRel(Card, on_delete=models.CASCADE)
  amount = models.FloatField()
  transaction_type = models.CharField(choices=OPTIONS)
  timestamp = models.DateTimeField()

  class Meta:
    verbose_name = 'Transaction'
    verbose_name_plural = 'Transactions'

  def __str__(self):
    return self.transaction_type
  