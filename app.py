import streamlit as st
st.set_page_config(page_title="微型 TimeTree", layout="wide")
with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作", "家庭" , "朋友"])

col_left, col_center, col_right = st.columns([1, 2, 1.2], gap="large")

with col_left: 
    st.write("###  新增區") 
    st.button("按鈕放左邊")
    with st.container(border=True): 
        st.write(" 標題：開學典禮") 
        st.write(" 時間：09:00")

with col_center: 
    st.write("###  看板區") 
    st.info("主要行程訊息放中間")
    tab1, tab2, tab3 = st.tabs(["首頁", "圖表", "設定"])
    with tab1: 
        st.header("首頁") 
        st.write("這是首頁內容")
    with tab2: 
        st.header("圖表") 
        st.line_chart([1, 5, 2, 6, 2, 1])
    with tab3: 
        st.header("設定") 
        name = st.text_input("你的名字") 
        st.write(f"Hello {name}")

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
