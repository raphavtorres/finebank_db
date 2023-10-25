# finebank_db
```cmd
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
py populate.py
```



## JWT
```txt
http://127.0.0.1:8000/api/v1/auth/jwt/create/
```
### POST
```json
{
  "register_number": 123,
  "password": "123"
}
```


#### Returns tokens
```txt
All methods require Authorization - "Bearer <jwt>"
```

```json
{
  "refresh": "...",
  "access": "..."
}
```


## LegalPerson
### POST
```json
{
  "cnpj": "",
  "password": "",
  "fantasy_name": "",
  "establishment_date": "0000-00-00",
  "im": "",
  "ie": "",
  "legal_nature": ""
}
```


## NaturalPerson
### POST
```json
{
  "cpf": "",
  "password": "",
  "name": "",
  "birthdate": "0000-00-00",
  "rg": "",
  "social_name": ""
}
```


## Email
### POST
```json
{
  "email": "name@example.com",
  "customer": "pk.customer"
}
```


## Phone
### POST
```json
{
  "phone": "00000000",
  "country_code": "55",
  "prefix_number": "000",
  "customer": "pk.customer"
}
```


## Address
### POST
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


## Account
### POST
```json
{
  "acc_type": "checking | savings",
  "balance": 0
}
```


## Investment
### POST
```json
{
  "investment_type": "Tesouro Direto",
  "contribution": 200.0,
  "admin_fee": 0.02,
  "period": "2026-01-01",
  "risc_rate": "Baixo",
  "profitability": 0.1
}
```


## AccountInvestment

### GET
```txt
http://127.0.0.1:8000/api/v1/account-investments/?account=1
```

### POST
```json
{
  "id_investment": 1,
  "id_account": 2
}
```


## Loan

### PATCH
```txt
"http://127.0.0.1:8000/api/v1/loans/<loan_id>/"
```

### POST
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


## Installment
### only GET
```txt
http://127.0.0.1:8000/api/v1/account-investments/?installment=1
```


## Card
## POST
```json
{
  "id_account": 1
}
```


## Transaction

```json
{
	"id_card": 2,
	"id_receiver": 1,
	"amount": 20,
	"transaction_type": "Credit"
}
```
