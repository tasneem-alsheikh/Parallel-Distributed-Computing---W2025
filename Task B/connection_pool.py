from multiprocessing import Semaphore

class ConnectionPool:
    def __init__(self, max_connections):
        """Initialize the connection pool with a semaphore."""
        self.max_connections = max_connections
        self.semaphore = Semaphore(max_connections)  # Semaphore to limit access
        self.connections = [f"Connection-{i}" for i in range(max_connections)]  # Simulating connections

    def get_connection(self):
        """Acquire a connection from the pool using the semaphore."""
        self.semaphore.acquire()  # Wait until a connection is available
        connection = self.connections.pop()  # Get the next available connection
        print(f"Acquired {connection}")
        return connection

    def release_connection(self, connection):
        """Release a connection back to the pool."""
        self.connections.append(connection)  # Add the connection back to the pool
        print(f"Released {connection}")
        self.semaphore.release()  # Release the semaphore, allowing another process to acquire a connection
