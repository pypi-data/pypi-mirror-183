import typer
from atk_training_nitesh_psq.sqlite_ import SQLITE
import time
import asyncio
from atk_training_nitesh_psq import read_yaml



app=typer.Typer()





    
    
@app.command()
def cons(config:str,db_name:str="queue.db"):
    d=read_yaml(config)
    d=d['process_func']
    # importing the module numpy
    main = __import__(d)
# importing an array from numpy
    process= getattr(main, "process")
    
    while True:
        queue=SQLITE()
        queue.process(process)
        time.sleep(10)
        # need to write asynchronous programming
        



     

def main():
    app()

if __name__=='__main__':
    main()
