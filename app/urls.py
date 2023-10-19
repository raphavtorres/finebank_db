from .imports.url import *


router = SimpleRouter()

router.register('natural-people', NaturalPersonViewSet,
                basename='natural-people')
router.register('legal-people', LegalPersonViewSet, basename='legal-people')
router.register('emails', EmailViewSet)
router.register('phones', PhoneViewSet)
router.register('addresses', AddressViewSet)
router.register('accounts', AccountViewSet)
router.register('investments', InvestmentViewSet)
router.register('account-investments', AccountInvestmentViewSet)
router.register('loans', LoanViewSet)
router.register('installments', InstallmentViewSet)
router.register('cards', CardViewSet)
router.register('transactions', TransactionViewSet)


urlpatterns = []
