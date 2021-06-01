import requests
from bs4 import BeautifulSoup

def get_contracts():
    '''Find unique token contracts from transactions list.'''
    page = requests.get('https://bscscan.com/tokentxns')
    soup = BeautifulSoup(page.text, 'html.parser')
    contracts = {
        row.select('td:nth-of-type(9)')[0].find('a')['href'].lstrip('/token/')
        for row in soup.find('tbody').find_all('tr')
    }
    return contracts

def get_token_info(contracts):
    '''Get token info from a list of contract addresses.'''
    tokens = []
    for contract in contracts:
        page = requests.get(f'https://bscscan.com/token/{contract}')
        soup = BeautifulSoup(page.text, 'html.parser')

        name = soup.find('h1').find(class_='text-secondary').text.strip()
        logo = soup.find('h1').find('img')['src']
        holders = soup.find(id='ContentPlaceHolder1_tr_tokenHolders').find(class_='mr-3').text
        holders = holders.replace('addresses', '').replace('\n', '').replace(',', '').replace(' ', '')

        tokens.append({
            'name': name,
            'contract': contract,
            'logo': logo,
            'holders': int(holders)
        })
    return tokens