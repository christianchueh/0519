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
    with st.expander("查看進階提醒參數設定"):
        st.write("這裡是發信伺服器的底層設定...")
    
    @st.dialog("系統公告")
    def show_alert():
        st.write("本週作業請確認 requirements.txt 有正確設定！")
    if st.button("查看公告"): 
        show_alert()
