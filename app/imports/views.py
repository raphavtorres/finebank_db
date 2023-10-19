from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

import random
from datetime import datetime, timedelta


from app.models import (
    NaturalPerson,
    LegalPerson,
    Email,
    Phone,
    Address,
    Account,
    Investment,
    AccountInvestment,
    Loan,
    Installment,
    Card,
    Transaction,
)

from app.serializers import (
    NaturalPersonGetSerializer,
    NaturalPersonPostPatchSerializer,

    LegalPersonGetSerializer,
    LegalPersonPostPatchSerializer,

    EmailSerializer,
    PhoneSerializer,
    AddressSerializer,

    AccountGetSerializer,
    AccountPostPatchSerializer,

    InvestmentSerializer,

    AccountInvestmentPostPatchSerializer,
    AccountInvestmentGetSerializer,

    LoanSerializer,
    InstallmentSerializer,
    CardSerializer,
    TransactionSerializer,
)

from app.permissions import (
    CustomerGetPostPatch,
    CustomerGetPermission,
    # SuperUserPermission,
    # CustomerPostPermission,
    # DeletePermission,
)
