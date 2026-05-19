import streamlit as st

st.title("極簡暫存示範")

# 1. 初始化
if "my_list" not in st.session_state:
    st.session_state.my_list = ["蘋果", "香蕉"]

# 2. 新增功能
new_item = st.text_input("輸入要新增的東西")

if st.button("確認新增"):
    # 加上去除空白的防禦
    if new_item.strip():
        st.session_state.my_list.append(new_item)
        st.success(f"成功暫存：{new_item}")
        st.rerun()
    else:
        st.error("請勿輸入空白內容！")

st.divider()

# 3. 刪除功能
if st.session_state.my_list:
    target = st.selectbox("選擇要刪除的東西", st.session_state.my_list)

    if st.button("確認刪除"):
        st.session_state.my_list.remove(target)
        st.rerun()
else:
    st.write("目前清單空空如也")

st.divider()

# 4. 顯示結果
st.write("📊 當前暫存清單：", st.session_state.my_list)

# streamlit資料暫存範例
