from django.shortcuts import get_object_or_404
from app.models import Account, Loan


def user_info_filter(model, customer):
    """
    Returns the queryset with info about the user
    Or returns all if superuser
    """
    queryset = model.objects.all()

    if customer.is_authenticated and not customer.is_superuser:
        queryset = queryset.filter(customer=customer.pk)
    return queryset


def account_info_filter(model, account, customer):
    """
    Returns the queryset filtered by the account
    """
    queryset = []

    if account:
        account_instance = get_object_or_404(Account, pk=account)

        if (customer.is_authenticated and customer.is_superuser) or (customer in account_instance.customer.all()):
            queryset = model.objects.all()
            queryset = queryset.filter(account=account)

    return queryset


def loan_info_filter(model, loan, customer):
    """
    Returns the queryset filtered by the loan
    """
    queryset = []

    if loan:
        loan_instance = get_object_or_404(Loan, pk=loan)

        if (customer.is_authenticated and customer.is_superuser) or (customer in loan_instance.customer.all()):
            queryset = model.objects.all()
            queryset = queryset.filter(loan=loan)

    return queryset
