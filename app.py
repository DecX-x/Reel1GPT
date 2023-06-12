import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

st.title('💀GPT')
st.write('Using OpenAI Gpt models')
prompt = st.text_input('Prompt: ')

llm = OpenAI(temperature=0.9)

if prompt:
    response = llm(prompt)
    st.write(response)