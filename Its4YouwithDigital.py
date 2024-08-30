import streamlit as st
import pandas as pd
import time
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import base64
from io import BytesIO

st.markdown("<h2 style='text-align:center'>ITS 4 YOU</h2>", unsafe_allow_html=True)

if "photo" not in st.session_state:
    st.session_state["photo"]= "not done"
    
def change_photo_state():
    st.session_state["photo"]="done"
    
upload_photo = st.file_uploader("upload_photo",on_change=change_photo_state)
camera_photo = st.camera_input("Take a photo",on_change=change_photo_state)

if st.session_state["photo"]=="done":
   progress_bar = st.progress(0)

for perc_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)
st.success("photo uploaded successfuly.")

with st.form("form 1", clear_on_submit=True):
    st.text_input("Family Name")
    st.text_input("Last Name")
    st.text_input("Birth Name")
    st.text_input("Mother's Family Name")
    st.text_input("Mother's Last Name")
    st.text_input("Place of birth")
    st.text_input("Date of birth")
    st.text_input("Nationality")
    st.text_input("Religion")
    st.text_input("Passport #")
    st.text_input("When did you come to here, concrete date as in the passport stamp:")
    st.text_input("Which border airport:")
    st.text_input("Family status:")
    st.text_input("Education Level")
    st.text_input("Profession in original country:")
    st.text_input("Company registration number")
    st.text_input("Saving amount")
    st.text_input("Hungarian TRC #")
    st.text_input("Hungarian Tax ID #")
    st.text_input("Hungarian Business Tax ID #")
    st.text_input("Hungarian Business Registration ID")
    st.text_input("Hungarian Health Card #")
    st.text_input("Driving License #")
    st.text_input("Bank Name")
    st.text_input("Bank Account #")
    radio_btn = st.radio("Gender", options=("Male", "Female"))
    radio_btn1 = st.radio("Have you ever had rejection?", options=("Yes", "No"))
    radio_btn2 = st.radio("Have you ever committed a crime?", options=("Yes", "No"))
    
    st.markdown("Permanent Address")
    code, District = st.columns(2)
    code.text_input("Post Code")
    District.text_input("District")
    street, floor, door = st.columns(3)
    street.text_input("Street")
    floor.text_input("Floor")
    door.text_input("Room")

    st.text_input("Full Address")
    st.text_input("Email Address")
    st.text_input("Mobile Number")
    st.text_input("Current Status")
    radio_btn3 = st.radio("Marital Status", options=("Single", "Married", "Other"))

    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    Initial, Remaining, Total = st.columns(3)
    Initial.text_input("Initial Amount")
    Remaining.text_input("Remaining Amount")
    Total.text_input("Total Amount")

    st.title("Digital Signature Capture")
    st.write("Please sign below:")

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
        stroke_width=2,
        stroke_color="black",
        background_color="white",
        height=150,
        width=300,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Save the signature
    if canvas_result.image_data is not None:
        signature_image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
        
        # Display the signature
        st.image(signature_image)

        # Save the signature as a file
        save_button = st.button("Save Signature")
        if save_button:
            buffered = BytesIO()
            signature_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            st.write(f"Signature saved. Base64 encoded image: {img_str}")

            # Save to file
            signature_image.save("signature.png")
            st.success("Signature saved as 'signature.png'")

    
            s_state = st.form_submit_button("Submit")
            
    s_state = st.form_submit_button("Submit")
