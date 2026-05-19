import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
mode = st.radio("選擇群組" , ["學生" , "老師" , "家長會" , "校友會"])
l , r = st.columns(2)

with l:
    st.text_input("行程主旨")
    st.color_picker("顏色設定")
with r:
    st.data_input("日期選擇")
    st.time_input("時間選擇")

with st.popover("快速進階篩選"):
    st.checkbox("隱藏已過期行程")
