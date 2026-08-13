import streamlit as st

st.title("Xin chào mày đến với ĐỨC ANH HOME")

tiep_tuc = st.radio("Mày có muốn tiếp tục không?", ["Có", "Không"])

if tiep_tuc == "Có":
    mon_hoc = st.text_input("Môn học yêu thích của mày là gì?")
    
    if mon_hoc:
        st.write(f"Mày có chắc là thích học **{mon_hoc}** không?")
        
        diem_cao_nhat = st.number_input("Điểm số cao nhất của mày là bao nhiêu?", min_value=0, max_value=10)
        
        if st.button("Xác nhận"):
            if diem_cao_nhat < 8:
                st.warning("Mày quá gà, lêu lêu không nên thích môn học này!")
            else:
                st.success("Giỏi dữ, mày rất có tố chất để học môn này!")
            st.info("Cảm ơn vì mày đã chia sẻ!")
else:
    st.write("Vậy thôi tạm biệt mày nhé, khi nào rảnh quay lại!")
 

    
