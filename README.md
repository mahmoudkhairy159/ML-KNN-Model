# KNN Classifier - Yeast Dataset

## Overview
This project implements a **K-Nearest Neighbors (KNN)** classifier from scratch in **R** to classify yeast data. The classifier does not use any built-in functions for KNN and computes distances between instances using **Euclidean distance**. The goal is to classify yeast instances based on their features and predict their classes using different values of `k` (from 1 to 9).

The provided dataset includes:
- `yeast_train.txt`: Training data.
- `yeast_test.txt`: Testing data.

Each record in the dataset contains feature values separated by commas, with the last value representing the **class label**.

## Dataset Description
- **Train and Test Files**: Each file contains yeast instances, where the features are separated by commas. The last value on each line is the class label.
- **Features**: A set of attributes that describe each yeast sample.
- **Class Label**: The predicted output class (e.g., CYT, POX).

## Problem Statement
- Implement a simple KNN classifier using **R**.
- Compute Euclidean distance between instances.
- Break ties in the predicted class in favor of the class that comes first in the training file.
- Report accuracy on the testing data for values of `k` from 1 to 9.

## Steps

### 1. KNN Algorithm
KNN is a non-parametric, instance-based learning algorithm that classifies new instances based on the majority class among their `k` nearest neighbors in the feature space.

**Key components:**
- **Distance Calculation**: Euclidean distance between two instances:
  \[
  d(x, y) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}
  \]
  where \(x\) and \(y\) are the feature vectors of two instances.

- **Vote Tiebreaking**: In case of a tie between classes, the tie is broken in favor of the class that appears first in the training data.

### 2. Input and Output

#### Input:
- **Train File**: `yeast_train.txt`, containing instances for training.
- **Test File**: `yeast_test.txt`, containing instances for testing.

#### Output:
For each value of `k` (from 1 to 9):
1. The value of `k` used for testing.
2. A line for each instance in the test file showing the **predicted class** and the **actual class**.
3. After all predictions:
   - The number of correctly classified test instances.
   - The total number of test instances.
   - The accuracy, computed as:
   \[
   \text{Accuracy} = \frac{\text{Correctly Classified Instances}}{\text{Total Instances}}
   \]

