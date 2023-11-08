from .imports.serializers import *


# ACCOUNT
# GET ACCOUNT INFO
class AccountGetSerializer(serializers.ModelSerializer):

    investments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    loans = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = [
            'id',
            'number',
            'agency',
            'acc_type',  # POUPANÇA / CORRENTE
            'credit_limit',
            'balance',
            'customer',
            'investments',
            'loans',
            'cards'
        ]


# CREATE AND UPDATE ACCOUNT
class AccountPostPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            'acc_type',
        ]


# NATURAL PERSON
# GET NATURAL PERSON INFO
class NaturalPersonGetSerializer(serializers.ModelSerializer):

    accounts = AccountGetSerializer(many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
        model = NaturalPerson
        fields = [
            'id',
            'cpf',
            'customer',
            'name',
            'birthdate',
            'rg',
            'social_name',
            'accounts'
        ]


# CREATE AND UPDATE NATURAL PERSON
class NaturalPersonPostPatchSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=30)

    class Meta:
        model = NaturalPerson
        fields = [
            'cpf',
            'password',
            'name',
            'birthdate',
            'rg',
            'social_name'
        ]


# LEGAL PERSON
# GET LEGAL PERSON INFO
class LegalPersonGetSerializer(serializers.ModelSerializer):

    accounts = AccountGetSerializer(many=True, read_only=True)

    class Meta:
        model = LegalPerson
        fields = [
            'id',
            'cnpj',
            'fantasy_name',
            'establishment_date',
            'im',
            'ie',
            'legal_nature',
            'accounts'
        ]


# CREATE AND UPDATE LEGAL PERSON
class LegalPersonPostPatchSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=30)

    class Meta:
        model = LegalPerson
        fields = [
            'cnpj',
            'password',
            'fantasy_name',
            'establishment_date',
            'im',
            'ie',
            'legal_nature'
        ]


# EMAIL
class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = [
            'id',
            'email',
            'customer'
        ]


# PHONE
class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = [
            'id',
            'phone',
            'country_code',
            'prefix_number',
            'customer'
        ]


# ADRESS
class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = [
            'id',
            'neighborhood',
            'street',
            'number',
            'city',
            'state',
            'cep',
            'customer'
        ]


# INVESTMENT
class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investment
        fields = [
            'id',
            'investment_type',
            'contribution',
            'admin_fee',
            'period',
            'risc_rate',
            'profitability'
        ]


class AccountInvestmentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInvestment
        fields = [
            'id',
            'id_account',
            'investment_type',
            'contribution',
            'income',
            'admin_fee',
            'period',
            'risc_rate',
            'profitability'
        ]


class AccountInvestmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInvestment
        fields = [
            'id_investment',
            'id_account'
        ]


# LOAN
class LoanGetSerializer(serializers.ModelSerializer):

    installments = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Loan
        fields = [
            'id',
            'id_account',
            'amount_request',
            'interest_rate',
            'is_payout',
            'installment_amount',
            'request_date',
            'approval_date',
            'observation',
            'installments'
        ]


class LoanPostPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = [
            'id_account',
            'amount_request',
            'interest_rate',
            'is_payout',
            'installment_amount',
            'observation'
        ]


# INSTALLMENT
class InstallmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Installment
        fields = [
            'id',
            'number',
            'payment_amount',
            'payment_date',
            'expiration_date',
            'is_paid'
        ]


# CARD
class CardGetSerializer(serializers.ModelSerializer):

    transactions = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Card
        fields = [
            'id',
            'number',
            'verification_code',
            'flag',
            'expiration_date',
            'is_active',
            'transactions'
        ]


class CardPostPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = [
            'id_account'
        ]


# TRANSACTION
class TransactionGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'id',
            'card',
            'id_receiver',
            'amount',
            'transaction_type',
            'timestamp'
        ]


class TransactionPostPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'id_card',
            'id_receiver',
            'amount',
            'transaction_type'
        ]


# BANKSTATEMENT
class BankStatementSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankStatement
        fields = []
