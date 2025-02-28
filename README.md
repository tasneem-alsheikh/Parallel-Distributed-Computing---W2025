# 🧠 Brain Tumor Detection Using Parallel Processing

## 📋 Assignment Overview
In this assignment, the task was to develop a machine learning model for detecting brain tumors from MRI images. The project leveraged parallel processing to efficiently handle the large dataset and speed up computation-intensive tasks involved in image processing and model training.

## 📊 Dataset
The dataset consists of MRI images classified into two categories:
- **yes**: Images that contain brain tumors.
- **no**: Images that do not contain brain tumors.

The goal was to preprocess these images using various filters and techniques, extract relevant features, and then train a machine learning model to accurately classify the images as having a tumor or not.

## ⚡ Parallel Processing
To optimize the performance of image processing and model training, parallel processing techniques were implemented using Python's multiprocessing module. This allowed for the parallelization of tasks such as image preprocessing, feature extraction, and model training.

## 🎯 Objectives
- Load the MRI images using OpenCV.
- Implement parallel processing to efficiently handle image processing and model training.
- Train a machine learning model for brain tumor classification.
- Evaluate the performance of the model on a test set.

## 📬 Submission
The submission included:
- A completed Jupyter Notebook with all the code for loading the data, preprocessing, parallel processing implementation, model training, and evaluation.

## 🔍 Part I: Guided Code (60%)

### 🔄 Sequential Processing
The initial part of the assignment involved understanding and implementing a sequential version of the brain tumor detection process. This included:

- **Data Loading**: Loading MRI images using OpenCV.
- **Preprocessing**: Applying various filters (e.g., Entropy, Gaussian, Sobel, Gabor, Hessian, Prewitt) to enhance image features.
- **Feature Extraction**: Extracting features using methods like GLCM (Gray Level Co-occurrence Matrix) and LBP (Local Binary Patterns).
- **Classification**: Training a machine learning model to classify images as having a tumor or not.

### 🚀 Parallel Processing Implementation
The sequential code was then refactored to utilize parallel processing. The key steps included:

- **Identifying Parallelizable Components**: The most time-consuming tasks, such as image filtering and feature extraction, were identified as candidates for parallelization.
- **Implementing Parallel Processing**: Python's multiprocessing module was used to parallelize the filtering and feature extraction tasks.
- **Measuring Performance**: The execution time of the parallelized code was compared with the sequential version to evaluate the speedup.

### 📈 Results
- **Sequential Execution Time (for only 5 images)**: 241.65 seconds.
- **Parallel Execution Time (for the entire dataset)**: 6.12 seconds.
- **Speedup**: The parallel execution was 38.9 times faster than the sequential version.
- **Efficiency**: The efficiency was approximately 9.7 per process when using 4 CPU cores.

### ⚖️ Trade-offs
- **Overhead**: Running multiple processes introduced some overhead, which could affect speedup if the task per image is too small.
- **Memory Usage**: More processes used more memory, which could be an issue with larger datasets.
- **Diminishing Returns**: Beyond a certain number of processes, the performance boost might not be as significant due to management overhead.

## 🧩 Part II: Half-Guided Programming (30%)

### 🧮 Feature Extraction for Machine Learning
In this part, the focus was on creating a machine learning dataset by extracting features from the preprocessed images. The features extracted were based on the Gray Level Co-occurrence Matrix (GLCM), which captures texture information from the images.

### 🔢 GLCM Features
The following GLCM features were computed for each image:
- Contrast
- Dissimilarity
- Homogeneity
- Energy
- Correlation
- ASM (Angular Second Moment)

These features were computed for four different angles (0°, 45°, 90°, 135°) to capture texture information in multiple directions.

### ⚡ Parallelization of Feature Extraction
The feature extraction process was parallelized using Python's multiprocessing module. The key steps included:

- **Identifying Parallelizable Components**: The computation of GLCM features for each image was identified as a parallelizable task.
- **Implementing Parallel Processing**: The multiprocessing.Pool was used to parallelize the feature extraction process.
- **Measuring Performance**: The execution time of the parallelized feature extraction was compared with the sequential version.

### 📊 Results
- **Parallel Execution Time**: 0.77 seconds.
- **Speedup**: The parallel execution was significantly faster than the sequential version.

## 🤖 Part III: Non-Guided Machine Learning Application (10%)

### 🏋️ Model Training and Validation
In the final part, the extracted features were used to train and validate machine learning models. The steps included:

- **Data Splitting**: The dataset was split into training (75%) and testing (25%) sets.
- **Model Selection**: Three machine learning models were chosen:
  - Random Forest Classifier
  - Support Vector Machine (SVM)
  - Logistic Regression
- **Model Training**: The models were trained on the training data.
- **Model Validation**: The models were evaluated on the test data using metrics such as accuracy, precision, recall, and F1-score.

### 📈 Results
- **Random Forest Accuracy**: 60.00%
- **SVM Accuracy**: 80.00%
- **Logistic Regression Accuracy**: 80.00%

## 🏁 Conclusion
The assignment successfully demonstrated the use of parallel processing to speed up image preprocessing and feature extraction tasks in a brain tumor detection pipeline. The parallelized implementation achieved a significant speedup, reducing the execution time from 241.65 seconds to 6.12 seconds. The machine learning models trained on the extracted features achieved reasonable accuracy, with SVM and Logistic Regression performing the best at 80% accuracy.

## 🔮 Future Work
- **Hyperparameter Tuning**: Further fine-tuning of the machine learning models could improve their performance.
- **Larger Dataset**: Testing the pipeline on a larger dataset to evaluate its scalability.
- **Advanced Models**: Exploring more advanced models such as Convolutional Neural Networks (CNNs) for image classification.

## 🚀 How to Run the Code

### 📦 Install Dependencies:
```bash
pip install opencv-python scikit-image matplotlib tqdm seaborn scikit-learn joblib
```

### 📓 Run the Jupyter Notebook:
- Open the provided Jupyter Notebook and run each cell sequentially.
- Ensure that the dataset is placed in the correct directory (`../data/brain_tumor_dataset/`).

### 📊 Evaluate Results:
- The notebook will output the execution times, speedup, and model accuracies.
- Visualizations of the filtered images and feature importance can also be viewed in the notebook.
