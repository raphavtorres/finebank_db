from .imports.serializers import *


# ACCOUNT
# GET
class AccountSerializer(serializers.ModelSerializer):

    investments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    loans = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
        model = Account
        fields = [
            'id',
            'number',
            'agency',
            'acc_type',
            'credit_limit',
            # 'is_active',
            'customers',
            'investments',
            'loans',
            'cards'
        ]


# POST AND PATCH
class AccountPostPatchSerializer(serializers.ModelSerializer):

    investments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    loans = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
        model = Account
        fields = [
            'id',
            'number',
            'agency',
            'acc_type',
            'credit_limit',
        ]


# NATURAL PERSON
# GET
class NaturalPersonSerializer(serializers.ModelSerializer):

    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
        model = NaturalPerson
        fields = [
            'id',
            'register_number',
            'customer',
            'name',
            'birthdate',
            # 'cpf',
            'rg',
            'social_name',
            'accounts'
        ]


# POST AND PATCH
class NaturalPersonPostPatchSerializer(serializers.ModelSerializer):

    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = NaturalPerson
        fields = [
            'register_number',
            'customer',
            'name',
            'birthdate',
            # 'cpf',
            'rg',
            'social_name',
        ]


# LEGAL PERSON
# GET
class LegalPersonSerializer(serializers.ModelSerializer):

    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = LegalPerson
        fields = [
            'id',
            'register_number',
            'fantasy_name',
            'establishment_date',
            # 'cnpj',
            'im',
            'ie',
            'legal_nature',
            'accounts'
        ]


# POST AND PATCH
class LegalPersonPostPatchSerializer(serializers.ModelSerializer):

    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = LegalPerson
        fields = [
            'register_number',
            'fantasy_name',
            'establishment_date',
            # 'cnpj',
            'im',
            'ie',
            'legal_nature',
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
            'state'
            'cep',
            'customer'
        ]


# INVESTMENT
class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investment
        fields = (
            'id',
            'investment_type',
            'contribution',
            'income',
            'admin_fee',
            'period'
            'risc_rate',
            'profitability'
        )


class AccountInvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInvestment
        fields = (
            'id',
            'investment_type',
            'contribution',
            'income',
            'admin_fee',
            'period'
            'risc_rate',
            'profitability'
        )


# LOAN
class LoanSerializer(serializers.ModelSerializer):

    installments = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Loan
        fields = (
            'id',
            'amount_request',
            'interest_rate',
            'is_payout',
            'installment_amount',
            'request_date'
            'approval_date',
            'observation'
        )


# INSTALLMENT
class InstallmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Installment
        fields = (
            'id',
            'number',
            'payment_amount',
            'payment_date',
            'expiration_date'
        )


# CARD
class CardSerializer(serializers.ModelSerializer):

    transactions = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Card
        fields = (
            'id',
            'number',
            'verification_code',
            'flag',
            'expiration_date',
            'is_active',
            'transactions'
        )


# TRANSACTION
class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = (
            'id',
            'amount',
            'transaction_type',
            'timestamp'
        )
