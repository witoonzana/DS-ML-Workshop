import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")

st.markdown(''':rainbow[T1977]''')
st.write("Witoon_D")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("💰 ระบบทำความสะอาดข้อมูล Clean โต้ง"):
    st.switch_page("pages/clean_by_T1977.py")
elif st.button("💰 ระบบทำความสะอาดข้อมูล Clean อาจารย์"):
    st.switch_page("pages/clean_app.py")
elif st.button("💰 Customers"):
    st.switch_page("pages/clean_customers.py")
elif st.button("💰 Energy"):
    st.switch_page("pages/energy_inventory.py")
