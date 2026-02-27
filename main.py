import streamlit as st
import pandas as pd
import pickle
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import streamlit.components.v1 as components




st.set_page_config(
    page_title="ColorSnap",     # 👈 Tab name
    page_icon="🎨",             # 👈 Emoji as logo
    layout="centered"
)



st.header('Welcome to ColorSnap')


img =  st.file_uploader("Upload your image", type=["png", "jpg", "jpeg"])
if img is not None:
    img = Image.open(img).convert('RGB')

    img_array = np.array(img)

    img_reshaped = img_array.reshape(-1 , 3)
    kmean = KMeans(n_clusters=3)
    result = kmean.fit_predict(img_reshaped)

    width = height = 200
    dominant_colors = kmean.cluster_centers_

    # Loop through each dominant color and display it
    for i, color in enumerate(dominant_colors):
        r, g, b = color
        color_tuple = (int(r), int(g), int(b))

        img = Image.new(mode='RGB', size=(width, height), color=color_tuple)
        # print(f"Dominant Color {i + 1}: {color_tuple}" , end=' ')
        rgb_text = f"rgb{color_tuple}"

        html_code = f"""
            <div 
                onclick="navigator.clipboard.writeText('{rgb_text}')"
                style="
                    background-color: {rgb_text};
                    padding: 60px;
                    margin: 15px 0;
                    border-radius: 12px;
                    cursor: pointer;
                    text-align: center;
                    font-size: 18px;
                    font-weight: bold;
                    color: white;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                ">
                {rgb_text} <br>
                <small>(Click to Copy)</small>
            </div>
            """


        components.html(html_code, height=120)



else:
    st.write('Please upload an image')

