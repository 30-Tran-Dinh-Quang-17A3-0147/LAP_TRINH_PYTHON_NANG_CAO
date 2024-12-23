import numpy as np 
nhiet_do = np.random.uniform(10, 35, size=30)
nhiet_do = np.round(nhiet_do, 2)  
#1
nhiet_do_trung_binh = np.mean(nhiet_do)

print("Dữ liệu nhiệt độ (độ C) trong tháng:", nhiet_do)
print("Nhiệt độ trung bình trong tháng:", round(nhiet_do_trung_binh, 2), )
#2
nhiet_do_cao_nhat_trong_ngay = np.argmax(nhiet_do) + 1
nhiet_do_thap_nhat_trong_ngay = np.argmin(nhiet_do) + 1  

su_chenh_lech_nhiet_do = np.abs(np.diff(nhiet_do))
ngay_bien_doi_cao_nhat = np.argmax(su_chenh_lech_nhiet_do) + 1

print(f"Ngày có nhiệt độ cao nhất: Ngày {nhiet_do_cao_nhat_trong_ngay} với {nhiet_do[nhiet_do_cao_nhat_trong_ngay-1]}")
print(f"Ngày có nhiệt độ thấp nhất: Ngày {nhiet_do_thap_nhat_trong_ngay} với {nhiet_do[nhiet_do_thap_nhat_trong_ngay-1]}")
print(f"Ngày có sự biến đổi nhiệt độ cao nhất: Ngày {ngay_bien_doi_cao_nhat} và {ngay_bien_doi_cao_nhat+1} với chênh lệch {round(su_chenh_lech_nhiet_do[ngay_bien_doi_cao_nhat-1], 2)}")
#3
ngay_co_nhiet_do_tren20 = [i+1 for i, temp in enumerate(nhiet_do) if temp > 20]
nhiet_do_cua_nhung_ngay = {day: round(float(nhiet_do[day-1]), 2) for day in [5, 10, 15, 20, 25]}
nhiet_do_tren_trung_binh = {i+1: round(float(temp), 2) for i, temp in enumerate(nhiet_do) if temp > nhiet_do_trung_binh}
nhiet_do_ngay_chan = {i+1: round(float(nhiet_do[i]), 2) for i in range(len(nhiet_do)) if (i+1) % 2 == 0}
nhiet_do_ngay_le = {i+1: round(float(nhiet_do[i]), 2) for i in range(len(nhiet_do)) if (i+1) % 2 != 0}



print("Các ngày có nhiệt độ cao hơn 20:", ngay_co_nhiet_do_tren20)
print("Nhiệt độ của ngày 5, 10, 15, 20, và 25:", nhiet_do_cua_nhung_ngay)
print("Nhiệt độ của các ngày trên trung bình:", nhiet_do_tren_trung_binh)
print("Nhiệt độ của các ngày chẵn:", nhiet_do_ngay_chan)
print("Nhiệt độ của các ngày lẻ:", nhiet_do_ngay_le)