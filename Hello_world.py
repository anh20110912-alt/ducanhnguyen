# Lời chào đầu tiên
print("Xin chào mày đến với ĐỨC ANH HOME")
tiep_tuc = input("mày có muốn tiếp tục không?")

if tiep_tuc == "có":
    # 1. Máy tính đặt câu hỏi và chờ mày nhập kết quả
    mon_hoc = input("Môn học yêu thích của mày là gì? ")

    # 2. Máy tính ghép câu trả lời và in ra màn hình
    print("mày có chắc là thích học", mon_hoc, "không?")

    if tiep_tuc == "có":
        # 3. Điểm số cao nhất của mày 
        diem_cao_nhat = input("Điểm số cao nhất của mày là bao nhiêu? ")
        print ("Điểm số cao nhất của mày là " + diem_cao_nhat)
        diem = int(diem_cao_nhat)
    if diem < 8:
        print ("mày quá gà, lêu lêu mày không nên thích môn học này, đồ gà!")
    if diem >= 8:
        print ("giỏi dữ, mày rất có tố chất để học môn này")

    print ("Cảm vì mày đã chia sẻ")
 

else:
    print("Vậy thôi tạm biệt mày nhé, khi nào rảnh quay lại!")

 

    
