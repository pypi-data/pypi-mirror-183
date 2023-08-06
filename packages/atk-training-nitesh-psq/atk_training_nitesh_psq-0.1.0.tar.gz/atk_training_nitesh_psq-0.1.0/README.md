# a Very simple Persistant queue service using sqlite3

How to intialize the queue using  the package (to instialize the db)
```
pip install atk_training_nitesh_psq
from atk_training_nitesh_psq.sqlite_ import SQLITE
queue=SQLITE('db_name')

# if someone is directly jumping to producer queue is automaticallt initialized
```
How to run intialize the queue using command
```
queue --db-name db_name
```

How to initialize the producer using the package
```
---> Given one has installed the package
from atk_training_nitesh_psq.producer import producer_
producer_("queue.db")
```
How to initialize the producer using the command
```
producer "queue.db"
```

How to initialize the consumer using the package
```
from atk_training_nitesh_psq.consumer import cons

cons('queue.db')
```
How to initailize the consumer using the command
```
consumer "queue.db" or empty
(automatically initializes to queue.db)
```

```
Need to implement a manager schuduled to push pending tasks to queue back to procesing and a ops manager
```
