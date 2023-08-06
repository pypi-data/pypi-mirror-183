import typer
import schedule
import time as tm
import sqlite3
from datetime import time,timedelta,datetime
from atk_training_nitesh_psq import read_yaml
from atk_training_nitesh_psq.sqlite_ import SQLITE


app=typer.Typer()



def job(config:str,db_path:str='queue.db'):
    sql_=SQLITE()
    d=read_yaml(config)
    d=d['process_func']
    # importing the module numpy
    main = __import__(d)
# importing an array from numpy
    process= getattr(main, "process")
    print("running in a manager")
    sql_.process(process)
    


@app.command()
def manager(config:str):
    schedule.every(5).minutes.do(lambda: job(config))
    while True:
        schedule.run_pending()
        tm.sleep(20)
    

def main():
    app()