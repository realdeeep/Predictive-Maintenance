# Predictive-Maintenance
Prediction of fault type and severity in mechanical bearings based on sensor data.

### What the project is about
We have matlab files which contain accelerometer data from drive end, fan end and ball bearings, and the y lables include fault types and severity (total of 9 types). From this files we analyze the data, do feature engineering and then train the models using Naive Bayes and CNN.

### So, how exactly do we do predictive maintenance?
As mentioned before, there may be defects at 3 different locations and for 3 different levels of severity. So, combining them we get 9 types. These locations include: outer race, inner race and ball-bearings. And severity is basically the size of the defect in milimeters.
After we have trained our models, when we give time series matlab data as input, we'll get which type of defect at which severity level might be present. Suppose the model predicts that there might be defects in outer race then it will be easy to decide where to put more focus on the next preventive maintenance cycle.

### Data
Divided into 2 types: Fault data and Normal data
Fault data has further classification based upon the types explained above. Below is the legend for files' naming.
Nomenclature: B -> Bearing fault, IR -> Inner race fault, OR -> Outer race fault, severity levels: 7, 14, 21
So, for example, is the file name is B007.mat, it means it contains data from Drive end (DE), Fan end (FE), Ball (BA) sensors which corresponds to bearing fault of severity level 0.007''.
