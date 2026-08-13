import streamlit as st
import pandas as pd 
import os 

FILE_DATA = "danh_sach_khao_sat.csv"

# Tiêu đề trang web
st.title("Xin chào mày đến với ĐỨC ANH HOME")

# CÂU HOỎI 1: Tùy chọn không chọn sẵn (index=None)
tiep_tuc = st.radio(
    "Mày có muốn tiếp tục không?", 
    ["có", "không"], 
    index=None # Không chọn sẵn ô nào
)

# Chỉ khi người dùng bấm chọn "có" hoặc "không" thì mới bắt đầu xử lý
if tiep_tuc == "có":
    
    # CÂU HOỎI 2: Chọn Lớp
    danh_sach_lop = [f"Lớp {i}" for i in range(1, 13)]
    lop = st.selectbox(
        "Mày đang học lớp mấy?", 
        danh_sach_lop, 
        index=None, # Để trống, bắt người dùng phải tự bấm chọn
        placeholder="Bấm vào đây để chọn lớp..."
    )

    # Chỉ khi ĐÃ CHỌN LỚP xong mới hiện câu hỏi tiếp theo
    if lop:
        danh_sach_mon = [
            "Toán", "Ngữ văn", "Tiếng Anh", "Vật lý", 
            "Hóa học", "Sinh học", "Lịch sử", "Địa lý", "Tin học"
        ]
        
        # CÂU HOỎI 3: Chọn Môn học
        mon_hoc = st.selectbox(
            "Môn học yêu thích của mày là gì?", 
            danh_sach_mon, 
            index=None, 
            placeholder="Bấm vào đây để chọn môn..."
        )

        # Chỉ khi ĐÃ CHỌN MÔN HỌC xong mới hiện câu hỏi tiếp theo
        if mon_hoc:
            st.write(f"Mày có chắc là thích học **{mon_hoc}** không?")

            # CÂU HOỎI 4: Điểm số (Mặc định None)
            diem = st.number_input(
                "Điểm số cao nhất của mày là bao nhiêu (0 - 10)?", 
                min_value=0.0, 
                max_value=10.0, 
                value=None, # Không điền sẵn điểm 8.0 nữa
                placeholder="Nhập số điểm từ 0 - 10..."
            )

            # Chỉ khi ĐÃ NHẬP ĐIỂM xong mới hiện Nút Xác Nhận
            if diem is not None:
                    # Đánh giá điểm số
                    if diem < 8.0:
                        st.error("mày nên từ bỏ môn này đi, đồ gà!")
                    else:
                        st.success("mày khá giỏi, mày rất hợp với môn học này")

                    st.info("Cảm ơn vì mày đã chia sẻ")

                    # 1. Gom dữ liệu lại thành 1 dòng bảng
                    du_lieu_moi = pd.DataFrame([{
                        "Lớp": ...,           # <--- Điền tên biến chứa Lớp của cậu vào đây
                        "Môn yêu thích": ..., # <--- Điền tên biến chứa Môn học vào đây
                        "Điểm cao nhất": ...  # <--- Điền tên biến chứa Điểm vào đây
                    }])

                    # 2. Kiểm tra và lưu file:
                    # Nếu FILE_DATA CHƯA tồn tại (dùng os.path.exists):
                    #   -> Lưu file mới có cả cột tiêu đề (du_lieu_moi.to_csv(FILE_DATA, index=False))
                    # Ngược lại (file ĐÃ tồn tại):
                    #   -> Ghi nối tiếp vào cuối file (dùng mode='a', header=False)

elif tiep_tuc == "không":
    st.write("Biến!")
