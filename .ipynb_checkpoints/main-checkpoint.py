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
