#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit

#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

subject = "AI"
result = chat_model.invoke(subject + "에 대한 음식레시피를 써줘.")
print(result.content)

import streamlit as st

st.title("인공지능 요리사")
subject = st.text_input("음식의 이름 입력해주세요.")
st.write("음식의 이름 : " + subject)

if st.button("음식레시피 작성"):
    with st.spinner("음식레시피 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 음식레시피를 써줘")
        st.write(result.content)
