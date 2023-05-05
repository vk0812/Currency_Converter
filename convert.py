import click
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ['API_KEY']
URL = os.environ['URL']

@click.group()
def main():
    pass

@click.command()
def hello():
    click.echo("Hello! Welcome To Convert, world's first CLI Tool for Currency Conversion😁😁")

@click.command()
@click.option('-f','--from','from_',prompt='Currency to convert from',help='The Currency to convert From')
@click.option('-t','--to',prompt='Currency to convert to',help='The Currency to convert To')
@click.option('-a','--amount',default=1,help='The Amount to be converted',show_default=True,type=int)
def convert(from_,to,amount):
    options = {'api_key': API_KEY, 'from': from_, 'to': to, 'amount': amount}
    data = requests.get(url=URL,params=options)
    error_code = data.json()['error']
    if error_code == 0:
        result = data.json()['amount']
        click.echo(f'{amount} {from_} = {result:.2f} {to}')
    elif error_code == 210:
        click.echo('Invalid FROM Currency!')
    elif error_code == 260:
        click.echo('Invalid TO Currency!')
    elif error_code == 320:
        click.echo('Amount cannot be 0')

main.add_command(hello)
main.add_command(convert)

if __name__ == '__main__':
    main()
