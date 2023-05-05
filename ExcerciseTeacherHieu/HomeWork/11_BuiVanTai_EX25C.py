import pandas as pd

DF = pd.read_csv('https://raw.githubusercontent.com/anhdung98/diem_thi_2022/main/diem_thi_thpt_2022.csv')
matinh = [(1, "THÀNH PHỐ HÀ NỘI"), (7, 'TỈNH LAI CHÂU'), (12, 'TỈNH THÁI NGUYÊN'), (13, 'TỈNH YÊN BÁI'),
          (15, 'TỈNH PHÚ THỌ'), (16, 'TỈNH VĨNH PHÚC'), (17, 'TỈNH QUẢNG NINH'),
          (18, 'TỈNH BẮC GIANG'), (19, 'TỈNH BẮC NINH'), (8, 'TỈNH LÀO CAI'), (9, 'TỈNH TUYÊN QUANG'),
          (10, ' TỈNH LẠNG SƠN'), (2, "THÀNH PHỐ HỒ CHÍ MINH"), (14, 'TỈNH SƠN LA'),
          (21, 'TỈNH HẢI DƯƠNG'), (22, 'TỈNH HƯNG YÊN'), (24, 'TỈNH HÀ NAM'), (25, 'TỈNH NAM ĐỊNH'),
          (26, 'TỈNH THÁI BÌNH'), (28, 'TỈNH THANH HÓA'), (29, 'TỈNH NGHỆ AN'), (30, 'TỈNH HÀ TĨNH'),
          (31, 'TỈNH QUẢNG BÌNH'), (32, 'TỈNH QUẢNG TRỊ'), (33, 'TỈNH THỪA THIÊN - HUẾ'), (34, ' TỈNH QUẢNG NAM'),
          (35, 'TỈNH QUẢNG NGÃI'), (36, 'TỈNH KON TUM'), (38, 'TỈNH GIA LAI'), (39, 'TỈNH PHÚ YÊN'),
          (40, 'TỈNH ĐẮK LẮK')
    , (41, 'TỈNH KHÁNH HÒA'), (43, 'TỈNH BÌNH PHƯỚC'), (45, 'TỈNH NINH THUẬN'), (46, 'TỈNH TÂY NINH'),
          (47, ' TỈNH BÌNH THUẬN'), (49, 'TỈNH LONG AN'), (50, 'TỈNH ĐỒNG THÁP')
    , (51, 'TỈNH AN GIANG'), (53, 'TỈNH TIỀN GIANG'), (54, 'TỈNH KIÊN GIANG'), (55, 'THÀNH PHỐ CẦN THƠ'),
          (56, 'TỈNH BẾN TRE'), (57, 'TỈNH VĨNH LONG'), (58, 'TỈNH TRÀ VINH'), (59, 'TỈNH SÓC TRĂNG'),
          (60, 'TỈNH BẠC LIÊU')
    , (61, ' TỈNH CÀ MAU'), (62, 'TỈNH ĐIỆN BIÊN'), (63, 'TỈNH ĐĂK NÔNG'), (64, 'TỈNH HẬU GIANG'),
          (11, 'TỈNH BẮC KẠN'), (42, 'TỈNH LÂM ĐỒNG'), (37, 'TỈNH BÌNH ĐỊNH'), (23, 'TỈNH HÒA BÌNH'),
          (48, 'TỈNH ĐỒNG NAI'), (52, 'TỈNH BÀ RỊA – VŨNG TÀU'), (44, 'TỈNH BÌNH DƯƠNG'),
          (3, 'THÀNH PHỐ HẢI PHÒNG'), (4, 'THÀNH PHỐ ĐÀ NẴNG'), (5, 'TỈNH HÀ GIANG'), (6, 'TỈNH CAO BẰNG'),
          (27, 'TỈNH NINH BÌNH')]

'''- Create a data frame df_HCM containing the list of
examinees at Ho Chi Minh City Examination Council, whose first 2 digits of the
registration number (sbd) are "02".'''
DF_HCM = DF[DF.sbd // 1000000 == 2]

'''- Display on the screen the list of all examinees who have the scores of 
mathematics (toan) or literature (ngu_van) higher than 9 in Ho Chi Minh city'''


def display_toan_nguvan_than_9():
    print("1. List of all examinees who have the scores of mathematics (toan) or literature (ngu_van) higher than 9 in Ho Chi Minh city")
    GRADE_THAN_9 = DF_HCM[(DF_HCM.toan > 9) | (DF_HCM.ngu_van > 9)]
    print(GRADE_THAN_9)


def take_name(so):
    for (i, name) in matinh:
        if i == so:
            return name


def top3most_toan():
    print("2. Top province had student math scored 10")
    math10 = []
    for i in range(1, 65):
        local_DF = DF[DF.sbd // 1000000 == i]
        sl = len(local_DF[local_DF.toan == 10])
        math10.append((i, sl))

    top3 = sorted(math10, key=lambda el: el[1])[-3:]
    for (i, sl) in reversed(top3):
        ten_tinh = take_name(i)
        print(f'{ten_tinh}:{sl}')


def average_ngoaingu():
    result = []
    for i in range(1, 65):
        local_DF = DF[DF.sbd // 1000000 == i]
        average_grade = local_DF['ngoai_ngu'].mean()
        result.append((i, average_grade))
    return sorted(result, key=lambda el: el[1])


def top5_lowest_greatest_ngoaingu():
    print("3. Top lowest/greatest foreign language: ")
    sort_ngoaingu = average_ngoaingu()
    top5_lowest_greatestt = sort_ngoaingu[:5] + sort_ngoaingu[-5:]

    for (index, (i, sl)) in enumerate(top5_lowest_greatestt):
        if index == 0:
            print("- Top lowest:")
        if index == 5:
            print("- Top greatest:")
        ten_tinh = take_name(i)
        print(f'{ten_tinh}:{round(sl, 3)}')


def all_average_math():
    sort_ngoaingu = average_ngoaingu()
    for (index, (i, sl)) in enumerate(sort_ngoaingu):
        ten_tinh = take_name(i)
        print(f'{ten_tinh}:{round(sl, 3)}')


if __name__ == "__main__":
    display_toan_nguvan_than_9()
    print("-----------------------------------------------")
    top3most_toan()
    print("-----------------------------------------------")
    top5_lowest_greatest_ngoaingu()
    print("-----------------------------------------------")
    all_average_math()
