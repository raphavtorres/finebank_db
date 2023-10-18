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

```json
Address
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