from .imports.admin import *


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    add_form = CustomerCreateForm
    form = CustomerChangeForm
    model = Customer
    list_display = ('register_number', 'username', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal Information', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')})
    )


@admin.register(NaturalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'name',
        'birthdate',
        'cpf',
        'rg',
        'social_name'
    ]

    ordering = ['id']
    # list_filter = ['']


@admin.register(LegalPerson)
class LegalPersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer',
                    'fantasy_name', 'establishment_date',
                    'cnpj', 'legal_nature',
                    'im', 'ie']
    ordering = ['id']


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'customer']
    ordering = ['id']


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'phone', 'country_code', 'prefix_number']
    ordering = ['id']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'neighborhood',
                    'street', 'number', 'city', 'state', 'cep']
    ordering = ['id']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'agency',
                    'acc_type', 'credit_limit', 'balance', 'is_active']
    ordering = ['id']


@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'investment_type', 'contribution',
                    'admin_fee', 'period', 'risc_rate', 'profitability']
    ordering = ['id']


@admin.register(AccountInvestment)
class AccountInvestmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_account', 'investment_type', 'contribution',
                    'income', 'admin_fee', 'period', 'risc_rate', 'profitability']
    ordering = ['id']


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_account', 'amount_request', 'interest_rate', 'is_payout',
                    'installment_amount', 'request_date', 'approval_date', 'is_approved', 'observation']
    ordering = ['id']


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'loan', 'number',
                    'payment_amount', 'payment_date', 'expiration_date', 'is_paid']
    ordering = ['id']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'number',
                    'verification_code', 'flag', 'expiration_date', 'is_active']
    ordering = ['id']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'card', 'amount',
                    'receiver_acc_number', 'transaction_type', 'timestamp']
    ordering = ['id']


@admin.register(BankStatement)
class BankStatementAdmin(admin.ModelAdmin):
    list_display = ['id', 'account', 'transaction_action',
                    'source', 'amount', 'account_balance']
    ordering = ['id']
