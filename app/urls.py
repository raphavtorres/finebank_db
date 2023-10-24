from .imports.url import *


router = SimpleRouter()

router.register('natural-people', NaturalPersonViewSet,
                basename='natural-people')
router.register('legal-people', LegalPersonViewSet, basename='legal-people')
router.register('emails', EmailViewSet, basename='emails')
router.register('phones', PhoneViewSet, basename='phones')
router.register('addresses', AddressViewSet, basename='addresses')
router.register('accounts', AccountViewSet, basename='accounts')
router.register('investments', InvestmentViewSet, basename='investments')
router.register('account-investments', AccountInvestmentViewSet,
                basename='account-investments')
router.register('loans', LoanViewSet, basename='loans')
router.register('installments', InstallmentViewSet, basename='installments')
router.register('cards', CardViewSet, basename='cards')
router.register('transactions', TransactionViewSet, basename='transactions')


urlpatterns = []
