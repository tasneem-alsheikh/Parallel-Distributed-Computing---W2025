# Parallel and Distributed Computing - Lab 3: Data Parallel Model 🚀

## Overview
This repository contains the code and resources for **Lab 3** of the **DSAI 3202 – Parallel and Distributed Computing** course. In this lab, we build a parallel program to enhance the training of a machine learning model using the **Data Parallel Model**. The goal is to compare sequential, threaded, and multiprocessing implementations for optimizing the performance of a Random Forest model. 💡

---

## Objectives
- **Develop** a parallel program to speed up machine learning model training.
- **Learn** when to use threads and processes for effective parallelization.
- **Compare** performance metrics across different parallel implementations.

---

## Tasks
### 1. Data Preparation
- Download the dataset (`housing_prices_data.zip`) and the Jupyter notebook (`ModelingWithRandomForests.ipynb`).
- Transfer the files to the remote host machine using `scp`.
- Unzip the dataset and organize it into the appropriate directories.

### 2. Sequential Implementation
- Train a Random Forest model sequentially to find the best hyperparameters (`n_estimators`, `max_features`, `max_depth`).
- Measure the execution time and evaluate the model's performance using **RMSE** and **MAPE**.

### 3. Threading Implementation
- Parallelize the hyperparameter search using Python's `threading` module.
- Compare the execution time and performance metrics with the sequential implementation.

### 4. Multiprocessing Implementation
- Parallelize the hyperparameter search using Python's `multiprocessing` module.
- Compare the execution time and performance metrics with the sequential and threading implementations.

---

## Dataset 📊
The dataset used in this lab is from the **Housing Prices Competition**. It includes:
- **train.csv**: Training data with 79 explanatory variables describing residential homes in Ames, Iowa.
- **test.csv**: Test data for evaluating the model.

---

## Code Structure 🗂️
- **ModelingWithRandomForests.ipynb**: Jupyter notebook with code for data preparation, model training, and hyperparameter tuning.
- **data/housing_prices_data/**: Directory containing the dataset files.
- **notebooks/**: Directory for storing Jupyter notebooks.

---

## Results & Performance Metrics ⏱️
### Performance Comparison
| Method          | Execution Time (s) | RMSE       | MAPE       |
|-----------------|--------------------|------------|------------|
| Sequential      | 65.01              | 26057.94   | 9.83%      |
| Threading       | 25.61              | 26057.94   | 9.87%      |
| Multiprocessing | 13.21              | 26057.94   | 9.87%      |

### Key Findings
- **Execution Time:**  
  - Moving from **Sequential** (65.01s) to **Threaded** (25.61s) greatly reduces the time taken.  
  - **Multiprocessing** further decreases the time to **13.21s**—making it the fastest approach! 🚀
- **Performance Metrics:**  
  - The **RMSE** and **MAPE** values remain virtually identical across all implementations (RMSE ≈ 26057.94, MAPE ≈ 9.87%), which indicates that parallelization improves speed without sacrificing model accuracy.

---

## Questions ❓
1. **How does the execution time change when moving from sequential to threaded to multiprocessing implementations?**  
   **Answer:**  
   - **Sequential:** 65.01s  
   - **Threaded:** 25.61s  
   - **Multiprocessing:** 13.21s  
   The execution time decreases significantly, with multiprocessing providing the most dramatic improvement.

2. **Compute the performance metrics for the threaded and multiprocessing executions.**  
   **Answer:**  
   Both the **threaded** and **multiprocessing** implementations achieve:  
   - **RMSE:** 26057.94  
   - **MAPE:** 9.87%  
   This shows that while the speed improves with parallelization, the model's predictive performance remains consistent.

---

## How to Run the Code 🏃‍♂️
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/parallel-and-distributed-computing-dsai3202.git
   ```

2. **Navigate to the repository:**
   ```bash
   cd parallel-and-distributed-computing-dsai3202
   ```

3. **Transfer the dataset and notebook to the remote host machine:**
   ```bash
   scp housing_prices_data.zip student@10.102.10.XX:/home/student/
   scp ModelingWithRandomForests.ipynb student@10.102.10.XX:/home/student/
   ```

4. **Connect to the host machine and organize the files:**
   ```bash
   ssh student@10.102.10.XX
   mv housing_prices_data.zip parallel-and-distributed-computing-dsai3202/data/
   mv ModelingWithRandomForests.ipynb parallel-and-distributed-computing-dsai3202/notebooks/
   cd parallel-and-distributed-computing-dsai3202/data/
   unzip housing_prices_data.zip
   ```

5. **Open the Jupyter notebook and run the code:**
   ```bash
   jupyter notebook
   ```

---

## Dependencies 🛠️
- **Python:** 3.x
- **Libraries:**
  - pandas
  - scikit-learn
  - numpy
  - threading
  - multiprocessing

**Install the required libraries using:**
```bash
pip install pandas scikit-learn numpy
```
