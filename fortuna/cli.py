import argparse

def init():
    '''Get CLI arguments.'''
    parser = argparse.ArgumentParser(prog='fortuna', description='Pull token info from the transactions log on bscscan.com')
    return parser.parse_args()