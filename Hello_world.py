import streamlit as st

# Tiêu đề trang web
st.title("Xin chào mày đến với ĐỨC ANH HOME")

# Hỏi có muốn tiếp tục không?
tiep_tuc = st.radio("Mày có muốn tiếp tục không?", ["có", "không"])

if tiep_tuc == "có":
    # 1. Chọn Lớp (từ lớp 1 đến lớp 12)
    danh_sach_lop = [f"Lớp {i}" for i in range(1, 13)]
    lop = st.selectbox("Mày đang học lớp mấy?", danh_sach_lop)

    # 2. Giới hạn Môn học chính bằng danh sách chọn
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
    mon_hoc = st.selectbox("Môn học yêu thích của mày là gì?", danh_sach_mon)
    st.write(f"Mày có chắc là thích học **{mon_hoc}** không?")

    # 3. Giới hạn Điểm số từ 0.0 đến 10.0
    diem = st.number_input(
        "Điểm số cao nhất của mày là bao nhiêu (0 - 10)?", 
        min_value=0.0, 
        max_value=10.0, 
        value=8.0, 
        step=0.5
    )

    # Nút bấm để gửi thông tin và nhận đánh giá
    if st.button("Xác nhận"):
        st.write(f"Đang học: **{lop}**")
        st.write(f"Môn yêu thích: **{mon_hoc}**")
        st.write(f"Điểm số cao nhất: **{diem}**")

        # 4. Đánh giá điểm số
        if diem < 8:
            st.error("mày nên từ bỏ môn này đi, đồ gà!")
        else:
            st.success("mày khá giỏi, mày rất hợp với môn học này")

        st.info("Cảm ơn vì mày đã chia sẻ")

else:
    st.write("Vậy thôi tạm biệt mày nhé, khi nào rảnh quay lại!")
