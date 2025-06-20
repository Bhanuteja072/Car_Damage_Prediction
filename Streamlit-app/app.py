import streamlit as st
from model_helper import predict

st.title("Vehicle damage detection")

uploaded_file=st.file_uploader("Upload file",type=['jpg','png'])


if uploaded_file:
    image_path="temp_file.jpg"
    with open(image_path,"wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file,caption="Uploaded_file",use_container_width=True)
        predicion=predict(image_path)
        st.info(f"Predicted Class :{predicion}")
        