from .imports.views import *


# NATURAL PERSON
class NaturalPersonViewSet(viewsets.ModelViewSet):
    permission_classes = []

    def get_queryset(self):
        return filter_by_user(NaturalPerson, self.request.user)

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

        try:
            # creating user
            customer = get_user_model().objects.create_user(
                register_number=int(cpf),
                password=password,
                picture='picture_path'
            )

            # creating user type naturalperson
            NaturalPerson.objects.create(
                customer=customer,
                name=name,
                birthdate=birthdate,
                cpf=str(cpf),
                rg=rg,
                social_name=social_name
            )

        except IntegrityError as e:
            return Response({'status': 'User with this CPF already registered'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'status': 'Natural Person Succesfully Created'}, status=status.HTTP_201_CREATED)


# LEGAL PERSON
class LegalPersonViewSet(viewsets.ModelViewSet):
    permission_classes = []

    def get_queryset(self):
        return filter_by_user(LegalPerson, self.request.user)

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

        try:
            # creating user
            customer = get_user_model().objects.create_user(
                register_number=int(cnpj),
                password=password,
                picture='picture_path'
            )

            # creating user type legalperson
            LegalPerson.objects.create(
                customer=customer,
                cnpj=str(cnpj),
                fantasy_name=fantasy_name,
                legal_nature=legal_nature,
                establishment_date=establishment_date,
                im=im,
                ie=ie
            )

        except IntegrityError as e:
            return Response({'status': 'User with this CNPJ already registered'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'status': 'Legal Person Succesfully Created'}, status=status.HTTP_201_CREATED)


class EmailViewSet(viewsets.ModelViewSet):
    serializer_class = EmailSerializer
    permission_classes = [CustomerGetPostPatchPermission]

    def get_queryset(self):
        return filter_by_user(Email, self.request.user)


class PhoneViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSerializer
    permission_classes = [CustomerGetPostPatchPermission]

    def get_queryset(self):
        return filter_by_user(Phone, self.request.user)


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [CustomerGetPostPatchPermission]

    def get_queryset(self):
        return filter_by_user(Address, self.request.user)


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomerGetPostPatchPermission]

    def get_queryset(self):
        return filter_by_user(Account, self.request.user)

    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return AccountPostPatchSerializer
        elif self.request.method in 'GET':
            return AccountGetSerializer

    def create(self, request):
        # account parameters
        acc_number = get_random_number(8)
        agency = '4242'
        acc_type = request.data.get('acc_type')  # POUPANÇA / CORRENTE
        credit_limit = random.choice([200, 400, 600, 800])
        balance = random.choice([500, 1000, 2000, 3000])
        customer = self.request.user.pk

        if acc_type not in [option[0] for option in Account.OPTIONS]:
            return Response({'status': "Invalid account type. Valid values: [checking, savings]"}, status=status.HTTP_403_FORBIDDEN)

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
            balance=balance,
            is_active=True
        )
        account.customer.add(customer)

        # creating card
        Card.objects.create(
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
    permission_classes = [CustomerGetPermission]
    serializer_class = InvestmentSerializer


class AccountInvestmentViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomerGetPostPermission]

    def get_queryset(self):
        return filter_by_account(self, AccountInvestment)

    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return AccountInvestmentPostSerializer
        elif self.request.method in 'GET':
            return AccountInvestmentGetSerializer

    def create(self, request):
        # getting investment in "Investment" table
        id_investment = request.data.get('id_investment')
        investment = get_object_or_404(Investment, pk=id_investment)

        # getting info for AccountInvestment based on the Investment received
        account = request.data.get('account')
        account_instance = get_object_or_404(Account, pk=account)

        if account_instance.balance >= investment.contribution:
            investment_type = investment.investment_type
            contribution = investment.contribution
            income = 0.00
            admin_fee = investment.admin_fee
            period = investment.period
            risc_rate = investment.risc_rate
            profitability = investment.profitability

            # adding to BankStatement table
            create_bankstatement(account_instance, 'Sent',
                                 'Investment', contribution)

            # creating AccountInvestment
            AccountInvestment.objects.create(
                account=account_instance,
                investment_type=investment_type,
                contribution=contribution,
                income=income,
                admin_fee=admin_fee,
                period=period,
                risc_rate=risc_rate,
                profitability=profitability
            )

            return Response({'status': 'Account Investment Succesfully Created'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Not enough balance to make the investment'}, status=status.HTTP_403_FORBIDDEN)


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    permission_classes = [CustomerGetPostPatchPermission]

    def get_queryset(self):
        return filter_by_account(self, Loan)

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

        account = request.data.get('account')
        account_instance = get_object_or_404(Account, pk=account)

        def create_loan(is_approved):
            loan = Loan.objects.create(
                account=account_instance,
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
        payment_amount = round((amount_request / installment_amount), 2)

        # Approved
        if payment_amount < account_instance.credit_limit * 4:
            # adding to BankStatement table
            create_bankstatement(
                account_instance, 'Received', 'Loan', amount_request)

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

    # Updates installments 'is_paid' and loan 'is_payout'
    def partial_update(self, request, *args, **kwargs):
        # getting information to installment
        loan = self.get_object()

        related_installments = Installment.objects.filter(loan=loan)
        account = loan.account

        amount = 0

        # iterating installments to find a non paid
        for installment_for in related_installments:
            if not installment_for.is_paid:
                amount = installment_for.payment_amount
                installment = installment_for
                break

        if amount == 0:
            return Response({'status': 'No installments left to pay, loan is payout'}, status=status.HTTP_201_CREATED)

        # testing if account has enough balance to pay
        if account.balance > amount:
            # saving payment in BankStatement
            create_bankstatement(account, 'Sent', 'Installment', amount)
            # updating installment fields
            installment.is_paid = True
            installment.payment_date = datetime.now()
            installment.save()

            # updating loan fields
            loan.paid_installment_amount += 1
            # testing if all loan installments are paid
            if loan.installment_amount == loan.paid_installment_amount:
                loan.is_payout = True
            loan.save()

            return Response({'status': 'Installment Succesfully Paid'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Not enough balance to pay the installment'}, status=status.HTTP_403_FORBIDDEN)


class InstallmentViewSet(viewsets.ModelViewSet):
    serializer_class = InstallmentSerializer
    permission_classes = [CustomerGetPermission]

    def get_queryset(self):
        return filter_by_loan(self)


class CardViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomerGetPostPermission]

    def get_queryset(self):
        return filter_by_card(self)

    def get_serializer_class(self):
        if self.request.method in 'POST PATCH':
            return CardPostPatchSerializer
        elif self.request.method in 'GET':
            return CardGetSerializer

    def create(self, request):
        # getting account
        account = request.data.get('account')
        account_instance = get_object_or_404(Account, pk=account)

        if account_instance.credit_limit > 500:
            # card parameters
            card_number = get_random_number(16)
            verification_code = get_random_number(3)
            flag = random.choice(["MasterCard", "Visa", "Elo"])
            expiration_date = datetime.now() + timedelta(days=365*5)

            # creating card
            Card.objects.create(
                account=account_instance,
                number=card_number,
                verification_code=verification_code,
                flag=flag,
                expiration_date=expiration_date,
                is_active=True
            )

            return Response({'status': 'Card Succesfully Created'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Not eligible to receive the card'}, status=status.HTTP_403_FORBIDDEN)


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomerPostPermission]

    serializer_class = TransactionSerializer

    def create(self, request):
        # getting receiver account
        id_receiver = request.data.get('id_receiver')
        receiver = get_object_or_404(Account, pk=id_receiver)

        # getting transaction info from serializer
        id_card = request.data.get('id_card')
        card = get_object_or_404(Card, pk=id_card)
        amount = request.data.get('amount')
        transaction_type = request.data.get('transaction_type')

        # getting account instance from card fk
        account = card.account

        # testing user balance to accept transaction
        if account.balance > amount:

            # creating transaction
            Transaction.objects.create(
                card=card,
                amount=amount,
                receiver_acc_number=receiver,
                transaction_type=transaction_type
            )

            # saving transaction in BankStatement to Sender
            create_bankstatement(account, 'Sent', 'Transaction', amount)
            # saving transaction in BankStatement to Receiver
            create_bankstatement(receiver, 'Received', 'Transaction', amount)

            return Response({'status': 'Transaction Succesfully Created'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Not enough balance to make the transaction'}, status=status.HTTP_403_FORBIDDEN)


class BankStatementViewSet(viewsets.ModelViewSet):
    serializer_class = BankStatementSerializer

    permission_classes = [CustomerGetPermission]

    def get_queryset(self):
        return filter_by_account(self, BankStatement)


# Functions
def create_bankstatement(account, action, source, amount):
    if action == 'Received':
        account.balance += amount
    elif action == 'Sent':
        account.balance -= amount

    account.save()

    BankStatement.objects.create(
        account=account,
        transaction_action=action,
        source=source,
        amount=amount,
        account_balance=account.balance
    )


def get_random_number(length):
    return ''.join(random.choice('0123456789') for _ in range(0, length))
