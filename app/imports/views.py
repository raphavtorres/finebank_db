from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

import random
from datetime import datetime, timedelta
from decimal import Decimal


from app.models import (
    Customer,
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
    BankStatement,
)

from app.serializers import (
    CustomerSerializer,
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

    AccountInvestmentPostSerializer,
    AccountInvestmentGetSerializer,

    LoanGetSerializer,
    LoanPostPatchSerializer,

    InstallmentSerializer,

    CardGetSerializer,
    CardPostPatchSerializer,

    TransactionSerializer,

    BankStatementSerializer,
)

from app.permissions import (
    CustomerGetPermission,
    CustomerPostPermission,
    CustomerPatchPermission,
    CustomerGetPatchPermission,
    CustomerGetPostPermission,
    CustomerGetPostPatchPermission,
    SuperUserPermission,
    CustomerPostPermission,
    DeletePermission,
)

from app.filters import (
    filter_by_customer,
    filter_by_user,
    filter_by_account,
    filter_by_loan,
    filter_by_card
)
