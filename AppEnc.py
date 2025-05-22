import streamlit as st
import cv2
import numpy as np
import os
from PIL import Image
def logistic_map(r,x,n):
    sequence = [x]
    for i in range(n):
        x=r*x*(1-x)
        sequence.append(x)
        return np.array(sequence)
def encrypt_image(image, x0, r=3.99):
    M, N = image.shape
    num_pixels = M * N
    
    chaotic_seq = logistic_map(r, x0, num_pixels)
    chaotic_seq = (chaotic_seq * 255).astype(np.uint8).reshape(M,N)
    
    encrypted_image = cv2.bitwise_xor(image, chaotic_seq)
    return encrypted_image, chaotic_seq

def decrypt_image(encrypted_image, chaotic_seq):
    decrypted_image = cv2.bitwise_xor(encrypt_image, chaotic_seq)
    return decrypted_image

st.set_page_config(page_title="Image Encryption & Decryption", page_icon="🔒",  layout="centered")
st.markdown("""
    <style>
        .stbutton>button{
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .stDownloadButton>button{
            background-color: #008CBA;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        input[type=number]{
            -moz-appearance: textfield;
        }
        input[type=number]::-webkit-inner-spin-button,
            """)