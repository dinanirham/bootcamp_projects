from PIL import Image
import streamlit as st
import requests
import json
import numpy as np
import tensorflow as tf

st.set_page_config(
    page_title="A Tea Leaves Diseases Predictor",
    page_icon="📇",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/dinanirham',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': "This is web-based application for Author's very first classification model deployment on subject of StartUp's Success Prediction"
    }
)

st.title("A Tea Leaves Diseases Predictor")
st.subheader("Predict the diseases of tea leaves. We can take care the tea's diseases as soon as possible.")

# Uploader
uploader = st.file_uploader('Upload image from your local...', type=['jpg', 'png'])
if uploader is not None:
    image = Image.open(uploader)
else:
    st.write('waiting for your uploaded image')

# URL backend
URL = "https://irham-dinan-ftds-p2m2-bend.herokuapp.com/v1/models/tea_leaves_diseases:predict"

# predictor
predictor = st.button('predict')
if predictor: 
    # preprocess input inference image
    image = np.array(image)[:, :, :]
    image = tf.image.resize(image, size=(224, 224))
    image = image / 255.0
    image = tf.expand_dims(image, axis=0)
    imagelist = image.numpy().tolist()
    
    # inference image request to backend for model prediction
    input_data_json = json.dumps({
    'signature_name':'serving_default',
    'instances':imagelist})
    response = requests.post(URL, data=input_data_json)
    response.raise_for_status()
    response = response.json()
    result = np.argmax(response['predictions'][0])
    
    # prediction result
    if result == 0:
        st.subheader("The Disease of Tea Leaf Is Possibly Anthracnose")
    elif result == 1:
        st.subheader("The Disease of Tea Leaf Is Possibly Algal Leaf")
    elif result == 2:
        st.subheader("The Disease of Tea Leaf Is Possibly Bird Eye Spot")
    elif result == 3:
        st.subheader("The Disease of Tea Leaf Is Possibly Brown Blight")
    elif result == 4:
        st.subheader("The Disease of Tea Leaf Is Possibly Gray Light")
    elif result == 5:
        st.subheader("The Disease of Tea Leaf Is Possibly Healthy")
    elif result == 6:
        st.subheader("The Disease of Tea Leaf Is Possibly Red Leaf Spot")
    else:
        st.subheader("The Disease of Tea Leaf Is Possibly  White Spot")



