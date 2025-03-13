import random
import time
from connection_pool import ConnectionPool  # Correct import

def access_database(connection_pool):
    """Simulate a process performing a database operation."""
    process_id = random.randint(1, 100)
    print(f"Process {process_id} waiting for a connection...")
    connection = connection_pool.get_connection()  # Acquire a connection

    print(f"Process {process_id} working with {connection}...")
    time.sleep(random.uniform(1, 3))  # Simulating work by sleeping for a random duration

    connection_pool.release_connection(connection)  # Release the connection back to the pool
    print(f"Process {process_id} finished with {connection}")
