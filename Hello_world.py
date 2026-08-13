import streamlit as st

# Tiêu đề trang web
st.title("Xin chào mày đến với ĐỨC ANH HOME")

# Hỏi tiếp tục
tiep_tuc = st.radio("Mày có muốn tiếp tục không?", ["Có", "Không"])

if tiep_tuc == "Có":
    # 1. Danh sách các môn học chính cố định (không cho nhập bậy bạ)
    danh_sach_mon = [
        "Toán", 
        "Ngữ văn", 
        "Tiếng Anh", 
        "Vật lý", 
        "Hóa học", 
        "Sinh học", 
        "Lịch sử", 
        "Địa lý", 
        "Tin học"
    ]
    
    # Dùng selectbox để chọn môn trong danh sách
    mon_hoc = st.selectbox("Chọn môn học yêu thích của mày:", danh_sach_mon)
    st.write(f"Mày có chắc là thích học **{mon_hoc}** không?")
    
    # 2. Ô nhập điểm số GIỚI HẠN từ 0.0 đến 10.0
    diem_cao_nhat = st.number_input(
        "Điểm số cao nhất của mày là bao nhiêu? (Từ 0 đến 10)", 
        min_value=0.0, 
        max_value=10.0, 
        value=8.0, 
        step=0.5
    )
    
    # Nút bấm xác nhận
    if st.button("Xác nhận"):
        if diem_cao_nhat < 8.0:
            st.warning("Mày quá gà, lêu lêu mày không nên thích môn học này!")
        else:
            st.success("Giỏi dữ, mày rất có tố chất để học môn này!")
            
        st.info("Cảm ơn vì mày đã chia sẻ!")

else:
    st.write("Vậy thôi tạm biệt mày nhé, khi nào rảnh quay lại!")

    
