from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    NaturalPersonViewSet,
    LegalPersonViewSet,
    EmailViewSet,
    PhoneViewSet,
    AddressViewSet,
    AccountViewSet,
    InvestmentViewSet,
    LoanViewSet,
    InstallmentViewSet,
    CardViewSet,
    TransactioViewSet
)


router = SimpleRouter()
router.register('natural-people', NaturalPersonViewSet)
router.register('legal-people', LegalPersonViewSet)
router.register('emails', EmailViewSet)
router.register('phones', PhoneViewSet)
router.register('addresses', AddressViewSet)
router.register('accounts', AccountViewSet)
router.register('investments', InvestmentViewSet)
router.register('loans', LoanViewSet)
router.register('installments', InstallmentViewSet)
router.register('cards', CardViewSet)
router.register('transactions', TransactioViewSet)


urlpatterns = []
