import streamlit as st
import subprocess

st.set_page_config(page_title="Tự động mở Facebook", page_icon="🌐")

st.title("Công cụ tự động mở Facebook")
st.write("Chương trình này sẽ mở Facebook trên trình duyệt Edge bằng profile hiện tại (đã lưu sẵn tên và mật khẩu).")

if st.button("Mở Facebook trên Edge", type="primary"):
    try:
        # Sử dụng lệnh start của Windows để mở Edge với URL Facebook
        # msedge là lệnh gọi Microsoft Edge trên Windows
        subprocess.Popen(["start", "msedge", "https://www.facebook.com"], shell=True)
        st.success("Đang mở Facebook trên trình duyệt Edge!")
    except Exception as e:
        st.error(f"Có lỗi xảy ra: {e}")
