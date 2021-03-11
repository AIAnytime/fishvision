#--------------------Beginning of all Imports--------------------#
#Utility pkgs
import os, sys
import base64
from pathlib import Path
from PIL import Image

#Importing web framework streamlit
import streamlit as st

#Numpy for computation
import numpy as np

#Neural nets pkgs
import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model

import cv2
import tempfile

#loading utils for design
from utility import (
    img_to_bytes,
    read_markdown_file,
)

#----------------Import Completed--------------------------------#

#Defining the labels 
class_names = ['Hourse Mackerel', 'Black Sea Sprat', 'Sea Bass',
'Red Mullet','Trout', 'Striped Red Mullet', 'Shrimp', 
'Gilt-Head Bream','Red Sea Bream']


def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele   
    return str1 


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True) 

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')




#------------------The main function---------------------------#
def main():
    menu = ['Home', 'Identify in Image', 'About Me']
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        welcome_markdown = read_markdown_file("markdown/hi.md")
        st.markdown(welcome_markdown, unsafe_allow_html=True)
    elif choice == "Identify in Image":
        image_file = st.file_uploader("Upload an Image that contains a Fish 🐬",
        type=['jpg', 'jpeg', 'png'])
        st.write('')

        if image_file is not None:
            img = Image.open(image_file)
            img = img.resize((224,224))
            #img = image.loaploaded_img(image_file, target_size=(224, 224))
            st.write(' ')
            st.write(' ')
            st.image(img)

            x = image.img_to_array(img)
            #st.write(x)
            x = np.expand_dims(x, axis=0)
            #st.write(x)
            if st.button("Identify"):
                new_model = load_model("model/model.h5")
                #classes = new_model.predict(x)
                #st.write(classes)
                classes = np.argmax(new_model.predict(x), axis = -1)
                names = [class_names[i] for i in classes]
                st.write('')
                st.success("The identified Fish is : "+ listToString(names) + " 🐠")
    else:
        about_markdown = read_markdown_file("markdown/aboutme.md")
        st.markdown(about_markdown, unsafe_allow_html=True)



if __name__ == '__main__':
    main()
