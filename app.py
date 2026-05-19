import streamlit as st
from datetime import datetime, time

st.set_page_config(page_title="TimeTree 智慧行事曆", layout="wide")

# =========================
# 1️⃣ Sidebar
# =========================
with st.sidebar:
    st.title("📅 行事曆群組")
    st.caption("edit by 闕河正")

    calendar_group = st.radio(
        "切換當前行事曆：",
        ["課務行事曆", "家庭行程", "個人重點"]
    )

    st.divider()

    st.subheader("🔐 權限認證")
    vip_code = st.text_input("輸入 VIP 授權碼", type="password")

    if vip_code == "VIP999":
        st.success("VIP 優先通知權限已開啟！")


# =========================
# 2️⃣ Header
# =========================
st.title("📊 TimeTree 智慧行事曆系統")
st.caption("Streamlit UI 整合版本")

view_mode = st.radio(
    "視角切換",
    ["月曆看板", "清單模式"],
    horizontal=True
)

st.divider()


# =========================
# 3️⃣ session state
# =========================
if "events" not in st.session_state:
    st.session_state.events = []


# =========================
# 4️⃣ layout
# =========================
col_left, col_center, col_right = st.columns([1, 2, 1.2])


# =========================
# 5️⃣ 左欄（新增行程）
# =========================
with col_left:
    st.subheader("➕ 新增行程")

    title = st.text_input("行程主旨")
    tag = st.selectbox("分類", ["工作", "家庭", "緊急"])
    date = st.date_input("日期")
    start = st.time_input("開始時間", time(9, 0))
    end = st.time_input("結束時間", time(10, 0))
    color = st.color_picker("顏色", "#1A73E8")

    note = st.text_area("備註")

    if st.button("新增行程", type="primary"):
        if title.strip():
            st.session_state.events.append({
                "title": title,
                "tag": tag,
                "date": str(date),
                "start": str(start),
                "end": str(end),
                "color": color,
                "note": note
            })
            st.rerun()
        else:
            st.error("請輸入行程主旨")


# =========================
# 6️⃣ 中欄（卡片顯示）
# =========================
with col_center:
    st.subheader("📌 行程看板")

    st.info(f"目前檢視：{calendar_group} / {view_mode}")

    if not st.session_state.events:
        st.warning("目前沒有行程")
    else:
        for ev in st.session_state.events:
            st.markdown(f"""
                <div style="border-left: 6px solid {ev['color']}; padding: 10px;">
                    <span style="background:{ev['color']}22; color:{ev['color']}; padding:2px 6px; border-radius:10px;">
                        {ev['tag']}
                    </span>
                
                    <h4 style="margin:8px 0;">{ev['title']}</h4>
                
                    <p style="margin:0;">
                        📅 {ev['date']}<br>
                        ⏰ {ev['start']} - {ev['end']}
                    </p>
                
                    <p style="margin-top:5px; color:#666;">
                        {ev['note']}
                    </p>
                </div>
                """, unsafe_allow_html=True)


# =========================
# 7️⃣ 右欄（表格）
# =========================
with col_right:
    st.subheader("📊 行程總覽")

    st.dataframe(
        st.session_state.events,
        use_container_width=True
    )
