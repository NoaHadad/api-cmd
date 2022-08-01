import click

from data_file import DataFile

@click.group()
def cli():
    pass

@cli.command('set-value')                                                                                                                                                                                                                    
@click.option('--key', required=True, type=str)                                                                                                                                                                                                
@click.option('--value', required=True, type=str)
@click.option('--file', required=True, type=str)                                                                                                                                                                                                                                             
def set_value(key, value, file):
    """set key-val"""
    DataFile(file).set(key, value)

@cli.command('get-value')
@click.option('--key', required=True, type=str)
@click.option('--file', required=True, type=str)                                                                                                                                                                                                                                             
def get_value(key, file):
    """get val"""
    click.echo(DataFile(file).get(key))

@cli.command('delete-value')
@click.option('--key', required=True, type=str)
@click.option('--file', required=True, type=str)                                                                                                                                                                                                                                             
def delete_value(key, file):
    """del key"""
    click.echo(DataFile(file).delete(key))

if __name__=='__main__':
    cli()