import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import base64


# model = pickle.load(open('model.pkl','rb'))


st.title("Poteto disese:")

file = st.file_uploader("Please choose a file")

st.button('Predict')