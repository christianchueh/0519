import streamlit as st
st.set_page_config(page_title="微型 TimeTree", layout="wide")
with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作", "家庭" , "朋友"])

col_left, col_right = st.columns([1, 2], gap="large")

with col_left: 
    with st.container(border=True): 
        st.write("形成描述")
        txt = st.text_input(" 時間：09:00")
        if st.button("新增行程"):
            @st.dialog("新增完成")
            def showAdd():
                st.write(f"新增行程 {txt} 成功")
            showAdd()


with col_right: 
    st.write("###  設定區") 
    st.button("控制項放右邊")
    tab1 , tab2 = st.tabs(["本月行程" , "已封存的行程"])

    with tab1:
        with st.container(border=True):
            st.write("本月行程")
    with tab1:
        with st.container(border=True):
            st.write("已封存的行程")
