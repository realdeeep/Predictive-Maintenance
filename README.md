# Predictive-Maintenance
Prediction of fault type and severity in mechanical bearings based on sensor data.

## Overview
This project focuses on predicting fault types and severity in mechanical bearings using sensor data. By leveraging MATLAB files containing accelerometer data from various bearings, we conduct a detailed analysis, perform feature engineering, and train models using Naive Bayes and Convolutional Neural Networks (CNN).

## Purpose
The primary goal is to enable predictive maintenance, identifying potential faults at three different locations (outer race, inner race, and ball bearings) and three severity levels. With a total of 9 possible fault types, the models assist in determining the nature and severity of defects based on sensor data. This predictive capability aids in optimizing maintenance efforts, allowing for targeted interventions where needed.

## How It Works
<b>Data Analysis</b>: MATLAB files include accelerometer data from drive end, fan end, and ball bearings.
<b>Feature Engineering</b>: Extract relevant features from the sensor data to enhance model performance.
<b>Model Training</b>: Utilize Naive Bayes and CNN to train predictive models on fault and normal data.
<b>Predictive Maintenance</b>: Input time series MATLAB data to receive predictions about potential defects and their severity levels.

## Data Classification
The data is categorized into two main types:

<b>Fault Data</b>: Further classified based on fault types (bearing, inner race, outer race) and severity levels (7, 14, 21).
<b>Normal Data</b>: Represents the baseline condition without faults.

### File Naming Convention
<b>Fault Data</b>: Follows the nomenclature: B (Bearing fault), IR (Inner race fault), OR (Outer race fault), with severity levels denoted as 7, 14, 21.
Example: B007.mat corresponds to data from Drive End (DE), Fan End (FE), and Ball (BA) sensors, indicating a bearing fault with severity level 0.007''.

## Why Predictive Maintenance?
<b>Efficient Resource Allocation</b>: Focus preventive maintenance efforts where defects are predicted, optimizing resource utilization.
<b>Minimized Downtime</b>: Anticipate potential faults before they escalate, reducing unplanned downtime.
<b>Cost Savings</b>: Targeted maintenance leads to cost savings by avoiding unnecessary interventions.

Feel free to explore the provided MATLAB files and engage with the predictive maintenance capabilities of this project. Your feedback and contributions are highly appreciated!
