from django.shortcuts import get_object_or_404
from app.models import Account


def user_info_filter(model, user):
    """
    Returns the queryset with info about the user
    Or returns all if superuser
    """
    queryset = model.objects.all()

    if user.is_authenticated and not user.is_superuser:
        queryset = queryset.filter(user=user.pk)
    return queryset


def account_info_filter(model, user, account):
    """
    Returns the queryset filtered by the account
    """
    queryset = model.objects.all()

    if account:
        account_instance = get_object_or_404(Account, pk=account)

        if (user.is_authenticated and user.is_superuser) or user in account_instance.user.all():
            queryset = queryset.filter(id_account=account)
    return queryset
