from . import cli
from . import bsc

def run():
    args = cli.init()

    print('Searching transactions...')
    contracts = bsc.get_contracts()
    tokens = bsc.get_token_info(contracts)
    print('Here are some of the most recent tokens transfered:\n')
    print(f"{'NAME' : <30}{'HOLDERS' : <10}{'EMPTY LOGO' : <12}{'CONTRACT'}")
    for token in tokens:
        empty_logo = token['logo'] == '/images/main/empty-token.png'
        print(f"{token['name'] : <30}{token['holders'] : <10}{'✓' if empty_logo else '𐄂' : <12}{token['contract']}")