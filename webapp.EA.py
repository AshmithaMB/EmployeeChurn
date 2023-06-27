import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open("C:/Users/ashut/Downloads/deploy/trained_model.EA", 'rb'))

#creating a function for prediction

def attrition_prediction(input_data):
    np_array = np.asarray(input_data)
    np_array = np_array.reshape(1, -1)
    
    prediction = loaded_model.predict(np_array)
    if prediction == 0:
      return "The employee is predicted to not leave the company (not attrited)."
    else:
      return "The employee is predicted to leave the company (attrited)."


def main():
    
    # Title
    st.title("Employee Attrition Prediction Web Application")
    
    # Input Data
    satisfaction_level = st.text_input('Enter employee satisfaction level:')
    last_evaluation = st.text_input("Enter employee's last evaluation:")
    number_project = st.text_input("Number of projects:")
    average_monthly_hours = st.text_input("Employee's average monthly hours:")
    time_spend_company = st.text_input("Enter years at company:")
    Work_accident = st.text_input("Work accident? (1 for Yes, 0 for No):")
    promotion_last_5years = st.text_input("Promotion in the last 5 years? (1 for Yes, 0 for No):")
    Salary = st.text_input("Salary level (0 for High, 1 for Low, 2 for Medium):")
    Departments = st.text_input("Enter the department code (0 for IT, 1 for RandD, 2 for Accounting, 3 for HR, 4 for Management, 5 for Marketing, 6 for Product Management, 7 for Sales, 8 for Support, 9 for Technical):")
    
    # Code for Prediction
    analysis = ''
    
    if st.button("Employee churn prediction result"):
        if '' in [satisfaction_level, last_evaluation, number_project, average_monthly_hours, time_spend_company, Work_accident, promotion_last_5years, Salary, Departments]:
            analysis = "Please fill in all the input fields."
        else:
            input_data = [float(satisfaction_level), float(last_evaluation), float(number_project), float(average_monthly_hours), float(time_spend_company), float(Work_accident), float(promotion_last_5years), float(Salary), float(Departments)]
            analysis = attrition_prediction(input_data)
        
    st.success(analysis)    
        
        
if __name__ == '__main__':
    main()