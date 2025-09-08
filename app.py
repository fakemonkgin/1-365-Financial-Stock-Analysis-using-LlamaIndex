import os
import openai
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex,Settings, StorageContext, load_index_from_storage
from llama_index.llms.openai import OpenAI
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

Settings.llm = OpenAI(model="gpt-3.5-turbo")

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

st.title("Financial Stock Analysis using LlamaIndex")
st.header("Reports:")

report_type = st.selectbox(
    "What type of report do you want?",
    ("Single Stock Outlook", "Competitor Analysis")
)

if report_type == "Single Stock Outlook":
    symbol = st.text_input("Stock Symbol")

    if symbol:
        with st.spinner(f"Generating report for {symbol}..."):
            response = query_engine.query(f"write a report on the outlook for {symbol} stock from the years 2023-2027")
            st.write(str(response))

if report_type == "Competitor Analysis":
    symbol1 = st.text_input("Stock Symbol 1")
    symbol2 = st.text_input("Stock Symbol 2")

    if symbol1 and symbol2:
        with st.spinner(f"Generating report for {symbol1} vs {symbol2}"):
            response = query_engine.query(f"Write a report on the competition between {symbol1} stock and {symbol2} stock")
            st.write(str(response))

