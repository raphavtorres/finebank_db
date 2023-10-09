from .imports.views import *


class NaturalPersonViewSet(viewsets.ModelViewSet):
    queryset = NaturalPerson.objects.all()
    # serializer_class = NaturalPersonSerializer

    permission_classes = [CustomerGetPostPatch]

    def get_serializer_class(self):
        if self.request.method in "POST PATCH":
            return NaturalPersonPostPatchSerializer
        return NaturalPersonSerializer


class LegalPersonViewSet(viewsets.ModelViewSet):
    queryset = LegalPerson.objects.all()

    permission_classes = [CustomerGetPostPatch]

    def get_serializer_class(self):
        if self.request.method in "POST PATCH":
            return LegalPersonPostPatchSerializer
        return LegalPersonSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    permission_classes = [CustomerGetPostPatch]


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    permission_classes = [CustomerGetPostPatch]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    permission_classes = [CustomerGetPostPatch]


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    permission_classes = [CustomerGetPostPatch]


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    permission_classes = [CustomerGetPermission]


class AccountInvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = AccountInvestmentSerializer

    permission_classes = [CustomerGetPostPatch]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    permission_classes = [CustomerGetPostPatch]


class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer

    permission_classes = [CustomerGetPostPatch]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    permission_classes = [CustomerGetPostPatch]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    permission_classes = [CustomerGetPostPatch]
