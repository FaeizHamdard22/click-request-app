import click
import requests
import validators

@click.command()
def main():
    url=click.prompt("Enter your URL")
    if not validators.url(url) :
        click.echo("Invalid URL")
        return
    response = requests.get(url)
    click.echo(f"Status Code: {response.status_code}")
    if response.status_code==200 :
         click.echo("Request was successful!")
    else:
        click.echo("Request failed.")
    show_content = click.confirm("Do you want to see the respse content ?" , default=False)
    if show_content:
        click.echo(response.text)
        
if __name__ == '__main__':
     main()