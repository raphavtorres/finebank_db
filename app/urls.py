from .imports.url import *


router = SimpleRouter()
# NATURAL PERSON
router.register(
  'natural-people', 
  NaturalPersonGetViewSet, 
  basename='natural-people'
)
router.register(
  'natural-people-create'
  , NaturalPersonPostViewSet, 
  basename='natural-people-create'
)

# LEGAL PERSON
router.register(
  'legal-people', 
  LegalPersonGetViewSet,
  basename='legal-people'
)
router.register(
  'legal-people-create', 
  LegalPersonPostViewSet,
  basename='legal-people-create'
)

router.register('emails', EmailViewSet)
router.register('phones', PhoneViewSet)
router.register('addresses', AddressViewSet)
router.register('accounts', AccountViewSet)
router.register('investments', InvestmentViewSet)
router.register('loans', LoanViewSet)
router.register('installments', InstallmentViewSet)
router.register('cards', CardViewSet)
router.register('transactions', TransactionViewSet)


urlpatterns = []
