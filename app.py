import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
mode = st.radio("選擇群組" , ["學生" , "老師" , "家長會" , "校友會"],horizontal=True)


l , r = st.columns(2)

with l:
    st.text_input("行程主旨")
    st.color_picker("顏色設定")
with r:
    st.date_input("日期選擇" , datetime.date.today())
    st.time_input("時間選擇")


view = st.segmented_control(
  "檢視模式",
  ["月視角", "週視角"],
  default="月視角"
)

tag = st.pills(
  "行程屬性",
  ["#工作", "#家庭", "#緊急"]
)
