# -*- coding: utf-8 -*-



import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open("D:/Special Topic 2/multiple disease/models/diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("D:/Special Topic 2/multiple disease/models/heart_disease_model.sav",'rb'))

parkinsons_model = pickle.load(open("D:/Special Topic 2/multiple disease/models/parkinsons_model.sav", 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Glucose = st.text_input('Glucose Level')
        
    with col2:
        BMI = st.text_input('BMI value')
    
    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col1:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[float(Glucose),float(BMI), float(DiabetesPedigreeFunction), float(Age)]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cigsPerDay = st.text_input('Cigarettes per day')
        
    
    with col1:
        totChol = st.text_input('total Cholestoral in mg/dl')
        
    with col2:
        sysBP = st.text_input('Blood pressure')
        
    with col3:
        glucose = st.text_input('Glucose levels')
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[float(age), int(sex), float(cigsPerDay), float(totChol), float(sysBP), float(glucose)]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('Fhi(Hz)')
        
    with col3:
        flo = st.text_input('Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('Jitter(%)')
        
    with col1:
        Jitter_Abs = st.text_input('Jitter(Abs)')
        
    with col2:
        RAP = st.text_input('MDVP:RAP')
        
    with col3:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col4:
        DDP = st.text_input('Jitter:DDP')
        
    with col1:
        Shimmer = st.text_input('MDVP')
        
    with col2:
        Shimmer_dB = st.text_input('MDVP(dB)')
        
    with col3:
        APQ3 = st.text_input('APQ3')
        
    with col4:
        APQ5 = st.text_input('APQ5')
        
    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA = st.text_input('DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col4:
        HNR = st.text_input('HNR')
        
    with col1:
        RPDE = st.text_input('RPDE')
        
    with col2:
        DFA = st.text_input('DFA')
        
    with col3:
        spread1 = st.text_input('spread1')
        
    with col4:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ),float(DDP),float(Shimmer),float(Shimmer_dB),float(APQ3),float(APQ5),float(APQ),float(DDA),float(NHR),float(HNR),float(RPDE),float(DFA),float(spread1),float(spread2),float(D2),float(PPE)]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


