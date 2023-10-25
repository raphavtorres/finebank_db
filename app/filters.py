def user_info_filter(model, user):
    """
    Returns the queryset with info about the user
    Or returns all if superuser
    """
    queryset = model.objects.all()

    if user.is_authenticated and not user.is_superuser:
        queryset = queryset.filter(user=user.pk)
    return queryset


def account_info_filter(model, account):
    """
    Returns the queryset filtered by the account
    """
    queryset = model.objects.all()
    if account:
        queryset = queryset.filter(id_account=account)
    return queryset
