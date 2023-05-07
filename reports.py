import streamlit as st
from fpdf import FPDF
import base64

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
# Initialize Firebase Admin SDK

firebaseConfig = {
        apiKey: "AIzaSyCABO5A2bt8_ePU4tN7D92s6wTUlrWgCmE",
        authDomain: "healthcare-d6d4b.firebaseapp.com",
        projectId: "healthcare-d6d4b",
        storageBucket: "healthcare-d6d4b.appspot.com",
        messagingSenderId: "225897092313",
        appId: "1:225897092313:web:3c0fccdf8350b500a71ac8",
        measurementId: "G-VMVQZ4VJQR",
      };


# Fetch the service account key JSON file contents
cred = credentials.Certificate(firebaseConfig)
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://console.firebase.google.com/u/3/project/healthcare-d6d4b"
})

ref = db.reference('/Trial')

db = firestore.client()

# Define the data to be stored in the document
data = {
    "Name": "John"
}

# Add the data to a new document in a "users" collection
db.collection("Trial").add(data)

# Upload a local PDF file to Firebase Storage
# file_path = "path/to/local/file.pdf"
# blob = storage_client.blob("path/to/remote/file.pdf")
# blob.upload_from_filename(file_path)

report_text = st.text_input("Report Text")


export_as_pdf = st.button("Export Report")

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

if export_as_pdf:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 20, txt="Heart Diagnose", ln=1, align='C')
    pdf.cell(40, 10, report_text)
    
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

    st.markdown(html, unsafe_allow_html=True)