def filtering_by_user(model, user):
    """
    Returns the queryset with info about the user
    Or returns all if superuser
    """
    queryset = model.objects.all()
        
    if user.is_authenticated and not user.is_superuser:
        return queryset.filter(user=user.pk)
    return queryset


# def filtering_by_account(model, account):
#     """
#     Filtering the queryset by a specific account

#     Args:
#         model (class): Models class to filter

#     Returns:
#         queryset: filtered by the account
#     """
#     queryset = model.objects.all()
#     if account:
#         queryset = queryset.filter(id_account=account)
#         return queryset
#     return []