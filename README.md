# README: mpi4py for Parallel and Distributed Computing

## Overview
This lecture introduces mpi4py, a Python package that provides bindings to the Message Passing Interface (MPI) standard for parallel and distributed computing. It focuses on how mpi4py can be used to develop parallel applications and distribute computing tasks across multiple nodes. The MPI model enables efficient communication between processes, making it suitable for high-performance computing (HPC) environments.

## Key Concepts

### What is mpi4py?
- mpi4py is a Python library that allows Python programs to utilize the MPI standard, which is widely used for parallel computing in high-performance computing (HPC) environments.
- It enables efficient inter-process communication, allowing for the distribution of workloads across multiple nodes in a computing cluster.
- While primarily designed for parallel computing, mpi4py is also used in distributed computing for large-scale data processing and computation tasks.

### mpi4py for Distributed Computing
- mpi4py facilitates the distribution of workloads across multiple nodes for efficient execution of large-scale computations and data processing.
- It enables communication between processes, but in a tightly coupled manner, which is a feature of parallel computing rather than purely distributed systems.

### How it Works
- **Single Program, Multiple Data (SPMD)**: All processes run the same program but can perform different operations depending on their rank or process ID.
- **Communication**: MPI supports both synchronous and asynchronous communication patterns, including point-to-point and collective operations.
- **High-level Interface**: mpi4py provides a high-level interface for Python to communicate with the underlying MPI implementation for parallel computation.

## Example Code

```python
from mpi4py import MPI

# Get the communication world and rank of each process
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Process 0 sends data to process 1
if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)

# Process 1 receives data from process 0 and prints it
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print('On process 1, data received:', data)
```

## Major Components and Methods

### MPI.Request (Non-blocking Operations)
- MPI.Request is an object returned by non-blocking send and receive operations, such as isend() and irecv().
- It allows checking the status of non-blocking operations or waiting for their completion without halting the program.

Example:

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data_to_send = "Hello from Process 0"
    request = comm.isend(data_to_send, dest=1, tag=100)
    request.wait()  # Wait for the non-blocking send to complete
    print("Process 0 sent data")

elif rank == 1:
    request = comm.irecv(source=0, tag=100)
    data_received = request.wait()  # Wait for the non-blocking receive to complete
    status = request.Get_status()  # Get status of the message
    print("Process 1 received data:", data_received)
    print("Status of the received message:", status)
```

### MPI.Status
- MPI.Status provides details about a received message, such as the source, tag, and error status.
- It is used with wait() and Get_status() to inspect the message after a non-blocking operation has completed.

### Common Methods in mpi4py
- **comm.send(), comm.recv()**: For sending and receiving messages.
- **comm.bcast(), comm.scatter(), comm.gather()**: For collective communication among processes.
- **comm.barrier()**: Synchronization barrier to coordinate all processes in a program.

### irecv vs. recv
- **recv**: A blocking receive operation. The process waits until the message is received, which can lead to inefficiency if the process can do other work during that time.
- **irecv**: A non-blocking receive operation. The process immediately gets an MPI.Request object and can continue executing other code while the message is received. It later checks the status of the operation using wait().

## Summary
- mpi4py is a powerful library for implementing parallel and distributed computing in Python using the MPI standard.
- It provides high-level methods for efficient inter-process communication and synchronization in parallel applications.
- Key features include support for non-blocking operations, collective communication, and detailed message status inspection.
