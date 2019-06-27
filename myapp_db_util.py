from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

import sys

IP = sys.argv[1][1:-1]

"""
cluster = Cluster(
    [{'127.0.0.1'}],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='US_EAST'),
    port=9042)
"""

cluster = Cluster([IP])

session = cluster.connect()

session.execute("""CREATE KEYSPACE IF NOT EXISTS myapp WITH replication = 
{'class':'SimpleStrategy','replication_factor':'1'};""")

session.set_keyspace('myapp')

session.execute("""
    CREATE TABLE IF NOT EXISTS myapp.emp(
        emp_id int PRIMARY KEY,
        emp_name text,
        emp_city text,
        emp_sal varint,
        emp_phone varint
   );
    """
)

rows = session.execute("""
            SELECT * FROM myapp.emp
        """
    )

print(rows)
