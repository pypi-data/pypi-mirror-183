import typer
from atk_training_nitesh_psq.sqlite_ import SQLITE
import time
import asyncio



app=typer.Typer()





    
    
@app.command()
def cons(db_name:str="queue.db"):
    
    while True:
        queue=SQLITE()
        queue.process()
        time.sleep(10)
        # need to write asynchronous programming
        



     

def main():
    app()

if __name__=='__main__':
    main()
