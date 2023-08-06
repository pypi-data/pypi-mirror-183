import typer
import schedule
import time as tm
import sqlite3
from datetime import time,timedelta,datetime
from atk_training_nitesh_psq import process

class action(process):
    @staticmethod
    def init_process(*item):
        for item_ in item:
            return item_.upper()


app=typer.Typer()

def job(db_path:str='queue.db'):
    print("running in a manager")
    with sqlite3.connect(db_path) as conn:

    # Create a cursor
            cursor = conn.cursor()

    # Select the first pending item from the queue
            cursor.execute('''
            SELECT * FROM Queue
                    WHERE status = 'pending'
                    ''')

    # Fetch the item
            item = cursor.fetchall()
    

            if item is not None:
        # Process the item
                for item_ in item:
                    status='completed'
                    #logger.info(item_)
                    try_num=item_[3]

                    try:
            
                        logger.info("Processing Item: ---->  " + action.init_process(item_[1]))
                        try_num+=1
                    except Exception as e:
                        logger.info('item cannot be processed',e)
                    if try_num>3:
                        status="manual check"


                    

        # Update the item's status to "completed"
                    cursor.execute('''
                        UPDATE Queue
                        SET status = ?,
                            retries = ?,
                            end_time= CURRENT_TIMESTAMP
                        WHERE id = ?
                        ''', (status,try_num,item_[0],))
        

        

        # Commit the changes
                    conn.commit()


schedule.every(5).minutes.do(job)
@app.command()
def manager():
    while True:
        schedule.run_pending()
        tm.sleep(10)
    

def main():
    app()