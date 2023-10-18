# finebank_db
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
py populate.py


LegalPerson json
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

NaturalPerson json
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