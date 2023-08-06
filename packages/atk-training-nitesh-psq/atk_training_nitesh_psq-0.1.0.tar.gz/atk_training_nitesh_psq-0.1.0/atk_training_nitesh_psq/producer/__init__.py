import sqlite3
import typer
from atk_training_nitesh_psq.sqlite_ import SQLITE



app=typer.Typer()


def producer(item):
   queue=SQLITE()
   queue.put(item)


@app.command()
def producer_(queue:str='queue.db'):
    '''
    queue here is the db path which was first initialized 
    args: queue(db_path)
    for-example producer_('queue.db')
    '''
    while True:
        in_=input('Give items to be pushed to queue ---->  ')
        if in_=='exit':
            break
        producer(in_)

def main():
    app()
