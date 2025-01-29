import streamlit as st
import pandas as pd
import time
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import base64
from io import BytesIO

st.markdown("<h2 style='text-align:center'>ITS 4 YOU</h2>", unsafe_allow_html=True)

st.sidebar.header("It's 4 you.")
selected_year = st.sidebar.selectbox("page", options=["page1", "page2"])

if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

def change_photo_state():
    st.session_state["photo"] = "done"

upload_photo = st.file_uploader("Upload Photo", on_change=change_photo_state)
camera_photo = st.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done":
    progress_bar = st.progress(0)
    for perc_completed in range(100):
        time.sleep(0.02)  # Reduce sleep time for faster progress
        progress_bar.progress(perc_completed + 1)
    st.success("Photo uploaded successfully.")

with st.form("form 1", clear_on_submit=True):
    st.text_input("Family Name", key="family_name")
    st.text_input("Last Name", key="last_name")
    st.text_input("Birth Name", key="birth_name")
    st.text_input("Mother's Family Name", key="mother_family_name")
    st.text_input("Mother's Last Name", key="mother_last_name")
    st.text_input("Place of birth", key="place_of_birth")
    st.text_input("Date of birth", key="date_of_birth")
    st.text_input("Nationality", key="nationality")
    st.text_input("Religion", key="religion")
    st.text_input("Passport #", key="passport_number")
    st.text_input("When did you come to here, concrete date as in the passport stamp:", key="arrival_date")
    st.text_input("Which border airport:", key="border_airport")
    st.text_input("Family status:", key="family_status")
    st.text_input("Education Level", key="education_level")
    st.text_input("Profession in original country:", key="profession")
    st.text_input("Company registration number", key="company_registration_number")
    st.text_input("Saving amount", key="saving_amount")
    st.text_input("Hungarian TRC #", key="hungarian_trc")
    st.text_input("Hungarian Tax ID #", key="hungarian_tax_id")
    st.text_input("Hungarian Business Tax ID #", key="hungarian_business_tax_id")
    st.text_input("Hungarian Business Registration ID", key="hungarian_business_registration_id")
    st.text_input("Hungarian Health Card #", key="hungarian_health_card")
    st.text_input("Driving License #", key="driving_license")
    st.text_input("Bank Name", key="bank_name")
    st.text_input("Bank Account #", key="bank_account")
    radio_btn = st.radio("Gender", options=("Male", "Female"), key="gender")
    radio_btn1 = st.radio("Have you ever had rejection?", options=("Yes", "No"), key="rejection")
    radio_btn2 = st.radio("Have you ever committed a crime?", options=("Yes", "No"), key="crime")

    st.markdown("Permanent Address")
    code, district = st.columns(2)
    code.text_input("Post Code", key="post_code")
    district.text_input("District", key="district")
    street, floor, door = st.columns(3)
    street.text_input("Street", key="street")
    floor.text_input("Floor", key="floor")
    door.text_input("Room", key="room")

    st.text_input("Full Address", key="full_address")
    st.text_input("Email Address", key="email")
    st.text_input("Mobile Number", key="mobile_number")
    st.text_input("Current Status", key="current_status")
    radio_btn3 = st.radio("Marital Status", options=("Single", "Married", "Other"), key="marital_status")

    day, month, year = st.columns(3)
    day.text_input("Day", key="day")
    month.text_input("Month", key="month")
    year.text_input("Year", key="year")

    initial, remaining, total = st.columns(3)
    initial.text_input("Initial Amount", key="initial_amount")
    remaining.text_input("Remaining Amount", key="remaining_amount")
    total.text_input("Total Amount", key="total_amount")

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
    # Submit the form
    form_submit = st.form_submit_button("Submit")
    if form_submit:
        if canvas_result.image_data is not None:
            buffered = BytesIO()
            signature_image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
  
    
            # Save to file
            signature_image.save("signature.png")
            st.success("Signature saved as 'signature.png'")

    
    
        # Collect all form data
        form_data = {
            "Family Name": st.session_state.get("family_name", ""),
            "Last Name": st.session_state.get("last_name", ""),
            "Birth Name": st.session_state.get("birth_name", ""),
            "Mother's Family Name": st.session_state.get("mother_family_name", ""),
            "Mother's Last Name": st.session_state.get("mother_last_name", ""),
            "Place of birth": st.session_state.get("place_of_birth", ""),
            "Date of birth": st.session_state.get("date_of_birth", ""),
            "Nationality": st.session_state.get("nationality", ""),
            "Religion": st.session_state.get("religion", ""),
            "Passport #": st.session_state.get("passport_number", ""),
            "Arrival Date": st.session_state.get("arrival_date", ""),
            "Border Airport": st.session_state.get("border_airport", ""),
            "Family Status": st.session_state.get("family_status", ""),
            "Education Level": st.session_state.get("education_level", ""),
            "Profession": st.session_state.get("profession", ""),
            "Company Registration Number": st.session_state.get("company_registration_number", ""),
            "Saving Amount": st.session_state.get("saving_amount", ""),
            "Hungarian TRC #": st.session_state.get("hungarian_trc", ""),
            "Hungarian Tax ID #": st.session_state.get("hungarian_tax_id", ""),
            "Hungarian Business Tax ID #": st.session_state.get("hungarian_business_tax_id", ""),
            "Hungarian Business Registration ID": st.session_state.get("hungarian_business_registration_id", ""),
            "Hungarian Health Card #": st.session_state.get("hungarian_health_card", ""),
            "Driving License #": st.session_state.get("driving_license", ""),
            "Bank Name": st.session_state.get("bank_name", ""),
            "Bank Account #": st.session_state.get("bank_account", ""),
            "Gender": st.session_state.get("gender", ""),
            "Rejection": st.session_state.get("rejection", ""),
            "Crime": st.session_state.get("crime", ""),
            "Post Code": st.session_state.get("post_code", ""),
            "District": st.session_state.get("district", ""),
            "Street": st.session_state.get("street", ""),
            "Floor": st.session_state.get("floor", ""),
            "Room": st.session_state.get("room", ""),
            "Full Address": st.session_state.get("full_address", ""),
            "Email Address": st.session_state.get("email", ""),
            "Mobile Number": st.session_state.get("mobile_number", ""),
            "Current Status": st.session_state.get("current_status", ""),
            "Marital Status": st.session_state.get("marital_status", ""),
            "Day": st.session_state.get("day", ""),
            "Month": st.session_state.get("month", ""),
            "Year": st.session_state.get("year", ""),
            "Initial Amount": st.session_state.get("initial_amount", ""),
            "Remaining Amount": st.session_state.get("remaining_amount", ""),
            "Total Amount": st.session_state.get("total_amount", ""),
        }

        # Convert to DataFrame
        df = pd.DataFrame([form_data])

        # Save to CSV
        df.to_csv("form_data.csv", index=False)
        st.success("Form submitted successfully and data saved to 'form_data.csv'!")