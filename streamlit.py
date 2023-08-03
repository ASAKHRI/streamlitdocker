import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import pickle
from PIL import Image
import time


# Appel à l'API pour récupérer les informations de vol
url = "https://webnejnejapp.azurewebsites.net/"
response = requests.get(url)
flights = response.json()
url1 = "https://webnejnejapp.azurewebsites.net/predict"


# Fonction pour la page "Ajouter"
def add_page():
    st.title("Formulaire d'entrée pour les mesures d'une fleur")

    # Créer des widgets pour les mesures de la fleur

    sepal_length = st.slider("Sepal length", 0, 10, 5)
    sepal_width = st.slider("Sepal width", 0, 10, 3)
    petal_length = st.slider("Petal length", 0, 10, 1)
    petal_width = st.slider("Petal width", 0, 10, 2)



    if st.button("Ajouter Fleur", key="ajouter_fleur_button"):
        iris_data = {
                "sepal_length": sepal_length ,
                "sepal_width":sepal_width,
                "petal_length":petal_length,
                "petal_width":petal_width
            }

        # Envoyer les données à l'API
        response = requests.post(url1, json=iris_data)

        # Vérifier si la requête a réussi
        if response.ok:
        # Afficher un message de succès
                # Afficher un message de succès
            st.success("Les informations de votre fleur ont été ajouté avec succès !")

            # Afficher les informations de la fleur de manière plus esthétique
            st.write(f"La fleure est : {response.json()['prediction']}.")
            st.write(f"Avec une probabilité d'exactitude de : {response.json()['probability']}.")
        # Afficher les informations de la fleur
            #st.write(response.json())
        else:
        # Afficher un message d'erreur
            st.error("Erreur lors de l'ajout des informations de votre fleur.")



add_page()
#---------------------  Sidebar  ----------------------#
# Menu déroulant pour sélectionner la page à afficher
menu = ["iris"]
choice = st.sidebar.selectbox(" ", menu)
