# -*- coding: utf-8 -*-
"""
Created on Sat June 17 2023
@author: Zakaria Bouidane - Lokman Mihoubi
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="SmartDoc",
    page_icon=":stethoscope:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('SmartDoc: Système intelligent aidant au diagnostic des maladies',
                          ['Prédiction du diabète', 'Prédiction des maladies cardiaques'],
                          icons=['💉', '❤️'],
                          default_index=0)

# Page de prédiction du diabète
if selected == 'Prédiction du diabète':
    # Set page title and icon
    st.title('Diagnostic du diabète')
    st.markdown("💉 Fournissez les informations nécessaires pour le diagnostic.")

    # Get user input data
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Nombre de grossesses', min_value=0, step=1)

    with col2:
        Glucose = st.number_input('Niveau de glucose', min_value=0.0, step=1.0)

    with col3:
        BloodPressure = st.number_input('Valeur de la pression artérielle', min_value=0.0, step=1.0)

    with col1:
        SkinThickness = st.number_input('Épaisseur de la peau', min_value=0.0, step=1.0)

    with col2:
        Insulin = st.number_input('Niveau d\'insuline', min_value=0.0, step=1.0)

    with col3:
        BMI = st.number_input('Valeur de l\'IMC', min_value=0.0, step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Valeur de la fonction de pedigree du diabète', min_value=0.0, step=0.1)

    with col2:
        Age = st.number_input('Âge de la personne', min_value=0, step=1)

    # Code de prédiction
    diab_diagnosis = ''

    # Create a button for prediction
    if st.button('Résultat du test de diabète'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'La personne est diabétique'
        else:
            diab_diagnosis = 'La personne n\'est pas diabétique'

    st.success(diab_diagnosis)


# Page de prédiction des maladies cardiaques
if selected == 'Prédiction des maladies cardiaques':
    # Set page title and icon
    st.title('Diagnostic des maladies cardiaques')
    st.markdown("❤️ Fournissez les informations nécessaires pour le diagnostic.")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Âge', min_value=0, step=1)

    with col2:
       sex = st.selectbox('Sexe', ['Féminin', 'Masculin'], index=0)

    with col3:
        cp = st.number_input('Types de douleurs thoraciques', min_value=0, step=1)

    with col1:
        trestbps = st.number_input('Tension artérielle au repos', min_value=0.0, step=1.0)

    with col2:
        chol = st.number_input('Cholestérol', min_value=0.0, step=1.0)

    with col3:
        fbs = st.number_input('Taux de sucre dans le sang à jeun', min_value=0.0, step=1.0)

    with col1:
        restecg = st.number_input('Résultats de l\'électrocardiogramme au repos', min_value=0.0, step=1.0)

    with col2:
        thalach = st.number_input('Fréquence cardiaque maximale atteinte', min_value=0.0, step=1.0)

    with col3:
        exang = st.number_input('Angine induite par l\'effort', min_value=0.0, step=1.0)

    with col1:
        oldpeak = st.number_input('Dépression ST induite par l\'effort', min_value=0.0, step=0.1)

    with col2:
        slope = st.number_input('Pente du segment ST d\'effort', min_value=0.0, step=0.1)

    with col3:
        ca = st.number_input('Nombre de vaisseaux principaux colorés par fluoroscopie', min_value=0.0, step=1.0)

    with col1:
        thal_translation = {0: 'Normal', 1: 'Défaut corrigé', 2: 'Défaut réversible'}
        thal_options = list(thal_translation.values())
        thal_text = st.selectbox('Résultats d\'un test sanguin appelé test de thallium', thal_options)
        thal = list(thal_translation.keys())[list(thal_translation.values()).index(thal_text)]

    sex = 0 if sex == 'Féminin' else 1
    # Code de prédiction
    heart_diagnosis = ''

    # Create a button for prediction
    if st.button('Résultat du test des maladies cardiaques'):
        # Convert input values to numeric types
        age = float(age)
        sex = float(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = float(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = float(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)

        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'La personne souffre d\'une maladie cardiaque'
        else:
            heart_diagnosis = 'La personne ne souffre d\'aucune maladie cardiaque'

    st.success(heart_diagnosis)
