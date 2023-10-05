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
def create_jwt(edv, password):
    response = requests.post(jwt_create_url, json={
                             'edv': edv, 'password': password})
    return response.json()['access']


def create_header():
    access_token = create_jwt(92902044, '123')
    headers = {'Authorization': f'Bearer {access_token}'}
    return headers


# TABLES POPULATION
def create_natural_person(headers, user):
    response = requests.post(natural_people_url, headers=headers,
                             json={
                                 'user': user
                             })
    return response.json()


def create_legal_person(headers, user):
    response = requests.post(legal_people_url, headers=headers,
                             json={
                                 'user': user
                             })
    return response.json()


def main():
    HEADERS = create_header()

    # NATURAL PERSON
    print(create_natural_person(HEADERS, ''))

    # LEGAL PERSON
    print(create_legal_person(HEADERS, ''))


if __name__ == '__main__':
    main()
