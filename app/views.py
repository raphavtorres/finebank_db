from .imports.views import *


# NATURAL PERSON
class NaturalPersonViewSet(viewsets.ModelViewSet):
    queryset = NaturalPerson.objects.all()
    # permission_classes = [CustomerGetPostPatch]

    # testing request HTTP method
    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return NaturalPersonPostPatchSerializer
        elif self.request.method in 'GET':
            return NaturalPersonGetSerializer

    def create(self, request):
        cpf = request.data.get('cpf')
        password = request.data.get('password')
        name = request.data.get('name')
        birthdate = request.data.get('birthdate')
        rg = request.data.get('rg')
        social_name = request.data.get('social_name')

        # creating user
        customer = get_user_model().objects.create(
            register_number=int(cpf),
            username=str(cpf),
            password=password,
            picture='picture_path'
        )

        # creating user type naturalperson
        natural_person = NaturalPerson.objects.create(
            customer=customer,
            name=name,
            birthdate=birthdate,
            cpf=str(cpf),
            rg=rg,
            social_name=social_name
        )

        return Response({'status': 'Natural Person Succesfully Created'}, status=status.HTTP_201_CREATED)


# LEGAL PERSON
class LegalPersonViewSet(viewsets.ModelViewSet):
    queryset = LegalPerson.objects.all()
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
            picture='picture_path'
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

        return Response({'status': 'Legal Person Succesfully Created'}, status=status.HTTP_201_CREATED)


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    # permission_classes = [CustomerGetPostPatch]


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    # permission_classes = [CustomerGetPostPatch]


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    # permission_classes = [CustomerGetPostPatch]


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    # permission_classes = [CustomerGetPostPatch]

    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return AccountPostPatchSerializer
        elif self.request.method in 'GET':
            return AccountGetSerializer

    def create(self, request):
        # account parameters
        acc_number = get_random_number(8)
        agency = '4242'
        acc_type = request.data.get('acc_type')
        print(acc_type)  # POUPANÇA / CORRENTE
        credit_limit = 800.00
        customer = self.request.user.pk

        # card parameters
        card_number = get_random_number(16)
        verification_code = get_random_number(3)
        flag = random.choice(["MasterCard", "Visa", "Elo"])
        expiration_date = datetime.now() + timedelta(days=365*5)

        # creating account
        account = Account.objects.create(
            number=acc_number,
            agency=agency,
            acc_type=acc_type,
            credit_limit=credit_limit,
            is_active=True
        )
        account.customer.add(customer)

        # creating card
        card = Card.objects.create(
            account=account,
            number=card_number,
            verification_code=verification_code,
            flag=flag,
            expiration_date=expiration_date,
            is_active=True
        )

        return Response({'status': 'Account Succesfully Created'}, status=status.HTTP_201_CREATED)


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    # permission_classes = [CustomerGetPermission]
    serializer_class = InvestmentSerializer


class AccountInvestmentViewSet(viewsets.ModelViewSet):
    queryset = AccountInvestment.objects.all()
    # permission_classes = [CustomerGetPostPatch]

    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return AccountInvestmentPostPatchSerializer
        elif self.request.method in 'GET':
            return AccountInvestmentGetSerializer

    def create(self, request):
        # getting investment in "Investment" table
        id_investment = request.data.get('id_investment')
        investment = get_object_or_404(Investment, pk=id_investment)

        # getting info for AccountInvestment based on the Investment received
        id_account = request.data.get('id_account')
        id_account = get_object_or_404(Account, pk=id_account)

        investment_type = investment.investment_type
        contribution = investment.contribution
        income = 0.00
        admin_fee = investment.admin_fee
        period = investment.period
        risc_rate = investment.risc_rate
        profitability = investment.profitability

        # creating AccountInvestment
        AccountInvestment.objects.create(
            id_account=id_account,
            investment_type=investment_type,
            contribution=contribution,
            income=income,
            admin_fee=admin_fee,
            period=period,
            risc_rate=risc_rate,
            profitability=profitability
        )

        return Response({'status': 'Account Investment Succesfully Created'}, status=status.HTTP_201_CREATED)


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    # permission_classes = [CustomerGetPostPatch]

    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return LoanPostPatchSerializer
        elif self.request.method in 'GET':
            return LoanGetSerializer

    def create(self, request):
        # Getting loan information
        amount_request = request.data.get('amount_request')
        interest_rate = request.data.get('interest_rate')
        is_payout = request.data.get('is_payout')
        installment_amount = request.data.get('installment_amount')
        approval_date = datetime.now().strftime('%Y-%m-%d')
        observation = request.data.get('observation')

        id_account = request.data.get('id_account')
        account = get_object_or_404(Account, pk=id_account)

        def create_loan(is_approved):
            loan = Loan.objects.create(
                id_account=account,
                amount_request=amount_request,
                interest_rate=interest_rate,
                is_payout=is_payout,
                installment_amount=installment_amount,
                approval_date=approval_date,
                is_approved=is_approved,
                observation=observation
            )
            return loan

        # Getting installment information
        number = get_random_number(8)
        payment_amount = amount_request / installment_amount

        # margem consignável
        consignable_margin = account.balance * Decimal(0.40)
        # Approved
        if consignable_margin > payment_amount:
            loan = create_loan(True)

            # payment_date
            for i in range(installment_amount):
                expiration_date = datetime.now() + timedelta(30 * i)

                Installment.objects.create(
                    loan=loan,
                    number=number,
                    payment_amount=payment_amount,
                    expiration_date=expiration_date,
                    is_paid=False
                )

            return Response({'status': 'Loan Succesfully Created'}, status=status.HTTP_201_CREATED)

        # Rejected
        create_loan(False)
        return Response({'status': 'Not eligible to receive the loan'}, status=status.HTTP_403_FORBIDDEN)


class InstallmentViewSet(viewsets.ModelViewSet):
    queryset = Installment.objects.all()
    serializer_class = InstallmentPostGetSerializer

    permission_classes = [CustomerGetPermission]


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    permission_classes = [CustomerGetPostPatch]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    permission_classes = [CustomerGetPostPatch]


def get_random_number(length):
    return ''.join(random.choice('0123456789') for _ in range(0, length))
