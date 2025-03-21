import pandas as pd
import os

def save_to_excel(data):
    file_path = "cv_data.xlsx"

    df_new = pd.DataFrame([data])

    if os.path.exists(file_path):
        df_existing = pd.read_excel(file_path, engine="openpyxl")
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_excel(file_path, index=False, engine="openpyxl")
