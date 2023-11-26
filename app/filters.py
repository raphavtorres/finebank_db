from django.shortcuts import get_object_or_404
from app.models import Account, Loan, Installment, Card


def filter_by_customer(model, customer):
    """
    Returns the queryset with info about the customer
    Or returns all if superuser
    """
    queryset = model.objects.all()

    if customer.is_authenticated and not customer.is_superuser:
        queryset = queryset.filter(register_number=customer.pk)
    return queryset


def filter_by_user(model, customer):
    """
    Returns the queryset with info about the user
    Or returns all if superuser
    """
    queryset = model.objects.all()

    if customer.is_authenticated and not customer.is_superuser:
        queryset = queryset.filter(customer=customer.pk)
    return queryset


def filter_by_account(obj, model):
    """
    Returns the queryset filtered by the account
    """
    queryset = []

    customer = obj.request.user
    account = obj.request.query_params.get('account')

    if account:
        account_instance = get_object_or_404(Account, pk=account)

        if (customer.is_authenticated and customer.is_superuser) or (customer in account_instance.customer.all()):
            queryset = model.objects.all()
            queryset = queryset.filter(account=account)

    return queryset


def filter_by_loan(obj):
    """
    Returns the queryset filtered by the loan
    """
    queryset = []

    customer = obj.request.user
    loan = obj.request.query_params.get('loan')

    if loan:
        loan_instance = get_object_or_404(Loan, pk=loan)

        if (customer.is_authenticated and customer.is_superuser) or (customer in loan_instance.account.customer.all()):
            queryset = Installment.objects.all()
            queryset = queryset.filter(loan=loan_instance)

    return queryset


def filter_by_card(obj):
    """
    Returns the queryset filtered by the account
    """
    queryset = []

    customer = obj.request.user
    card = obj.request.query_params.get('card')

    if card:
        card_instance = get_object_or_404(Card, pk=card)

        if (customer.is_authenticated and customer.is_superuser) or (customer in card_instance.account.customer.all()):
            queryset = Card.objects.all()
            queryset = queryset.filter(card=card_instance)

    return queryset
