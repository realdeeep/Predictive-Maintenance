# Predictive Maintenance for Mechanical Bearings

## Overview

This project focuses on predicting fault types and severity in mechanical bearings using sensor data. By leveraging MATLAB files containing accelerometer data from various bearings, we conduct a detailed analysis, perform feature engineering, and train models using Naive Bayes and Convolutional Neural Networks (CNN).

## Purpose

The primary goal is to enable predictive maintenance, identifying potential faults at three different locations (outer race, inner race, and ball bearings) and three severity levels. With a total of 9 possible fault types, the models assist in determining the nature and severity of defects based on sensor data. This predictive capability aids in optimizing maintenance efforts, allowing for targeted interventions where needed.

## How It Works

1. **Data Analysis:** MATLAB files include accelerometer data from drive end, fan end, and ball bearings.
2. **Feature Engineering:** Extract relevant features from the sensor data to enhance model performance.
3. **Model Training:** Utilize Naive Bayes and CNN to train predictive models on fault and normal data.
4. **Predictive Maintenance:** Input time series MATLAB data to receive predictions about potential defects and their severity levels.

## Data Classification

The data is categorized into two main types:
- **Fault Data:** Further classified based on fault types (bearing, inner race, outer race) and severity levels (7, 14, 21).
- **Normal Data:** Represents the baseline condition without faults.

### File Naming Convention

- **Fault Data:** Follows the nomenclature: `B` (Bearing fault), `IR` (Inner race fault), `OR` (Outer race fault), with severity levels denoted as 7, 14, 21.
  - Example: `B007.mat` corresponds to data from Drive End (DE), Fan End (FE), and Ball (BA) sensors, indicating a bearing fault with severity level 0.007''.

## Why Predictive Maintenance?

- **Efficient Resource Allocation:** Focus preventive maintenance efforts where defects are predicted, optimizing resource utilization.
- **Minimized Downtime:** Anticipate potential faults before they escalate, reducing unplanned downtime.
- **Cost Savings:** Targeted maintenance leads to cost savings by avoiding unnecessary interventions.

Feel free to explore the provided MATLAB files and engage with the predictive maintenance capabilities of this project. Your feedback and contributions are highly appreciated!
