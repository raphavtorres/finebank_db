import requests
import os


BASE_URL = 'http://127.0.0.1:8000/api/v1/'

natural_people_url = os.path.join(BASE_URL, 'natural-people/')
legal_people_url = os.path.join(BASE_URL, 'legal-people/')
emails_url = os.path.join(BASE_URL, 'emails/')
phones_url = os.path.join(BASE_URL, 'phones/')
addresses_url = os.path.join(BASE_URL, 'addresses/')
accounts_url = os.path.join(BASE_URL, 'accounts/')
investments_url = os.path.join(BASE_URL, 'investments/')
account_investments_url = os.path.join(BASE_URL, 'account-investments/')
loans_url = os.path.join(BASE_URL, 'loans/')
installments_url = os.path.join(BASE_URL, 'installments/')
cards_url = os.path.join(BASE_URL, 'cards/')
transactions_url = os.path.join(BASE_URL, 'transactions/')
jwt_create_url = os.path.join(BASE_URL, 'auth/jwt/create/')


# AUTH
def create_jwt(register_number, password):
    response = requests.post(jwt_create_url, json={
                             'register_number': register_number, 'password': password})
    return response.json()['access']


def create_header(register_number, password):
    access_token = create_jwt(register_number, password)
    headers = {'Authorization': f'Bearer {access_token}'}
    return headers


# TABLES POPULATION
def create_natural_person(cpf, password, name, birthdate, rg, social_name):
    response = requests.post(natural_people_url,
                             json={
                                 "cpf": cpf,
                                 "password": password,
                                 "name": name,
                                 "birthdate": birthdate,
                                 "rg": rg,
                                 "social_name": social_name
                             })
    print(response.json())
    return response.json()


def create_legal_person(cnpj, password, fantasy_name, establishment_date, im, ie, legal_nature):
    response = requests.post(legal_people_url,
                             json={
                                 "cnpj": cnpj,
                                 "password": password,
                                 "fantasy_name": fantasy_name,
                                 "establishment_date": establishment_date,
                                 "im": im,
                                 "ie": ie,
                                 "legal_nature": legal_nature
                             })
    print(response.json())
    return response.json()


def create_email(headers, email, customer):
    response = requests.post(emails_url, headers=headers,
                             json={
                                 "email": email,
                                 "customer": customer
                             })
    print(response.json())
    return response.json()


def create_phone(headers, phone, country_code, prefix_number, customer):
    response = requests.post(phones_url, headers=headers,
                             json={
                                 "phone": phone,
                                 "country_code": country_code,
                                 "prefix_number": prefix_number,
                                 "customer": customer
                             })
    print(response.json())
    return response.json()


def create_address(headers, neighborhood, street, number, city, state, cep, customer):
    response = requests.post(addresses_url, headers=headers,
                             json={
                                 "neighborhood": neighborhood,
                                 "street": street,
                                 "number": number,
                                 "city": city,
                                 "state": state,
                                 "cep": cep,
                                 "customer": customer
                             })
    print(response.json())
    return response.json()


def create_account(headers, acc_type):
    response = requests.post(accounts_url, headers=headers,
                             json={
                                 "acc_type": acc_type
                             })
    print(response.json())
    return response.json()


def create_investment(headers, investment_type, contribution, admin_fee, period, risc_rate, profitability):
    response = requests.post(investments_url, headers=headers,
                             json={
                                 "investment_type": investment_type,
                                 "contribution": contribution,
                                 "admin_fee": admin_fee,
                                 "period": period,
                                 "risc_rate": risc_rate,
                                 "profitability": profitability
                             })
    print(response.json())
    return response.json()


def create_account_investment(headers, id_investment, id_account):
    response = requests.post(account_investments_url, headers=headers,
                             json={
                                 "id_investment": id_investment,
                                 "id_account": id_account
                             })
    print(response.json())
    return response.json()


def create_loan(headers, account, amount_request, interest_rate, is_payout, installment_amount, observation):
    response = requests.post(loans_url, headers=headers,
                             json={
                                 "account": account,
                                 "amount_request": amount_request,
                                 "interest_rate": interest_rate,
                                 "is_payout": is_payout,
                                 "installment_amount": installment_amount,
                                 "observation": observation
                             })
    print(response.json())
    return response.json()


def create_card(headers, account):
    response = requests.post(cards_url, headers=headers,
                             json={
                                 "account": account
                             })
    print(response.json())
    return response.json()


def create_transaction(headers, card, receiver_acc_number, amount, transaction_type):
    response = requests.post(transactions_url, headers=headers,
                             json={
                                 "card": card,
                                 "receiver_acc_number": receiver_acc_number,
                                 "amount": amount,
                                 "transaction_type": transaction_type
                             })
    print(response.json())
    return response.json()


def main():
    # CREATE NATURAL PERSON
    create_natural_person("92154845070", "test@test",
                          "Person1", "2004-03-15", "380959021", social_name="")
    create_natural_person("96731438030", "test@test",
                          "Person2", "2003-12-02", "147879619", social_name="")
    create_natural_person("48090331041", "test@test",
                          "Person3", "1980-12-04", "306126618", social_name="")

    # CREATE LEGAL PERSON
    create_legal_person("72305148000145", "test@test", "Company1",
                        "2000-12-10", im="33333", ie="925113970461", legal_nature="Comp1Name")
    create_legal_person("03673451000188", "test@test", "Company2",
                        "2003-12-02", im="22222", ie="024719352149", legal_nature="Comp2Name")
    create_legal_person("18716263000167", "test@test", "Company3",
                        "1980-12-04", im="11111", ie="451925422835", legal_nature="Comp3Name")

    # CREATING HEADER
    super_user_header = create_header(123, "123")
    header_natural_1 = create_header(92154845070, "test@test")
    header_natural_2 = create_header(96731438030, "test@test")
    header_legal = create_header(72305148000145, "test@test")

    # CREATE EMAIL
    create_email(header_natural_1, "person1@gmail.com", "92154845070")
    create_email(header_natural_2, "person1second@gmail.com", "92154845070")
    create_email(header_legal, "company1@gmail.com", "72305148000145")

    # CREATE PHONE
    create_phone(header_natural_1, "31212867", country_code="55",
                 prefix_number="81", customer="92154845070")
    create_phone(header_natural_2, "23766213", country_code="55",
                 prefix_number="63", customer="92154845070")
    create_phone(header_legal, "38203406", country_code="55",
                 prefix_number="84", customer="72305148000145")

    # CREATE ADDRESS
    create_address(header_natural_1, "Planalto", "Treze", "769",
                   "Maceió", "Alagoas", "69121410", "92154845070")
    create_address(header_natural_2, "Centro", "Duque de Caxias", "28",
                   "Teófilo Otoni", "Minas Gerais", "09769184", "03673451000188")
    create_address(header_legal, "São José", "Bahia", "4225",
                   "Bacabal", "Maranhão", "69387595", "48090331041")

    # CREATE ACCOUNT - need user authenticated to make relation
    account1 = create_account(header_legal, "checking")
    account2 = create_account(header_natural_1, "savings")

    # CREATE INVESTMENT
    create_investment(super_user_header, "Tesouro Direto", 350.00, admin_fee=0.01,
                      period="2026-01-01", risc_rate="Baixo", profitability=0.10)
    create_investment(super_user_header, "CDB", 200.00, admin_fee=0.02,
                      period="2027-01-01", risc_rate="Médio", profitability=0.11)
    create_investment(super_user_header, "LCI", 540.00, admin_fee=0.012,
                      period="2028-01-01", risc_rate="Alto", profitability=0.12)

    # CREATE ACCOUNT INVESTMENT
    create_account_investment(
        header_natural_1, id_investment=1, id_account=2)
    create_account_investment(
        header_natural_1, id_investment=3, id_account=2)

    # CREATE LOAN
    create_loan(header_natural_1, 1, 700, interest_rate=0.05,
                is_payout=False, installment_amount=3, observation="comprar um celular")
    create_loan(header_legal, 2, 2000, interest_rate=0.03,
                is_payout=False, installment_amount=2, observation="contratar funcionário")

    # CREATE CARD
    create_card(header_natural_1, account=1)
    create_card(header_natural_1, account=2)
    create_card(header_legal, account=2)

    # CREATE TRANSACTION
    create_transaction(header_natural_1, card=2, receiver_acc_number=account1['number'],
                       amount=30, transaction_type="Credit")
    create_transaction(header_natural_1, card=2, receiver_acc_number=account1['number'],
                       amount=2000, transaction_type="Debit")


if __name__ == '__main__':
    main()
