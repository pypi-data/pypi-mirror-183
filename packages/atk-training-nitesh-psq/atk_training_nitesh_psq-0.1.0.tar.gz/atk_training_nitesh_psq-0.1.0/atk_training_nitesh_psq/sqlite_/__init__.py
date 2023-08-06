import sqlite3
import typer
from atk_training_nitesh_psq import logger
from atk_training_nitesh_psq import process

class action(process):
    @staticmethod
    def init_process(*item):
        for item_ in item:
            return item_.upper()



app=typer.Typer()



class SQLITE:
    def __init__(self,db_name:str='queue.db'):
        self.db=db_name
         #Connect to the database
        with sqlite3.connect(db_name) as conn:


# Create a cursor
            cursor = conn.cursor()

# Create the queue table
#Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            cursor.execute('''
                CREATE TABLE if not exists Queue (
                id INTEGER PRIMARY KEY,
                    item TEXT,
                    status TEXT,
                    retries INTEGER,
                    start_time DATETIME DEFAULT CURRENT_TIMESTAMP,
                    end_time DATETIME 

                            )
                        ''')
            conn.commit()
    def put(self,*items):
         with sqlite3.connect(self.db) as conn:

    # Create a cursor
            try:
                cursor = conn.cursor()
            except Exception as e:
                logger.info('Connection cannot be made to sqlitedb',e)

    # Insert the item into the queue
            for item in items:
                cursor.execute('''
                INSERT INTO queue (item, status,retries)
                VALUES (?, ?,?)
                ''', (item, 'pending',0))

    # Commit the changes
                conn.commit()
    def process(self):
        with sqlite3.connect(self.db) as conn:

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
                    if try_num>3:
                        status="manual check"
                    else:
                        status="pending"
                    

                    try:
            
                        logger.info("Processing Item: ---->  " + action.init_process(item_[1]))
                        try_num+=1
                        cursor.execute('''
                        UPDATE Queue
                        SET status = 'completed',
                            retries = ?,
                            end_time= CURRENT_TIMESTAMP
                        WHERE id = ?
                        ''', (try_num,item_[0],))
                    except Exception as e:
                        logger.info('item cannot be processed',e)
                        logger.info('it will added to queue for retry')
                        try_num+=1
                        cursor.execute('''
                        UPDATE Queue
                        SET status = ?,
                            retries = ?,
                            end_time= CURRENT_TIMESTAMP
                        WHERE id = ?
                        ''', (status,try_num,item_[0],))
                    


                    

        # Update the item's status to "completed"
                    
        

        

        # Commit the changes
                    conn.commit()

    def get_pending(self):
        pass



    # Close the connection


# Commit the changes
@app.command()
def init(db_name:str='queue.db'):
    slq=SQLITE(db_name)
    print

def init_():
    app()
