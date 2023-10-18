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
loans_url = os.path.join(BASE_URL, 'loans/')
installments_url = os.path.join(BASE_URL, 'installments/')
cards_url = os.path.join(BASE_URL, 'cards/')
transactions_url = os.path.join(BASE_URL, 'transactions/')
jwt_create_url = os.path.join(BASE_URL, 'auth/jwt/create/')


# AUTH
# def create_jwt(register_number, password):
#     response = requests.post(jwt_create_url, json={
#                              'register_number': register_number, 'password': password})
#     return response.json()['access']


# def create_header():
#     access_token = create_jwt(50050376837, '123')
#     headers = {'Authorization': f'Bearer {access_token}'}
#     return headers


# TABLES POPULATION
def create_natural_person(cpf, password, name, birthdate, rg, social_name):
    response = requests.post(natural_people_url,
                             json={
                                "cpf" : cpf,
                                "password" : password,
                                "name" : name,
                                "birthdate" : birthdate,
                                "rg" : rg,
                                "social_name": social_name
                            })
    return response.json()


def create_legal_person(cnpj, password, fantasy_name, establishment_date, im, ie, legal_nature):
    response = requests.post(legal_people_url,
                             json={
                                "cnpj" : cnpj,
                                "password" : password,
                                "fantasy_name" : fantasy_name,
                                "establishment_date" : establishment_date,
                                "im" : im,
                                "ie" : ie,
                                "legal_nature": legal_nature
                            })
    return response.json()


def main():
    # HEADERS = create_header()

    # CREATE NATURAL PERSON
    print(create_natural_person('92154845070', 'test@test', 'Person1', '2004-03-15', '380959021', social_name=''))
    print(create_natural_person('96731438030', 'test@test', 'Person2', '2003-12-02', '147879619', social_name=''))
    print(create_natural_person('48090331041', 'test@test', 'Person3', '1980-12-04', '306126618', social_name=''))

    # CREATE LEGAL PERSON
    print(create_legal_person('72305148000145', 'test@test', 'Company1', '2000-12-10', im='33333', ie='925113970461', legal_nature='Comp1Name'))
    print(create_legal_person('03673451000188', 'test@test', 'Company2', '2003-12-02', im='22222', ie='024719352149', legal_nature='Comp2Name'))
    print(create_legal_person('18716263000167', 'test@test', 'Company3', '1980-12-04', im='11111', ie='451925422835', legal_nature='Comp3Name'))


if __name__ == '__main__':
    main()
