from django.shortcuts import render
from rest_framework import viewsets

from app.models import (
    NaturalPerson,
    LegalPerson,
    Email,
    Phone,
    Address,
    Account,
    Investment,
    Loan,
    Installment,
    Card,
    Transaction,
)

from app.serializers import (
    NaturalPersonSerializer,
    NaturalPersonPostPatchSerializer,
    LegalPersonSerializer,
    LegalPersonPostPatchSerializer,
    EmailSerializer,
    PhoneSerializer,
    AddressSerializer,
    AccountSerializer,
    InvestmentSerializer,
    AccountInvestmentSerializer,
    LoanSerializer,
    InstallmentSerializer,
    CardSerializer,
    TransactionSerializer,
)

from app.permissions import (
    CustomerGetPostPatch,
    CustomerGetPermission,
    # SuperUserPermission,
    # CustomerPostPermission,
    # DeletePermission,
)
