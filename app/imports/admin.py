from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.forms import CustomerCreateForm, CustomerChangeForm
from app.models import (
    Customer,
    NaturalPerson,
    LegalPerson,
    Email,
    Phone,
    Address,
    Account,
    Investment,
    AccountInvestment,
    Loan,
    Installment,
    Card,
    Transaction,
    BankStatement,
    CardStatement,
)
