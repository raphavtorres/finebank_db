from rest_framework import serializers
# from django.db.models import Avg

from .models import (
    NaturalPerson,
    LegalPerson,
    Email,
    Phone,
    Address,
    Account,
    Investment,
    Loan,
    Installment,
    Card,
    Transaction,
)


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
            'is_active',
            'customers',
            'investments',
            'loans',
            'cards'
        ]


class NaturalPersonSerializer(serializers.ModelSerializer):

    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
        model = NaturalPerson
        fields = [
            'id',
            'customer',
            'name',
            'birthdate',
            # 'cpf',
            'rg',
            'social_name',
            'accounts'
        ]


class LegalPersonSerializer(serializers.ModelSerializer):

    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
        model = LegalPerson
        fields = [
            'id',
            'fantasy_name',
            'establishment_date',
            # 'cnpj',
            'im',
            'ie',
            'legal_nature',
            'accounts'
        ]


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        # extra_kwargs = {}
        model = Email
        fields = [
            'id',
            'email',
            'customer'
        ]


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        # extra_kwargs = {}
        model = Phone
        fields = [
            'id',
            'phone',
            'country_code',
            'prefix_number',
            'customer'
        ]


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        # extra_kwargs = {}
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


# ACCOUNT FICAVA AQUI


class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
        # extra_kwargs = {}
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


class LoanSerializer(serializers.ModelSerializer):

    installments = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
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


class InstallmentSerializer(serializers.ModelSerializer):

    class Meta:
        # extra_kwargs = {}
        model = Installment
        fields = (
            'id',
            'number',
            'payment_amount',
            'payment_date',
            'expiration_date'
        )


class CardSerializer(serializers.ModelSerializer):

    transactions = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        # extra_kwargs = {}
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


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        # extra_kwargs = {}
        model = Transaction
        fields = (
            'id',
            'amount',
            'transaction_type',
            'timestamp'
        )
