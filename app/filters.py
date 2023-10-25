from django.shortcuts import get_object_or_404
from app.models import Account


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
        queryset = model.objects.all()
        account_instance = get_object_or_404(Account, pk=account)

        if (customer.is_authenticated and customer.is_superuser) or (customer in account_instance.user.all()):
            queryset = queryset.filter(id_account=account)

    return queryset
