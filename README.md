# CV Data Extractor

## 📌 Project Overview
CV Data Extractor is a Python-based tool that extracts key details from CVs (PDFs) using **LangChain** and **Google Gemini AI**. It identifies **names, emails, phone numbers, and skills** and saves the extracted information in an Excel file. Plus, it can even send this data via email! Talk about automation at its finest! 🚀

## ✨ Features
- Extracts **name, email, contact, and skills** from CVs
- Uses **LangChain** for AI-powered text extraction
- Saves extracted data into an **Excel file (.xlsx)**
- Sends extracted details to a company email automatically 📩
- Easy to use with a **Streamlit UI**

## 🔧 Installation
Make sure you have **Python 3.9+** installed, then follow these steps:

```sh
# Clone the repository
git clone https://github.com/your-username/CV_Data_Extractor.git
cd CV_Data_Extractor

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage
1. Place CV files in the project directory 📂
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
3. Upload a CV file and let AI do its magic! 🎩✨

## 🛠️ Technologies Used
- **Python** 🐍
- **LangChain** (for AI-driven text extraction)
- **Google Gemini AI**
- **Streamlit** (for the user interface)
- **pandas & openpyxl** (for Excel file handling)
- **SMTP** (for email automation)

## 🤝 Contribution
Want to improve this project? Follow these steps:
1. Fork the repo 🍴
2. Create a new branch (`git checkout -b feature-xyz`)
3. Make your changes and commit (`git commit -m 'Added new feature'`)
4. Push to your branch (`git push origin feature-xyz`)
5. Open a pull request 🔥

## 📜 License
This project is open-source and free to use under the **MIT License**. Feel free to modify and share! 😊

---
Now, what are you waiting for? Give this project a spin and make CV processing **super easy!** 🏆

