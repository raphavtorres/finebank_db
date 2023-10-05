from django.shortcuts import render
from rest_framework import viewsets

from .models import (
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

from .serializers import (
    NaturalPersonSerializer,
    LegalPersonSerializer,
    EmailSerializer,
    PhoneSerializer,
    AddressSerializer,
    AccountSerializer,
    InvestmentSerializer,
    LoanSerializer,
    InstallmentSerializer,
    CardSerializer,
    TransactionSerializer,
)


class NaturalPersonViewSet(viewsets.ModelViewSet):
    permission_classes = []

    queryset = NaturalPerson.objects.all()
    serializer_class = NaturalPersonSerializer


class LegalPersonViewSet(viewsets.ModelViewSet):
    permission_classes = []

    queryset = LegalPerson.objects.all()
    serializer_class = LegalPersonSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
