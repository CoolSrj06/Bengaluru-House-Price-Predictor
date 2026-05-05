# 🏠 Bangalore House Price Predictor

A simple machine learning web application that predicts house prices based on user inputs such as location, size, and number of rooms.

This project is part of my learning journey in machine learning and backend development, where I implemented a complete pipeline from data preprocessing to deployment.

---

## 🚀 Live Demo

👉 [https://bengaluru-house-price-predictor-nlbo.onrender.com](https://bengaluru-house-price-predictor-nlbo.onrender.com)

---

## 🧠 Model Overview

- **Algorithm:** Linear Regression
    
- **R² Score:** 0.83
    
- The model explains ~83% of the variance in housing prices
    

The model takes structured inputs (location, sqft, BHK, bathrooms), processes them, and returns a predicted price.

---

## 📊 Model Insights

### 1. Actual vs Predicted Prices

- Most predictions align closely with actual values
    
- Some deviation exists, especially for higher-priced houses
    

### 2. Residual Analysis

- Errors are mostly centered around zero
    
- Error spread increases for higher values (heteroscedasticity)
    

### 3. Price Distribution

- Dataset is right-skewed
    
- Majority of houses fall in lower price ranges
    

---

## 📂 Dataset

- Contains real estate data for Bangalore
    
- Includes features like:
    
    - Location
        
    - Square Footage
        
    - BHK
        
    - Bathrooms
        

---

## ⚙️ Tech Stack

- Python
    
- Flask
    
- Scikit-learn
    
- Pandas / NumPy
    
- HTML / Bootstrap
    

---

## 🔄 Project Workflow

User Input → Flask API → Data Preprocessing → Model Prediction → Output

---

## ⚠️ Limitations

- Model is based on linear regression (may not capture complex relationships)
    
- Performs less accurately on high-priced properties
    
- Dataset is imbalanced (more low-price houses than high-price ones)
    

---

## 🔮 Future Improvements

- Try advanced models (Random Forest, XGBoost)
    
- Apply log transformation to handle skewed data
    
- Improve UI/UX
    
- Add interactive visualizations
    

---

## 📌 Key Takeaway

This project demonstrates:

- End-to-end ML workflow
    
- Model evaluation and interpretation
    
- Backend integration using Flask
    
- Deployment on Render
    

---