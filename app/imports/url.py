from django.urls import path

from rest_framework.routers import SimpleRouter

from app.views import (
    NaturalPersonViewSet,
    LegalPersonViewSet,
    EmailViewSet,
    PhoneViewSet,
    AddressViewSet,
    AccountViewSet,
    InvestmentViewSet,
    AccountInvestmentViewSet,
    LoanViewSet,
    InstallmentViewSet,
    CardViewSet,
    TransactionViewSet,
)
