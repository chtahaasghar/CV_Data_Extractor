from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

# Initialize Google Gemini Model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define Extraction Schema
class ExtractData(BaseModel):
    name: str = Field(description="Extract name from the content")
    email: str = Field(description="Extract email from the content")
    contact: str = Field(description="Extract contact number (including country code if available)")
    skills: list[str] = Field(description="Extract skills from the content")

def extract_cv_data(text):
    output = model.with_structured_output(ExtractData)
    result = output.invoke(text)
    return result.dict()
