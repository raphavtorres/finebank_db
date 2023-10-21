# finebank_db
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
py populate.py


# LegalPerson
```json
{
	"cnpj" : "",
	"password" : "",
	"fantasy_name" : "",
	"establishment_date" : "0000-00-00",
	"im" : "",
	"ie" : "",
	"legal_nature": ""
}
```

# NaturalPerson
```json
{
	"cpf" : "",
	"password" : "",
	"name" : "",
	"birthdate" : "0000-00-00",
	"rg" : "",
	"social_name": ""
}
```

# Email
```json
{
	"email": "name@example.com",
	"customer": "pk.customer"
}
```

# Phone
```json
{
	"phone": "00000000",
	"country_code": "55",
	"prefix_number": "000",
	"customer": "pk.customer"
}
```

# Address
```json
{
    "neighborhood": "",
    "street": "",
    "number": "",
    "city": "",
    "state": "",
    "cep": "",
    "customer": "pk.customer"
}
```

# Account
```json
{
	"acc_type": "checking | savings",
	"balance": 0
}
```

# Investment
```json
{
	"investment_type": "Tesouro Direto",
	"contribution": 200.00,
	"admin_fee": 0.02,
	"period": "2026-01-01",
	"risc_rate": "Baixo",
	"profitability": 0.10
}
```

# AccountInvestment
```json
{
	"id_investment": 1,
	"id_account": 2
}
```

# Loan
```json
{
	"id_account": 1,
	"amount_request": 200,
	"interest_rate": 0.05,
	"is_payout": false,
	"installment_amount": 1,
	"observation": ""
}
```

# Installment
Only Get

# Card

# Transaction