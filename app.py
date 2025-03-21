import streamlit as st
import os
from dotenv import load_dotenv
from pdf_extractor import extract_text_from_pdf
from ai_extractor import extract_cv_data
from data_saver import save_to_excel
from email_sender import send_email

# Load environment variables
load_dotenv()
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")

def main():  # Define the main function
    st.title("Send CV to Company 📄🤖")

    uploaded_file = st.file_uploader("Upload your CV (PDF only)", type=["pdf"])

    if uploaded_file:
        st.success("✅ CV Uploaded Successfully!")
        
        if st.button("Confirm & Send"):
            with st.spinner("Processing CV..."):
                text = extract_text_from_pdf(uploaded_file)

                result = extract_cv_data(text)

                user_data = {
                    "Name": result.get("name", "N/A"),
                    "Email": result.get("email", "N/A"),
                    "Contact": result.get("contact", "N/A"),
                    "Skills": ", ".join(result.get("skills", [])),
                }
                save_to_excel(user_data)

                company_email = "21014198-032@uog.edu.pk"
                subject = "New Job Application - CV Data"
                body = f"""
                Name: {user_data['Name']}
                Email: {user_data['Email']}
                Contact: {user_data['Contact']}
                Skills: {user_data['Skills']}
                """

                email_status = send_email(company_email, subject, body)

                if email_status:
                    st.success("✅ We received your CV. We will contact you soon.")
                else:
                    st.error("❌ Failed to send email.")

            st.success("✅ Your CV data has also been saved to 'cv_data.xlsx'.")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()