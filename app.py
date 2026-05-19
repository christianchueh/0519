import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作", "家庭" , "朋友"])

col_left, col_right = st.columns([1, 2], gap="large")

with col_left: 
    with st.container(border=True): 
        tt = st.write("行程描述")
        txt = st.text_input(" 時間：09:00")
        if st.button("新增行程"):
            @st.dialog("新增完成")
            def showAdd():
                st.write(f"新增行程 {txt} 成功")
            showAdd()

        today = st.date_input(
                  "選擇日期",
                  datetime.date.today()
                )

        meeting_time = st.time_input(
                          "選擇時間"
                        )

        my_color = st.color_picker(
                 "挑選辨識顏色",
                 "#1A73E8"
                )
        st.line_chart([1, 5, 2, 6, 2, 1] , my_color)


with col_right: 
    st.write("###  行程檢視") 
    tab1 , tab2 = st.tabs(["本月行程" , "已封存的行程"])

    with tab1:
        with st.container(border=True):
            st.write("本月行程")
    with tab2:
        with st.container(border=True):
            st.write("已封存的行程")

st.write("上面是大標題")
st.divider()
st.write("下面是內容區塊")
st.button("按鈕 A")
st.write("")  # 塞入一行空白間距
st.button("按鈕 B")

with st.popover("快速進階篩選"):
    st.checkbox("隱藏已過期行程")
