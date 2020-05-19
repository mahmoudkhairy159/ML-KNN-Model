# ML-KNN-Model
*Implement your own simple KNN classifier using R , (Don’t use any build in
functions)
* Use provided train and test file yeast_train.txt,yeast_test.txt
* Each record in dataset contain feature values are separated by commas, and the
last value on each line is the class label
* If there is a tie in the class predicted by the k -nearest neighbors, then
among the classes that have the same number of votes, the tie should
be broken in favor of the class comes first in the Train file.
* Use Euclidean distance to compute distances between instances.
* Report accuracy on testing data when k=1,2,3....9.
* As output, your programs should print the value of k used for the test
set on the first line, each output line should list the predicted class
label, and actual class label.
* Also output the number of correctly classified test instances, and the
total number of instances in the test set &Accuracy.
Example :
Machine Learning
CS456- 2019
k value : 3
Predicted class : POX Actual class : CYT.
.
.
.
.
.
Number of correctly classified instances : 238 Total number of instances : 445
Accuracy : 0.5348314606741573
