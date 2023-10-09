from django.urls import path

from rest_framework.routers import SimpleRouter

from app.views import (
    NaturalPersonGetViewSet,
    NaturalPersonPostViewSet,

    LegalPersonGetViewSet,
    LegalPersonPostViewSet,
    
    EmailViewSet,
    PhoneViewSet,
    AddressViewSet,
    AccountViewSet,
    InvestmentViewSet,
    LoanViewSet,
    InstallmentViewSet,
    CardViewSet,
    TransactionViewSet
)
