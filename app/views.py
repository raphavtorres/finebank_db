from .imports.views import *


# NATURAL PERSON
# GET
class NaturalPersonGetViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = NaturalPerson.objects.all()
    serializer_class = NaturalPersonGetSerializer
    # permission_classes = [CustomerGetPostPatch]


# POST
class NaturalPersonPostViewSet(viewsets.GenericViewSet):
    serializer_class = NaturalPersonPostPatchSerializer
    # permission_classes = [CustomerGetPostPatch]

    def create(self, request):
        cpf = request.data.get('cpf')
        password = request.data.get('password')
        name = request.data.get('name')
        birthdate = request.data.get('birthdate')
        rg = request.data.get('rg')
        social_name = request.data.get('social_name')

        customer = get_user_model().objects.create(
            register_number=int(cpf),
            username=str(cpf),
            password=password,
            picture='picture_path'
        )

        customer_obj = get_object_or_404(get_user_model(), pk=customer.pk)

        natural_person = NaturalPerson.objects.create(
            customer=customer_obj,
            name=name,
            birthdate=birthdate,
            cpf=str(cpf),
            rg=rg,
            social_name=social_name
        )

        return Response({'status': 'Natural Person Succesfully created'}, status=status.HTTP_201_CREATED)


# LEGAL PERSON
class LegalPersonViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    # permission_classes = []

    # testing request HTTP method
    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return LegalPersonPostPatchSerializer
        elif self.request.method in 'GET':
            return LegalPersonGetSerializer

    def create(self, request):
        cnpj = request.data.get('cnpj')
        password = request.data.get('password')
        fantasy_name = request.data.get('fantasy_name')
        legal_nature = request.data.get('legal_nature')
        establishment_date = request.data.get('establishment_date')
        im = request.data.get('im')
        ie = request.data.get('ie')

        # creating user
        customer = get_user_model().objects.create(
            register_number=int(cnpj),
            username=str(cnpj),
            password=password,
            picture='picture2'
        )

        # creating user type legalperson
        legal_person = LegalPerson.objects.create(
            customer=customer,
            cnpj=str(cnpj),
            fantasy_name=fantasy_name,
            legal_nature=legal_nature,
            establishment_date=establishment_date,
            im=im,
            ie=ie
        )

        return Response({'status': 'Legal Person Succesfully created'}, status=status.HTTP_201_CREATED)


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
