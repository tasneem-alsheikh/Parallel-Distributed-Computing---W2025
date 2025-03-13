from multiprocessing import Process
from connection_pool import ConnectionPool
from database_operations import access_database

def main():
    # Create a connection pool with a maximum of 3 connections
    connection_pool = ConnectionPool(max_connections=3)

    # Create a list of processes to simulate database access (let's simulate 5 processes)
    processes = []
    for _ in range(5):
        process = Process(target=access_database, args=(connection_pool,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
