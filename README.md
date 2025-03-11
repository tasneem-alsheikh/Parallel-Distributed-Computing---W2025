# Parallel and Distributed Computing - MPI with mpi4py

## 📌 Overview
This project demonstrates parallel computing using `mpi4py` to distribute tasks across multiple machines. It includes:
- **Square Computation Program**: Computes squares of numbers in parallel.
- **Virus Spread Simulation**: Models the spread of a virus across a population using MPI.

## 🛠️ Prerequisites
Ensure you have the following installed on **all machines**:
- Python 3.x  
- `mpi4py` package  
- MPI library (`mpich`)  

### Install dependencies:
```bash
pip install mpi4py numpy pandas
sudo apt install mpich  # or sudo yum install openmpi
```

## 🚀 Running the Programs

### 1. Square Computation (calculate_squares.py)

#### Step 1: Set Up Environment
- Install dependencies (see above).
- Set up passwordless SSH between machines:
```bash
ssh-keygen -t rsa
ssh-copy-id student@machine_ip
```
- There is a host file (machines.txt) listing all machine IPs:
```
10.102.0.159
10.102.0.173
```

#### Step 2: Copy Files to Machines
- Use SCP to copy the script to all machines:
```bash
scp calculate_squares.py machines.txt user@machine_ip:/home/user/
```

#### Step 3: Run the Program
- Execute with MPI:
```bash
mpiexec -np 4 --hostfile machines.txt python3 calculate_squares.py
```

### 2. Virus Spread Simulation (virus_simulation.py)

#### Step 1: Run the Simulation
```bash
mpiexec -np 4 --hostfile machines.txt python3 virus_simulation.py
```

#### Step 2: Modify Parameters
You can edit virus_simulation.py to test different values:
- Population Size
- Spread Chance
- Vaccination Rate
