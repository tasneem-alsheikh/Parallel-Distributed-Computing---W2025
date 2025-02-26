# Brain Tumor Detection Using Parallel Processing

## Project Overview
This project implements a machine learning system for detecting brain tumors from MRI images. The implementation leverages parallel processing techniques to efficiently handle the computationally intensive tasks of image processing and model training.

## Dataset
The dataset consists of MRI brain scans categorized into two classes:
- **Positive Cases**: Images containing brain tumors (in the 'yes' directory)
- **Negative Cases**: Images without brain tumors (in the 'no' directory)

## Implementation Approach

### 1. Image Processing Pipeline
The system processes MRI images through the following steps:
- **Loading**: Images are read using OpenCV in grayscale format
- **Filtering**: Multiple filters are applied to enhance features:
  - Entropy Filter: Measures randomness, highlighting information-rich regions
  - Gaussian Filter: Smooths the image to reduce noise
  - Sobel Filter: Detects edges by highlighting gradients
  - Gabor Filter: Analyzes texture patterns
  - Hessian Filter: Enhances blob-like structures
  - Prewitt Filter: Edge detection with different kernel values

### 2. Parallel Processing Implementation
Two main components were parallelized:

#### Image Filtering
- Implemented multiprocessing with Python's `multiprocessing.Pool`
- Distributed filter application across multiple CPU cores
- Achieved a 38.9x speedup compared to sequential processing (242.7s → 6.2s)

#### Feature Extraction
- Parallelized GLCM (Gray Level Co-occurrence Matrix) feature extraction
- Used the `joblib` library for efficient parallel execution
- Reduced feature extraction time significantly (0.9s vs sequential)

### 3. Machine Learning Model
The system includes three different classifier models:
- **Random Forest**: Ensemble learning method
- **Support Vector Machine**: With linear kernel
- **Logistic Regression**: For binary classification

All models were trained and evaluated in parallel using Leave-One-Out cross-validation.

## Key Features
- **High Performance**: Leverages multicore processing for significant speedup
- **Feature Engineering**: Extracts GLCM texture features (contrast, homogeneity, energy, correlation, etc.)
- **Feature Selection**: Uses SelectKBest to identify most predictive features
- **Model Evaluation**: Employs Leave-One-Out cross-validation for robust performance assessment

## Results
- **Parallel Processing**: Achieved 38.9x speedup in image filtering
- **Classification Performance**: Models achieved high accuracy in tumor detection
- **Memory Efficiency**: Optimized resource usage for handling large datasets

## Dependencies
- Python 3.x
- OpenCV (`opencv-python`)
- scikit-image
- scikit-learn
- NumPy
- Pandas
- SciPy
- matplotlib
- seaborn
- joblib (for parallelization)

## Usage
1. Ensure all dependencies are installed:
   ```
   pip install opencv-python scikit-image matplotlib tqdm seaborn pandas scikit-learn joblib
   ```

2. Place your MRI images in the following structure:
   ```
   data/brain_tumor_dataset/
   ├── yes/  (tumor images)
   └── no/   (non-tumor images)
   ```

3. Run the main notebook to execute the entire pipeline:
   - Image loading
   - Parallel filtering
   - Feature extraction
   - Model training and evaluation

## Performance Considerations
- The optimal number of processes varies based on CPU cores available
- Memory usage increases with the number of processes
- For very large datasets, consider batch processing to avoid memory issues

## Future Improvements
- Implementation of GPU acceleration for image processing
- Hyperparameter optimization with parallel grid search
- Integration of deep learning models for end-to-end tumor detection