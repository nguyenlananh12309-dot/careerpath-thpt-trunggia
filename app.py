import streamlit as st
import plotly.graph_objects as go
import random

st.set_page_config(page_title="Hệ thống Hướng nghiệp Cá nhân hóa - THPT Trung Giã", page_icon="🎯", layout="centered")

st.markdown("<h1 style='text-align: left; font-size: 32px;'>🎯 HỆ THỐNG PHẢN HỒI HƯỚNG NGHIỆP<br>CÁ NHÂN HÓA</h1>", unsafe_allow_html=True)
st.write("---")

# ==========================================
# CƠ SỞ DỮ LIỆU ĐIỂM TRÚNG TUYỂN 2026 (6 NHÓM NGÀNH)
# ==========================================
PROGRAM_DATABASE = {
    "Nhóm 1: Khoa học – Kỹ thuật – Công nghệ (STEM & IT)": [
        {"truong":"Đại học Bách khoa Hà Nội (HUST)","nganh":"Khoa học dữ liệu và Trí tuệ nhân tạo","ma_nganh":"IT-E10","to_hop":["A00","A01","B00","D07","K01"],"phuong_thuc":"Điểm thi tốt nghiệp THPT 2026","nam":2026,"diem":29.54,"verified":True,"nguon":"https://ts.hust.edu.vn/vi/tin-tuc/diem-chuan-dai-hoc-bach-khoa-ha-noi-nam-2026","link_truong":"https://hust.edu.vn"},
        {"truong":"Đại học Bách khoa Hà Nội (HUST)","nganh":"Khoa học máy tính","ma_nganh":"IT1","to_hop":["A00","A01","B00","D07","K01"],"phuong_thuc":"Điểm thi tốt nghiệp THPT 2026","nam":2026,"diem":29.27,"verified":True,"nguon":"https://ts.hust.edu.vn/vi/tin-tuc/diem-chuan-dai-hoc-bach-khoa-ha-noi-nam-2026","link_truong":"https://hust.edu.vn"},
        {"truong":"Đại học Bách khoa Hà Nội (HUST)","nganh":"Kỹ thuật Điều khiển - Tự động hoá","ma_nganh":"EE2","to_hop":["A00","A01","B00","D07","K01"],"phuong_thuc":"Điểm thi tốt nghiệp THPT 2026","nam":2026,"diem":28.98,"verified":True,"nguon":"https://ts.hust.edu.vn/vi/tin-tuc/diem-chuan-dai-hoc-bach-khoa-ha-noi-nam-2026","link_truong":"https://hust.edu.vn"},
        {"truong":"Đại học Bách khoa Hà Nội (HUST)","nganh":"Kỹ thuật Điện tử - Viễn thông","ma_nganh":"ET1","to_hop":["A00","A01","B00","D07","K01"],"phuong_thuc":"Điểm thi tốt nghiệp THPT 2026","nam":2026,"diem":28.57,"verified":True,"nguon":"https://ts.hust.edu.vn/vi/tin-tuc/diem-chuan-dai-hoc-bach-khoa-ha-noi-nam-2026","link_truong":"https://hust.edu.vn"},
        {"truong":"Đại học Bách khoa Hà Nội (HUST)","nganh":"Kỹ thuật Cơ điện tử","ma_nganh":"ME1","to_hop":["A00","A01","B00","D07","K01"],"phuong_thuc":"Điểm thi tốt nghiệp THPT 2026","nam":2026,"diem":28.47,"verified":True,"nguon":"https://ts.hust.edu.vn/vi/tin-tuc/diem-chuan-dai-hoc-bach-khoa-ha-noi-nam-2026","link_truong":"https://hust.edu.vn"},
        {"truong":"Đại học Bách khoa Hà Nội (HUST)","nganh":"Chương trình BF-E19","ma_nganh":"BF-E19","to_hop":["A00","A01","B00","D07","K01"],"phuong_thuc":"Điểm thi tốt nghiệp THPT 2026","nam":2026,"diem":20.06,"verified":True,"nguon":"https://ts.hust.edu.vn/vi/tin-tuc/diem-chuan-dai-hoc-bach-khoa-ha-noi-nam-2026","link_truong":"https://hust.edu.vn"},
        {"truong":"Đại học Công nghệ – ĐHQGHN (VNU-UET)","nganh":"Công nghệ thông tin","ma_nganh":"CN1","to_hop":["A00","A01"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":25.00,"verified":True,"nguon":"https://uet.vnu.edu.vn/truong-dai-hoc-cong-nghe-dhqghn-cong-bo-diem-chuan-dai-hoc-chinh-quy-nam-2026/","link_truong":"https://uet.vnu.edu.vn"},
        {"truong":"Đại học Công nghệ – ĐHQGHN (VNU-UET)","nganh":"Kỹ thuật máy tính","ma_nganh":"CN2","to_hop":["A00","A01"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":26.63,"verified":True,"nguon":"https://uet.vnu.edu.vn/truong-dai-hoc-cong-nghe-dhqghn-cong-bo-diem-chuan-dai-hoc-chinh-quy-nam-2026/","link_truong":"https://uet.vnu.edu.vn"},
        {"truong":"Đại học Công nghệ – ĐHQGHN (VNU-UET)","nganh":"Khoa học máy tính","ma_nganh":"CN8","to_hop":["A00","A01"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":26.86,"verified":True,"nguon":"https://uet.vnu.edu.vn/truong-dai-hoc-cong-nghe-dhqghn-cong-bo-diem-chuan-dai-hoc-chinh-quy-nam-2026/","link_truong":"https://uet.vnu.edu.vn"},
        {"truong":"Đại học Công nghệ – ĐHQGHN (VNU-UET)","nganh":"Trí tuệ nhân tạo","ma_nganh":"CN12","to_hop":["A00","A01"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":26.26,"verified":True,"nguon":"https://uet.vnu.edu.vn/truong-dai-hoc-cong-nghe-dhqghn-cong-bo-diem-chuan-dai-hoc-chinh-quy-nam-2026/","link_truong":"https://uet.vnu.edu.vn"},
    ],
    "Nhóm 2: Kinh tế – Quản trị – Tài chính (Business & Finance)": [
        {"truong":"Đại học Kinh tế Quốc dân (NEU)","nganh":n,"ma_nganh":m,"to_hop":["A00","A01","D01","D07"],"phuong_thuc":"Điểm chuẩn quy đổi tương đương năm 2026","nam":2026,"diem":d,"verified":True,"nguon":"https://fit.neu.edu.vn/post/diem-chuan-dai-hoc-chinh-quy-2026-toan-bo-nganh","link_truong":"https://neu.edu.vn"}
        for n,m,d in [
            ("Kinh doanh nông nghiệp","7620114",24.75),("Quản lý công và Chính sách (E-PMP)","EPMP",24.05),
            ("Quản trị kinh doanh","7340101",26.85),("Kế toán","7340301",27.30),
            ("Tài chính - Ngân hàng","7340201",27.43),("Marketing","7340115",27.99),
            ("Kinh doanh quốc tế","7340120",28.50),("Logistics và Quản lý chuỗi cung ứng","7510605",28.53),
            ("Thương mại điện tử","7340122",28.62),("Quản lý nhân lực","7340404",27.25)
        ]
    ],
    "Nhóm 3: Luật – Xã hội – Chính trị (Law & Social Sciences)": [
        {"truong":"Đại học Kinh tế Quốc dân (NEU)","nganh":n,"ma_nganh":m,"to_hop":["A00","A01","D01","D07"],"phuong_thuc":"Điểm chuẩn quy đổi tương đương năm 2026","nam":2026,"diem":d,"verified":True,"nguon":"https://fit.neu.edu.vn/post/diem-chuan-dai-hoc-chinh-quy-2026-toan-bo-nganh","link_truong":"https://neu.edu.vn"}
        for n,m,d in [("Luật","7380101",25.52),("Luật kinh doanh","POHE4",25.68),("Luật kinh tế","7380107",26.62),("Luật thương mại quốc tế","7380109",26.38)]
    ] + [
        {"truong":"Đại học Sư phạm Hà Nội (HNUE)","nganh":n,"ma_nganh":m,"to_hop":["Nhiều tổ hợp"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":d,"verified":True,"nguon":"https://hnue.edu.vn/tin-tuc/12356?page=132","link_truong":"https://hnue.edu.vn"}
        for n,m,d in [("Chính trị học","7310201",23.56),("Xã hội học","7310301",23.75),("Tâm lý học (Tâm lý học trường học)","7310401",24.25),("Tâm lý học giáo dục","7310403",25.62),("Quốc tế học","7310601",25.03),("Việt Nam học","7310630",23.00),("Lịch sử","7229010",27.20)]
    ],
    "Nhóm 4: Y tế – Sức khỏe – Sinh học (Healthcare & Medicine)": [
        {"truong":"Đại học Y Dược – ĐHQGHN","nganh":n,"ma_nganh":m,"to_hop":["B00"],"phuong_thuc":"Điểm chuẩn quy đổi tương đương năm 2026","nam":2026,"diem":d,"verified":True,"nguon":"https://ump.vnu.edu.vn/article-thong-bao-diem-chuan-%28diem-trung-tuyen%29-vao-dai-hoc-chinh-quy-nam-2026-truong-dai-hoc-y-duoc%2C-dai-hoc-quoc-gia-ha-noi-19816-3377.html","link_truong":"https://ump.vnu.edu.vn"}
        for n,m,d in [("Điều dưỡng","7720301",22.76),("Kỹ thuật hình ảnh y học","7720602",22.51),("Kỹ thuật xét nghiệm y học","7720601",23.21),("Dược học","7720201",23.39),("Răng Hàm Mặt","7720501",27.19),("Y khoa","7720101",27.43)]
    ] + [
        {"truong":"Đại học Sư phạm Hà Nội (HNUE)","nganh":n,"ma_nganh":m,"to_hop":["Nhiều tổ hợp"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":d,"verified":True,"nguon":"https://tuyensinh.hnue.edu.vn/thong-bao/698?page=16","link_truong":"https://hnue.edu.vn"}
        for n,m,d in [("Sinh học","7420101",19.00),("Công nghệ sinh học","7420201",19.60),("Hóa học","7440112",24.49),("Hóa học (Hóa dược)","7440112D",22.35)]
    ],
    "Nhóm 5: Sư phạm – Tâm lý & Nhân văn (Education & Humanities)": [
        {"truong":"Đại học Sư phạm Hà Nội (HNUE)","nganh":n,"ma_nganh":m,"to_hop":th,"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":d,"verified":True,"nguon":"https://tuyensinh.hnue.edu.vn/tuyensinh2026/665","link_truong":"https://hnue.edu.vn"}
        for n,m,th,d in [
            # ===== NHÓM NGÀNH KHOA HỌC GIÁO DỤC =====
            ("Giáo dục học (Giáo dục và truyền thông)","7140101",["D01"],24.89),
            ("Quản lí giáo dục","7140114",["D01","C20"],25.65),

            # ===== TẤT CẢ CHƯƠNG TRÌNH ĐÀO TẠO GIÁO VIÊN 2026 =====
            ("Giáo dục Mầm non","7140201",["M00"],23.93),
            ("Giáo dục Mầm non - Sư phạm Tiếng Anh","7140201K",["M01","M02"],22.25),
            ("Giáo dục Tiểu học","7140202",["D01"],28.15),
            ("Giáo dục Tiểu học - Sư phạm Tiếng Anh","7140202K",["D01"],28.42),
            ("Giáo dục Đặc biệt","7140203",["C00","D01"],26.53),
            ("Giáo dục công dân","7140204",["C19","C20","D66"],26.18),
            ("Giáo dục chính trị","7140205",["C19","C20","D66"],26.83),
            ("Giáo dục Thể chất","7140206",["Năng khiếu"],26.63),
            ("Giáo dục Quốc phòng và An ninh","7140208",["C03","C04"],25.41),
            ("Sư phạm Toán học","7140209",["A00","A01"],28.95),
            ("Sư phạm Toán học (dạy Toán bằng tiếng Anh)","7140209K",["A01","D01"],29.00),
            ("Sư phạm Tin học","7140210",["A01","X06"],23.96),
            ("Sư phạm Tin học (dạy Tin học bằng tiếng Anh)","7140210K",["A01","X06"],23.75),
            ("Sư phạm Vật lí","7140211",["A00","A01"],28.77),
            ("Sư phạm Vật lí (dạy Vật lí bằng tiếng Anh)","7140211K",["A00","A01"],28.35),
            ("Sư phạm Hoá học","7140212",["A00","B00"],28.99),
            ("Sư phạm Hoá học (dạy Hóa học bằng tiếng Anh)","7140212K",["D07"],28.22),
            ("Sư phạm Sinh học","7140213",["B00","D08"],28.28),
            ("Sư phạm Ngữ văn","7140217",["C00","D01"],28.71),
            ("Sư phạm Lịch sử","7140218",["C00","D14"],28.61),
            ("Sư phạm Địa lí","7140219",["C00","C04"],28.22),
            ("Sư phạm Âm nhạc","7140221",["Năng khiếu"],24.57),
            ("Sư phạm Mỹ thuật","7140222",["Năng khiếu"],23.43),
            ("Sư phạm Tiếng Anh","7140231",["D01"],27.69),
            ("Sư phạm Tiếng Pháp","7140233",["D01","D03"],20.60),
            ("Sư phạm Công nghệ","7140246",["A00","A01"],23.29),
            ("Sư phạm Khoa học tự nhiên","7140247",["A00","B00"],27.47),
            ("Sư phạm Lịch sử - Địa lí","7140249",["C00"],27.78),

            # ===== CÁC NGÀNH NHÂN VĂN - TÂM LÝ - XÃ HỘI ĐÃ CÓ TRONG CSDL =====
            ("Tiếng Việt và văn hóa Việt Nam","7220101",["C00","D14"],24.53),
            ("Ngôn ngữ Anh","7220201",["D01"],25.57),
            ("Ngôn ngữ Pháp (Tiếng Pháp ứng dụng và giao tiếp quốc tế)","7220203",["D01","D03"],22.25),
            ("Ngôn ngữ Trung Quốc","7220204",["D01","D04"],24.93),
            ("Triết học (Triết học Mác Lê-nin)","7229001",["C00","C19"],24.52),
            ("Lịch sử","7229010",["C00","D14"],27.20),
            ("Văn học","7229030",["C00","D01"],26.43),
            ("Chính trị học","7310201",["C19","C20","D66"],23.56),
            ("Xã hội học","7310301",["C00","C03","D01"],23.75),
            ("Tâm lý học (Tâm lý học trường học)","7310401",["C00","D01"],24.25),
            ("Tâm lý học giáo dục","7310403",["C00","D01"],25.62),
            ("Địa lí học (Địa lí tài nguyên và môi trường)","7310501",["C04","C00"],25.44),
            ("Quốc tế học","7310601",["C00","D14"],25.03),
            ("Việt Nam học","7310630",["C00","D14"],23.00),
            ("Công tác xã hội","7760101",["C00","D01"],22.95),
            ("Hỗ trợ giáo dục người khuyết tật","7760103",["C00","D01"],22.85),
        ]
    ],
    "Nhóm 6: Nghệ thuật – Thiết kế & Sáng tạo (Creative Arts & Design)": [
        {"truong":"Đại học Kiến trúc Hà Nội (HAU)","nganh":"Thiết kế đồ họa","ma_nganh":"7210403","to_hop":["Năng khiếu"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":23.47,"verified":True,"nguon":"https://www.hau.edu.vn/thong-tin-hoat-dong_c0706/Thong-bao-ve-diem-trung-tuyen-dai-hoc-hinh-thuc-chinh-quy-nam-2026-doi-voi-nhom-nganh-va-cac-nganhchuyen-nganh-xet-tuyen-doc-lap_n4794.html","link_truong":"https://hau.edu.vn"},
        {"truong":"Đại học Kiến trúc Hà Nội (HAU)","nganh":"Nghệ thuật số","ma_nganh":"7210403_1","to_hop":["Năng khiếu"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":24.00,"verified":True,"nguon":"https://www.hau.edu.vn/thong-tin-hoat-dong_c0706/Thong-bao-ve-diem-trung-tuyen-dai-hoc-hinh-thuc-chinh-quy-nam-2026-doi-voi-nhom-nganh-va-cac-nganhchuyen-nganh-xet-tuyen-doc-lap_n4794.html","link_truong":"https://hau.edu.vn"},
        {"truong":"Đại học Kiến trúc Hà Nội (HAU)","nganh":"Thiết kế thời trang","ma_nganh":"7210404","to_hop":["Năng khiếu"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":22.50,"verified":True,"nguon":"https://www.hau.edu.vn/thong-tin-hoat-dong_c0706/Thong-bao-ve-diem-trung-tuyen-dai-hoc-hinh-thuc-chinh-quy-nam-2026-doi-voi-nhom-nganh-va-cac-nganhchuyen-nganh-xet-tuyen-doc-lap_n4794.html","link_truong":"https://hau.edu.vn"},
        {"truong":"Đại học Kiến trúc Hà Nội (HAU)","nganh":"Thiết kế nội thất","ma_nganh":"7580108","to_hop":["Năng khiếu"],"phuong_thuc":"Điểm trúng tuyển đại học chính quy 2026","nam":2026,"diem":22.75,"verified":True,"nguon":"https://www.hau.edu.vn/thong-tin-hoat-dong_c0706/Thong-bao-ve-diem-trung-tuyen-dai-hoc-hinh-thuc-chinh-quy-nam-2026-doi-voi-nhom-nganh-va-cac-nganhchuyen-nganh-xet-tuyen-doc-lap_n4794.html","link_truong":"https://hau.edu.vn"},
    ],
}


def loc_nganh_tham_khao(danh_sach, to_hop_hs, cho_phep_nang_khieu=True):
    ket_qua = []
    for item in danh_sach:
        if not item.get("verified", False):
            continue
        combos = item.get("to_hop", [])
        if "Nhiều tổ hợp" in combos or to_hop_hs in combos or (cho_phep_nang_khieu and "Năng khiếu" in combos):
            ket_qua.append(item)
    return ket_qua

def chon_10_lua_chon_phu_diem(danh_sach, so_luong=10):
    ds = sorted(danh_sach, key=lambda x: x["diem"])
    if len(ds) <= so_luong:
        return ds

    idxs = []
    for i in range(so_luong):
        idx = round(i * (len(ds) - 1) / (so_luong - 1))
        if idx not in idxs:
            idxs.append(idx)
    return [ds[i] for i in idxs]

def phan_loai_nganh(danh_sach, diem_hs):
    sorted_ds = sorted(danh_sach, key=lambda x: x["diem"], reverse=True)
    tham_khao_cao = []
    tuong_duong = []
    tham_khao_thap = []

    for nganh in sorted_ds:
        chenh_lech = nganh["diem"] - diem_hs
        if chenh_lech > 1.5:
            tham_khao_cao.append(nganh)
        elif chenh_lech >= -1.5:
            tuong_duong.append(nganh)
        else:
            tham_khao_thap.append(nganh)

    return tham_khao_cao, tuong_duong, tham_khao_thap

def hien_thi_danh_sach_nganh(tieu_de, danh_sach, diem_hs):
    st.markdown(f"**{tieu_de}**")
    if not danh_sach:
        st.write("*Chưa có bản ghi ngành phù hợp với tổ hợp/phương thức đang chọn trong cơ sở dữ liệu thử nghiệm.*")
        return
    for i, item in enumerate(danh_sach, 1):
        chenh_lech = item["diem"] - diem_hs
        dau = "+" if chenh_lech >= 0 else ""
        st.markdown(
            f"{i}. **{item['nganh']}** — {item['truong']}  \n"
            f"   - Mã ngành: `{item['ma_nganh']}` | Tổ hợp: `{', '.join(item['to_hop'])}` | Phương thức: {item['phuong_thuc']}  \n"
            f"   - Điểm tham khảo **{item['diem']:.2f}** ({item['nam']}) | Điểm của bạn: **{diem_hs:.2f}** | Chênh lệch: **{dau}{chenh_lech:.2f}**  \n"
            f"   - [Nguồn dữ liệu]({item['nguon']}) · [Website trường]({item['link_truong']})"
        )

def lay_diem_lua_chon(selected_str):
    if selected_str.startswith("A."): return 1
    elif selected_str.startswith("B."): return 2
    elif selected_str.startswith("C."): return 3
    elif selected_str.startswith("D."): return 4
    elif selected_str.startswith("E."): return 5
    return 3

FACTOR_LABELS = {
    "noi_luc": "Cá nhân / Nội lực",
    "gia_dinh": "Gia đình",
    "nha_truong": "Nhà trường",
    "xa_hoi": "Truyền thông & môi trường xã hội",
    "trai_nghiem": "Trải nghiệm nghề nghiệp"
}

def muc_do_tham_khao(score):
    if score >= 4.0:
        return "Cao", "Đây là một điểm tựa đáng chú ý trong hồ sơ hiện tại."
    elif score >= 3.0:
        return "Trung bình", "Yếu tố này đang ở mức tương đối và còn có thể được củng cố."
    return "Cần củng cố", "Đây là yếu tố nên được quan tâm trước khi đưa ra quyết định dài hạn."

def tao_ho_so_ca_nhan(data):
    factors = {
        "noi_luc": data.get("noi_luc", 3.0),
        "gia_dinh": data.get("gia_dinh", 3.0),
        "nha_truong": data.get("nha_truong", 3.0),
        "xa_hoi": data.get("xa_hoi", 3.0),
        "trai_nghiem": data.get("trai_nghiem", 3.0)
    }
    ranked = sorted(factors.items(), key=lambda x: x[1], reverse=True)
    strengths = ranked[:2] if len(ranked) >= 2 else [("noi_luc", 3.0), ("gia_dinh", 3.0)]
    priorities = sorted(factors.items(), key=lambda x: x[1])[:2] if len(ranked) >= 2 else [("noi_luc", 3.0), ("gia_dinh", 3.0)]
    return strengths, priorities

def goi_y_hanh_dong(data, grade):
    actions = []
    nl = data.get("noi_luc", 3.0)
    nt = data.get("nha_truong", 3.0)
    gd = data.get("gia_dinh", 3.0)
    tn = data.get("trai_nghiem", 3.0)
    xh = data.get("xa_hoi", 3.0)
    
    if nl >= 4.0 and nt < 3.5:
        actions.append("Đối chiếu lại các môn học/tổ hợp xét tuyển liên quan và xây dựng kế hoạch củng cố môn nền tảng.")
    if nl >= 4.0 and gd < 3.5:
        actions.append("Trao đổi với gia đình về học phí, thời gian đào tạo, địa điểm học và các phương án hỗ trợ tài chính trước khi chốt lựa chọn.")
    if nl >= 4.0 and tn < 3.5:
        actions.append("Thực hiện ít nhất một trải nghiệm thực tế: phỏng vấn người đang làm nghề, tham quan nơi làm việc, CLB/dự án hoặc hoạt động trải nghiệm liên quan.")
    if nt < 3.0:
        actions.append("Tìm thêm thông tin từ giáo viên bộ môn, giáo viên chủ nhiệm hoặc hoạt động hướng nghiệp của trường để kiểm chứng năng lực học tập.")
    if xh < 3.0:
        actions.append("Mở rộng nguồn thông tin nghề nghiệp: đọc mô tả công việc, yêu cầu tuyển dụng và trao đổi với người có kinh nghiệm thay vì chỉ dựa vào hình mẫu trên mạng xã hội.")
    if tn < 3.0:
        actions.append("Ưu tiên trải nghiệm trước khi quyết định: một hoạt động thực tế có thể giúp kiểm chứng hình dung của bạn về công việc.")
    
    if not actions:
        if data.get("overall", 3.0) >= 4.0:
            actions.append("Tiếp tục kiểm chứng lựa chọn bằng trải nghiệm thực tế và đối chiếu yêu cầu tuyển sinh của một số chương trình đào tạo cụ thể.")
        elif data.get("overall", 3.0) >= 3.0:
            actions.append("Chọn 1–2 yếu tố có điểm thấp nhất để cải thiện, sau đó thực hiện lại đánh giá khi có thêm thông tin hoặc trải nghiệm mới.")
        else:
            actions.append("Chưa nên vội chốt lựa chọn. Hãy ưu tiên tìm hiểu bản thân, yêu cầu ngành học và trải nghiệm thực tế trước khi quyết định.")

    if grade == "Khối 10":
        actions.append("Hãy ưu tiên khám phá và tích lũy trải nghiệm; chưa cần xem kết quả này như một quyết định cuối cùng.")
    elif grade == "Khối 11":
        actions.append("Hãy bắt đầu thu hẹp lựa chọn và đối chiếu với tổ hợp môn, phương thức tuyển sinh và điều kiện gia đình.")
    else:
        actions.append("Hãy ưu tiên kiểm tra yêu cầu tuyển sinh hiện hành và lập phương án lựa chọn trường phù hợp với dữ liệu học tập thực tế.")
    return actions[:5]

def tao_phan_hoi_ro_rang(data, grp, grade):
    """Tạo phản hồi hành động ngắn, cụ thể từ chính hồ sơ 5 yếu tố."""
    factors = {
        "noi_luc": data.get("noi_luc", 3.0),
        "gia_dinh": data.get("gia_dinh", 3.0),
        "nha_truong": data.get("nha_truong", 3.0),
        "xa_hoi": data.get("xa_hoi", 3.0),
        "trai_nghiem": data.get("trai_nghiem", 3.0)
    }
    priorities = sorted(factors.items(), key=lambda x: x[1])[:2]
    strengths = sorted(factors.items(), key=lambda x: x[1], reverse=True)[:2]

    advice = []
    p1, p2 = priorities

    action_map = {
        "noi_luc": (
            "🔹 Củng cố nền tảng cá nhân",
            "Đối chiếu lại sở thích, năng lực học tập và các môn nền tảng của nhóm ngành đang quan tâm. Chọn 1–2 môn hoặc kỹ năng cần cải thiện và đặt một mục tiêu cụ thể trong 4–8 tuần tới."
        ),
        "gia_dinh": (
            "🔹 Làm rõ sự đồng thuận và điều kiện gia đình",
            "Trao đổi với cha mẹ về ngành đang cân nhắc theo 3 nội dung: mong muốn của bạn, điều kiện học tập – tài chính và những phương án thay thế. Mục tiêu là có thêm thông tin để tự đưa ra quyết định, không chỉ làm theo hoặc phản đối định hướng của gia đình."
        ),
        "nha_truong": (
            "🔹 Tăng khai thác nguồn hỗ trợ từ nhà trường",
            "Chủ động hỏi giáo viên bộ môn, giáo viên chủ nhiệm hoặc cán bộ phụ trách hướng nghiệp; đồng thời tham gia một hoạt động hướng nghiệp, ngày hội tuyển sinh, CLB hoặc trải nghiệm liên quan đến nhóm ngành đang cân nhắc."
        ),
        "xa_hoi": (
            "🔹 Kiểm chứng thông tin nghề nghiệp",
            "Tìm hiểu mô tả công việc, yêu cầu tuyển dụng, môi trường làm việc và xu hướng của ngành từ nhiều nguồn đáng tin cậy. Không nên chỉ dựa vào hình mẫu, video hoặc xu hướng trên mạng xã hội."
        ),
        "trai_nghiem": (
            "🔹 Tăng trải nghiệm trước khi chốt lựa chọn",
            "Ưu tiên ít nhất một hoạt động có tiếp xúc thực tế với lĩnh vực này: phỏng vấn người đang học/làm nghề, tham quan môi trường làm việc, tham gia CLB/dự án, workshop hoặc hoạt động trải nghiệm. Sau đó tự ghi lại điều bạn thích, không thích và điều còn muốn tìm hiểu."
        )
    }

    for key, score in priorities:
        title, text = action_map[key]
        if score < 3.0:
            advice.append((title, text))
        elif score < 3.5:
            advice.append((title, text))

    # Nếu hai yếu tố thấp nhất đều từ 3.5 trở lên, chuyển trọng tâm sang kiểm chứng lựa chọn.
    if not advice:
        advice.append((
            "🔹 Kiểm chứng lựa chọn bằng trải nghiệm",
            "Các nhóm yếu tố hiện tương đối cân bằng. Thay vì chỉ dựa vào điểm tổng, hãy chọn một hoạt động thực tế liên quan đến nhóm ngành và đối chiếu lại kết quả sau khi có thêm trải nghiệm."
        ))

    # Một lời nhắc dựa trên điểm tựa cao nhất.
    strong_key, strong_score = strengths[0]
    strong_action = {
        "noi_luc": "Bạn có thể tận dụng điểm tựa cá nhân hiện có để chủ động thử sức bằng một nhiệm vụ hoặc sản phẩm cụ thể liên quan đến nhóm ngành.",
        "gia_dinh": "Bạn có thể tận dụng sự hỗ trợ từ gia đình để cùng tìm hiểu học phí, môi trường đào tạo và các lựa chọn ngành/trường cụ thể.",
        "nha_truong": "Bạn có thể tận dụng các nguồn lực ở trường như giáo viên, CLB và hoạt động hướng nghiệp để kiểm chứng lựa chọn.",
        "xa_hoi": "Bạn có thể tận dụng nguồn thông tin xã hội nhưng nên đối chiếu giữa nhiều nguồn trước khi hình thành kết luận.",
        "trai_nghiem": "Bạn đã có nền tảng trải nghiệm tương đối tốt; hãy ghi lại những trải nghiệm thực sự khiến bạn hứng thú hoặc không phù hợp để thu hẹp lựa chọn."
    }[strong_key]
    advice.append(("💡 Tận dụng điểm tựa nổi bật", strong_action))

    # Điều chỉnh bước tiếp theo theo khối lớp.
    grade_action = {
        "Khối 10": "Hãy ưu tiên khám phá và trải nghiệm, chưa cần xem kết quả này như quyết định cuối cùng.",
        "Khối 11": "Hãy bắt đầu thu hẹp lựa chọn và đối chiếu với tổ hợp môn, điều kiện gia đình và yêu cầu tuyển sinh.",
        "Khối 12": "Hãy ưu tiên kiểm tra thông tin tuyển sinh hiện hành và chuyển kết quả thành danh sách ngành/trường để tiếp tục cân nhắc."
    }[grade]
    advice.append(("📍 Bước tiếp theo", grade_action))
    return advice[:4]


def hien_thi_ho_so_tong_quan(data, grp, grade):
    strengths, priorities = tao_ho_so_ca_nhan(data)
    st.markdown("### 🧭 Hồ sơ tương thích của bạn")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**💪 Hai điểm tựa nổi bật**")
        for key, score in strengths:
            level, desc = muc_do_tham_khao(score)
            st.write(f"• **{FACTOR_LABELS[key]}:** {score:.2f}/5 — {level}")
    with c2:
        st.markdown("**🎯 Hai yếu tố nên ưu tiên**")
        for key, score in priorities:
            level, desc = muc_do_tham_khao(score)
            st.write(f"• **{FACTOR_LABELS[key]}:** {score:.2f}/5 — {level}")

    if strengths and priorities:
        gap = strengths[0][1] - priorities[0][1]
        if gap >= 1.0:
            st.info(f"🔎 **Điểm cần chú ý:** hồ sơ của bạn có độ chênh {gap:.2f} điểm giữa điểm tựa cao nhất và yếu tố thấp nhất. Vì vậy, kết quả không chỉ cho biết điểm mạnh mà còn chỉ ra nơi bạn nên tập trung hành động tiếp theo.")
        else:
            st.success("🔎 **Hồ sơ khá cân bằng:** các nhóm yếu tố không chênh lệch lớn. Bước tiếp theo nên là kiểm chứng lựa chọn bằng trải nghiệm và thông tin thực tế.")

    st.markdown("### 💬 Phản hồi cá nhân hóa: Bạn nên làm gì tiếp theo?")
    st.caption("Các khuyến nghị dưới đây được tạo từ hai yếu tố có điểm thấp nhất, hai điểm tựa nổi bật và khối lớp của bạn.")
    for title, text in tao_phan_hoi_ro_rang(data, grp, grade):
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.write(text)

# ==========================================
# PHẦN 1: THÔNG TIN CƠ BẢN VÀ ĐIỀU HƯỚNG PHÂN NHÁNH
# ==========================================
st.header("PHẦN 1: Thông tin cơ bản & Phân luồng")
name = st.text_input("Câu 01: Họ và tên của bạn:")
grade = st.selectbox("Câu 02: Khối lớp đang theo học:", ["Khối 10", "Khối 11", "Khối 12"])

routing_choice = st.radio(
    "Câu 03: Tình trạng định hướng nghề nghiệp hiện tại của bạn:",
    (
        "A. Chưa có định hướng cụ thể: Bạn cảm thấy mơ hồ, chưa biết mình phù hợp với lĩnh vực nào.",
        "B. Đang phân vân giữa một số nhóm ngành: Bạn đã có một vài lựa chọn nhưng chưa thể đưa ra quyết định dứt khoát.",
        "C. Đã xác định rõ một nhóm ngành mục tiêu: Bạn đã có mục tiêu cụ thể và muốn kiểm chứng mức độ khả thi cùng các rào cản thực tế."
    )
)

st.write("---")

# ==========================================
# MODULE THÔNG TIN TỔ HỢP XÉT TUYỂN & ĐIỂM SỐ
# ==========================================
student_data = {}
if grade in ["Khối 10", "Khối 11", "Khối 12"]:
    st.subheader("📌 Thông tin bổ trợ chiến lược xét tuyển Đại học & Tổ hợp môn")
    
    to_hop = st.selectbox(
        "Lựa chọn tổ hợp môn dự kiến xét tuyển chính:",
        (
            "A00 (Toán, Vật lý, Hóa học)",
            "A01 (Toán, Vật lý, Tiếng Anh)",
            "A02 (Toán, Vật lý, Sinh học)",
            "B00 (Toán, Hóa học, Sinh học)",
            "B08 (Toán, Sinh học, Tiếng Anh)",
            "C00 (Ngữ văn, Lịch sử, Địa lý)",
            "C01 (Ngữ văn, Toán, Vật lý)",
            "C02 (Ngữ văn, Toán, Hóa học)",
            "C03 (Ngữ văn, Toán, Lịch sử)",
            "C04 (Ngữ văn, Toán, Địa lý)",
            "D01 (Toán, Ngữ văn, Tiếng Anh)",
            "D07 (Toán, Hóa học, Tiếng Anh)",
            "D08 (Toán, Sinh học, Tiếng Anh)",
            "D09 (Toán, Lịch sử, Tiếng Anh)",
            "D10 (Toán, Địa lý, Tiếng Anh)",
            "Khác (Tổ hợp tự chọn chuyên biệt)"
        )
    )

    custom_to_hop = ""
    if to_hop.startswith("Khác"):
        st.info("💡 Bạn có thể nhập trực tiếp mã tổ hợp nếu tổ hợp của mình chưa có trong danh sách trên, ví dụ: C03, D14, C19...")
        custom_to_hop = st.text_input(
            "Nhập mã tổ hợp xét tuyển của bạn:",
            placeholder="Ví dụ: C03",
            max_chars=30
        ).strip().upper()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        m1_score = st.number_input("Điểm TB môn 1 (Thang 10):", min_value=0.0, max_value=10.0, value=8.0, step=0.1)
    with col2:
        m2_score = st.number_input("Điểm TB môn 2 (Thang 10):", min_value=0.0, max_value=10.0, value=8.0, step=0.1)
    with col3:
        m3_score = st.number_input("Điểm TB môn 3 (Thang 10):", min_value=0.0, max_value=10.0, value=8.0, step=0.1)
    
    avg_to_hop = m1_score + m2_score + m3_score
    st.markdown(f"👉 **Tổng điểm tổ hợp quy đổi (Thang điểm 30):** `{round(avg_to_hop, 2)} điểm`")
    
    final_to_hop = custom_to_hop if (to_hop.startswith("Khác") and custom_to_hop) else to_hop.split()[0]
    
    student_data = {
        "to_hop": final_to_hop,
        "avg_to_hop": avg_to_hop
    }
    st.write("---")

GROUPS = [
    "Nhóm 1: Khoa học – Kỹ thuật – Công nghệ (STEM & IT)",
    "Nhóm 2: Kinh tế – Quản trị – Tài chính (Business & Finance)",
    "Nhóm 3: Luật – Xã hội – Chính trị (Law & Social Sciences)",
    "Nhóm 4: Y tế – Sức khỏe – Sinh học (Healthcare & Medicine)",
    "Nhóm 5: Sư phạm – Tâm lý & Nhân văn (Education & Humanities)",
    "Nhóm 6: Nghệ thuật – Thiết kế & Sáng tạo (Creative Arts & Design)"
]

selected_target_groups = []


# ==========================================
# PHẦN 2.1: SÀNG LỌC NHANH XU HƯỚNG HÀNH VI
# ==========================================
if routing_choice.startswith("A"):
    st.header("PHẦN 2.1: Sàng lọc nhanh xu hướng hành vi ")
    
    s1_opt = st.radio("Câu S1: Khi đối mặt với một thiết bị điện tử bị hỏng, một bài toán logic hóc búa hoặc một phần mềm bị lỗi cần mày mò, phản xạ tự nhiên của bạn là: ", (
        "A. Thấy phiền phức, lập tức bỏ qua hoặc né tránh.",
        "B. Cất đi, chờ đợi người khác làm hộ chứ không tự chạm vào.",
        "C. Tò mò xem qua một chút nhưng rất nhanh nản nếu thấy phức tạp.",
        "D. Tự lên mạng tìm kiếm video hướng dẫn hoặc bài viết để làm theo từng bước.",
        "E. Cực kỳ hào hứng tự tay tháo lắp, viết mã lệnh (code) hoặc kiên trì thử nhiều cách để tìm ra nguyên nhân đến cùng."
    ), key="s1_radio")
    s1 = lay_diem_lua_chon(s1_opt)

    s2_opt = st.radio("Câu S2: Khi tham gia một hoạt động tập thể có tính chất buôn bán, gây quỹ hoặc cần điều phối nguồn lực/sự kiện, xu hướng của bạn là: ", (
        "A. Né tránh các hoạt động liên quan đến tiền bạc, tính toán hay buôn bán.",
        "B. Chỉ nhận các công việc hậu cần chân tay đơn giản theo sự chỉ định.",
        "C. Tham gia phụ giúp bán hàng hoặc điều phối cho vui, không để tâm hiệu quả.",
        "D. Tự tin ra mặt tiếp thị, chào hàng, thương lượng và thuyết phục người mua.",
        "E. Chủ động lập kế hoạch kinh doanh, tính toán giá thành, quản lý dòng tiền và tìm cách tối ưu hóa lợi nhuận."
    ), key="s2_radio")
    s2 = lay_diem_lua_chon(s2_opt)

    s3_opt = st.radio("Câu S3: Khi chứng kiến một vụ việc tranh luận xã hội, các quy định chưa thỏa đáng hoặc vấn đề công bằng trong tập thể, thái độ của bạn là: ", (
        "A. Hoàn toàn thờ ơ, không bận tâm đến những chuyện xung quanh.",
        "B. Lướt qua đọc các bình luận cho vui, không suy nghĩ sâu xa.",
        "C. Nắm bắt thông tin bề nổi nhưng ngại nêu quan điểm cá nhân.",
        "D. Quan tâm đến phản ứng và cảm xúc của các bên liên quan để đưa ra góc nhìn hòa giải.",
        "E. Đi sâu tìm hiểu các quy định, văn bản pháp lý, rà soát lập luận logic của từng bên để phân tích đúng – sai và lên tiếng bảo vệ sự công bằng."
    ), key="s3_radio")
    s3 = lay_diem_lua_chon(s3_opt)

    s4_opt = st.radio("Câu S4: Khi chứng kiến người khác bị thương tích, ốm đau hoặc khi nghĩ đến việc chăm sóc thể chất, sức khỏe con người, bạn cảm thấy: ", (
        "A. Sợ hãi (sợ máu, vết thương, mùi thuốc), tìm cách né tránh việc chăm sóc.",
        "B. Cảm thấy lúng túng, không biết phải xử trí thế nào ngoài việc gọi người khác.",
        "C. Chỉ hỗ trợ những việc vặt bên ngoài khi được người lớn yêu cầu.",
        "D. Cẩn thận giúp đỡ việc cho uống thuốc, chăm sóc cơ bản theo hướng dẫn có sẵn.",
        "E. Giữ được bình tĩnh, tỉ mỉ sơ cứu, chăm sóc chu đáo và thôi thúc mong muốn hiểu sâu về cơ chế cơ thể để chữa trị."
    ), key="s4_radio")
    s4 = lay_diem_lua_chon(s4_opt)

    s5_opt = st.radio("Câu S5: Khi có người cần bạn giảng giải một bài học khó, hoặc khi bạn bè gặp chuyện buồn bã, bế tắc tâm lý, phản ứng của bạn là: ", (
        "A. Cảm thấy phiền hà, từ chối lắng nghe hoặc không muốn giải thích cho người khác.",
        "B. Lắng nghe hoặc giải thích qua loa cho xong chuyện.",
        "C. Động viên bằng những câu an ủi chung chung, hướng dẫn bài ở mức cơ bản.",
        "D. Cố gắng dành thời gian lắng nghe và khuyên nhủ hoặc hướng dẫn trong khả năng của mình.",
        "E. Cực kỳ kiên nhẫn lắng nghe, thấu cảm sâu sắc, hào hứng tìm cách diễn đạt trực quan để người khác hiểu bài hoặc giúp họ tháo gỡ nút thắt tâm lý."
    ), key="s5_radio")
    s5 = lay_diem_lua_chon(s5_opt)

    s6_opt = st.radio("Câu S6: Khi cần làm một bài thuyết trình, vẽ sơ đồ, trang trí không gian hoặc làm một sản phẩm sáng tạo, xu hướng của bạn là: ", (
        "A. Cực kỳ ngại, cảm thấy bản thân hoàn toàn không có khả năng thẩm mỹ.",
        "B. Làm đại khái, cốt xong việc, chỉ cần đủ nội dung chữ chứ không cần hình thức.",
        "C. Sử dụng các mẫu (template) có sẵn trên mạng mà không chỉnh sửa gì nhiều.",
        "D. Tự tìm cách chọn màu sắc, kiểu chữ và bố cục sao cho ưa nhìn, sạch đẹp.",
        "E. Tự tay thiết kế tỉ mỉ, sáng tạo bố cục, hình ảnh mang phong cách và dấu ấn thẩm mỹ riêng biệt."
    ), key="s6_radio")
    s6 = lay_diem_lua_chon(s6_opt)

    if st.button("Xác định 2 nhóm ngành tiềm năng nhất"):
        if not name.strip():
            st.warning("Vui lòng nhập Họ và tên ở Phần 1!")
        elif s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0 or s5 == 0 or s6 == 0:
            st.warning("⚠️ Vui lòng trả lời đầy đủ tất cả các câu hỏi sàng lọc trước khi tiếp tục!")
        else:
            screening_scores = {
                GROUPS[0]: s1,
                GROUPS[1]: s2,
                GROUPS[2]: s3,
                GROUPS[3]: s4,
                GROUPS[4]: s5,
                GROUPS[5]: s6
            }
            
            sorted_s = sorted(screening_scores.items(), key=lambda x: x[1], reverse=True)
            highest_score = sorted_s[0][1]
            top_groups = [g for g, score in sorted_s if score == highest_score]
            
            if len(top_groups) == 2:
                st.session_state['target_groups'] = top_groups
                st.success(f"Hệ thống phát hiện 2 nhóm ngành có điểm số cao nhất và đồng đều nhất: **{top_groups[0]}** và **{top_groups[1]}**")
            elif len(top_groups) == 1:
                second_highest_score = sorted_s[1][1]
                second_groups = [g for g, score in sorted_s if score == second_highest_score]
                st.session_state['target_groups'] = [top_groups[0], second_groups[0]]
                st.success(f"Hệ thống đã chọn lọc ra 2 nhóm ngành phù hợp nhất: **{top_groups[0]}** và **{top_groups[1]}**")
            else:
                st.session_state['target_groups'] = top_groups[:2] # Tự động lấy tối đa 2 nhóm nếu điểm bằng nhau hàng loạt

elif routing_choice is not None and routing_choice.startswith("B"):
    st.header("PHẦN 2.2: Chọn nhóm ngành phân vân")
    chosen_b = st.multiselect("Chọn tối đa 2 nhóm ngành bạn đang phân vân:", GROUPS, max_selections=2)
    if chosen_b:
        st.session_state['target_groups'] = chosen_b

elif routing_choice is not None and routing_choice.startswith("C"):
    st.header("PHẦN 2.2: Chọn nhóm ngành mục tiêu")
    target = st.selectbox("Chọn nhóm ngành mục tiêu của bạn:", GROUPS)
    if target:
        st.session_state['target_groups'] = [target]

st.write("---")

# ==========================================
# PHẦN 2.2 & PHẦN 3: MA TRẬN KHẢO SÁT CHUYÊN SÂU
# ==========================================
# Đồng bộ hóa dữ liệu từ session_state để hiển thị ma trận chuyên sâu
selected_target_groups = st.session_state.get('target_groups', [])
if selected_target_groups:
    st.header("PHẦN 2.2: Ma trận khảo sát chuyên sâu")
    
    group_report_data = {}
    
    for grp in selected_target_groups:
        st.subheader(f"📌 Đánh giá chi tiết cho: {grp}")
        
        if "Nhóm 1" in grp:
            q1_title = "T1.1: Trong thời gian rảnh hoặc khi làm việc nhóm, bạn có thói quen tự tay mày mò chế tạo mô hình, lắp ráp linh kiện, hoặc tự viết các đoạn mã/thuật toán không?"
            q1_opts = (
                "A. Không bao giờ, cảm thấy xa lạ hoặc không có hứng thú với việc mày mò máy móc.",
                "B. Rất hiếm khi, chỉ làm khi bị bắt buộc hoặc có người khác giao việc cụ thể.",
                "C. Thỉnh thoảng có làm theo các hướng dẫn có sẵn trên mạng nhưng không duy trì thường xuyên.",
                "D. Thường xuyên tự tìm tòi, lắp ráp các mô hình đơn giản hoặc tự viết các đoạn mã nhỏ khi có thời gian rảnh.",
                "E. Rất thường xuyên và cực kỳ thích thú, chủ động tự mày mò nghiên cứu các linh kiện mới hoặc tự phát triển các đoạn mã/thuật toán phức tạp."
            )
            q2_title = "T1.2: Khi đối mặt với một bài toán tư duy không gian, logic phức tạp hoặc lỗi kỹ thuật chưa tìm ra giải pháp, thái độ của bạn là gì?"
            q2_opts = (
                "A. Dễ nản lòng, bỏ cuộc ngay hoặc lập tức nhờ người khác làm thay.",
                "B. Cảm thấy bối rối, loay hoay một lúc rồi chuyển sang việc khác nếu thấy quá khó.",
                "C. Cố gắng tìm hiểu thêm một chút nhưng nếu tốn quá nhiều thời gian thì sẽ gác lại.",
                "D. Suy nghĩ tìm hướng giải quyết thay thế, hỏi bạn bè hoặc tra cứu tài liệu để tháo gỡ nút thắt.",
                "E. Tập trung cao độ, kiên trì thử nghiệm nhiều phương án khác nhau đến khi tìm ra giải pháp và khắc phục triệt để."
            )
            q3_title = "T1.3: Khả năng làm việc độc lập, kiên trì ngồi hàng giờ liền trước máy móc/màn hình để hoàn thành một nhiệm vụ đòi hỏi độ chính xác cao của bạn ở mức nào?"
            q3_opts = (
                "A. Rất kém, nhanh chán, dễ bị phân tâm bởi các yếu tố xung quanh sau vài phút.",
                "B. Hơi khó tập trung lâu, thường phải nghỉ giải lao liên tục giữa chừng.",
                "C. Có thể duy trì sự tập trung ở mức trung bình nếu đó là nhiệm vụ bắt buộc phải hoàn thành.",
                "D. Khá tốt, có khả năng tập trung làm việc độc lập trong thời gian tương đối dài để hoàn thành sản phẩm.",
                "E. Rất tốt, có thể tập trung sâu và say sưa làm việc độc lập hàng giờ liền mà không thấy mệt mỏi."
            )
            q4_text = "T1.4: Cha mẹ và người thân tôn trọng, đồng thuận hoặc chủ động định hướng tôi theo đuổi lĩnh vực khoa học – kỹ thuật – công nghệ."
            q5_text = "T1.5: Điều kiện kinh tế gia đình đáp ứng tốt mức học phí và các chi phí trang thiết bị học tập (máy tính cấu hình cao, vật liệu thực hành) của khối ngành này."
            q6_text = "T1.6: Điểm số và khả năng tiếp thu các môn học Toán, Vật lý, Hóa học hoặc Tin học là thế mạnh nổi trội của tôi so với các môn khác."
            q7_text = "T1.7: Các tiết học thực hành, hoạt động STEM, nghiên cứu khoa học kỹ thuật hoặc lời khuyên của thầy cô tại trường giúp tôi tự tin theo học ngành này."
            q8_text = "T1.8: Nhu cầu nhân lực chuyển đổi số, trí tuệ nhân tạo (AI) và cơ hội việc làm rộng mở của ngành công nghệ là yếu tố thúc đẩy tôi lựa chọn."
            q9_text = "T1.9: Những câu chuyện khởi nghiệp công nghệ, hình mẫu kỹ sư tài năng hoặc các diễn đàn công nghệ trên mạng truyền cảm hứng mạnh mẽ cho tôi."
            q10_text = "T1.10: Tôi đã từng chủ động tham gia câu lạc bộ tin học/STEM, tham gia các cuộc thi sáng tạo kỹ thuật hoặc tham quan môi trường công nghệ thực tế."

        elif "Nhóm 2" in grp:
            q1_title = "T2.1: Khi quan sát các cửa hàng, doanh nghiệp hay trào lưu mua bán xung quanh, bạn có thói quen phân tích cách họ tiếp thị, định giá và lý do họ đông khách hay vắng khách không?"
            q1_opts = (
                "A. Hoàn toàn không quan tâm, xem đó là việc bình thường và không để ý đến cách thức hoạt động của họ.",
                "B. Rất hiếm khi để ý, chỉ thỉnh thoảng nhìn thấy khi đi ngang qua chứ không suy nghĩ sâu xa.",
                "C. Thỉnh thoảng có tò mò tự hỏi vì sao quán đông hoặc quán ế nhưng không phân tích chi tiết.",
                "D. Thường xuyên quan sát cách họ trang trí, thu hút khách hàng và tự đưa ra nhận xét cá nhân.",
                "E. Thường xuyên quan sát và phân tích sâu chiến lược tiếp thị, cách định giá sản phẩm và nguyên nhân thành công hay thất bại của họ."
            )
            q2_title = "T2.2: Khi làm việc nhóm với mục tiêu gấp rút, khả năng lập kế hoạch, phân chia công việc, đôn đốc tiến độ và quản lý ngân quỹ của bạn đạt mức nào?"
            q2_opts = (
                "A. Chờ người khác phân công việc gì thì làm việc nấy, né tránh việc quản lý tiền bạc.",
                "B. Lúng túng khi phải sắp xếp công việc, chỉ làm tốt phần việc cá nhân được giao.",
                "C. Có thể lập kế hoạch cơ bản và quản lý công việc trong phạm vi nhóm nhỏ ở mức trung bình.",
                "D. Khá chủ động lên danh sách công việc, đôn đốc các thành viên hoàn thành đúng thời hạn.",
                "E. Chủ động điều phối, lãnh đạo hiệu quả toàn bộ nhóm, thiết lập kế hoạch chi tiết và kiểm soát tốt các nguồn lực/ngân quỹ."
            )
            q3_title = "T2.3: Mức độ tự tin của bạn khi phải chủ động giao tiếp, đàm phán, kết nối với những người lạ để đạt được mục tiêu chung:"
            q3_opts = (
                "A. Rất e ngại, né tránh, cảm thấy lo lắng hoặc không thoải mái khi phải trò chuyện với người lạ.",
                "B. Hơi rụt rè, chỉ giao tiếp khi thực sự bắt buộc phải làm việc và thấy khá gượng gạo.",
                "C. Có thể giao tiếp xã giao bình thường nhưng thiếu sự chủ động để thuyết phục người khác.",
                "D. Tự tin bắt chuyện, bày tỏ quan điểm và kết nối khá tốt với những người xung quanh để đạt mục tiêu.",
                "E. Cực kỳ tự tin và linh hoạt, chủ động dẫn dắt cuộc trò chuyện, đàm phán trôi chảy và tạo được ảnh hưởng tích cực với đối phương."
            )
            q4_text = "T2.4: Gia đình tôi có truyền thống làm kinh doanh, hoặc cha mẹ rất ủng hộ tôi trở thành một nhà quản trị/kinh doanh/chuyên viên tài chính."
            q5_text = "T2.5: Khả năng tài chính của gia đình đảm bảo ổn định để tôi hoàn thành chương trình đại học khối kinh tế (và có thể hỗ trợ nguồn vốn ban đầu nếu cần)."
            q6_text = "T2.6: Năng lực học tập môn Toán (tư duy số liệu) kết hợp với Ngoại ngữ hoặc Ngữ văn (khả năng giao tiếp/diễn đạt) là ưu thế rõ rệt của tôi."
            q7_text = "T2.7: Việc tham gia ban cán sự lớp, ban chấp hành Đoàn, quản lý quỹ hoặc tổ chức các hội chợ/sự kiện tại trường giúp tôi bộc lộ rõ năng lực quản lý."
            q8_text = "T2.8: Mức thu nhập hấp dẫn, cơ hội thăng tiến nhanh và môi trường làm việc năng động của khối kinh tế là động lực lớn đối với tôi."
            q9_text = "T2.9: Hình tượng các doanh nhân thành đạt, các chuyên gia tài chính hoặc các chương trình khởi nghiệp trên truyền thông tác động mạnh đến định hướng của tôi."
            q10_text = "T2.10: Tôi đã từng trực tiếp bán hàng, gây quỹ, tổ chức sự kiện hoặc tham gia quản lý tài chính cho một dự án tập thể."

        elif "Nhóm 3" in grp:
            q1_title = "T3.1: Khi đứng trước một quy định bất hợp lý trong tập thể hoặc vấn đề thời sự gây tranh cãi, hành động thực tế của bạn thường là:"
            q1_opts = (
                "A. Mặc kệ, làm ngơ, không quan tâm đến những chuyện xung quanh hay quy định chung.",
                "B. Cảm thấy khó chịu nhưng chỉ biết phàn nàn qua loa với bạn bè thân thiết chứ không làm gì khác.",
                "C. Thỉnh thoảng theo dõi thông tin, có bức xúc riêng nhưng ngại lên tiếng hay can thiệp.",
                "D. Quan sát cách mọi người phản ứng, chia sẻ góc nhìn cá nhân trên tinh thần xây dựng và hòa giải.",
                "E. Tìm hiểu căn cứ, lập luận logic và đề xuất sửa đổi quy định hoặc vấn đề một cách thuyết phục."
            )
            q2_title = "T3.2: Khả năng xây dựng hệ thống lý lẽ, tìm kiếm dẫn chứng thực tế và phản biện để bảo vệ quan điểm của mình trước tập thể:"
            q2_opts = (
                "A. Rất kém, ngại tranh luận, dễ bị lung lay hoặc lúng túng khi có người khác phản bác.",
                "B. Hơi lúng túng khi phải sắp xếp ý kiến, thường giữ im lặng trong các cuộc tranh luận đông người.",
                "C. Có thể đưa ra ý kiến cá nhân ở mức cơ bản nhưng thiếu hệ thống dẫn chứng sắc bén.",
                "D. Khá rõ ràng trong cách diễn đạt, biết cách sử dụng dẫn chứng để bảo vệ quan điểm đúng đắn.",
                "E. Rất sắc bén, tự tin thuyết phục, xây dựng hệ thống lý lẽ chặt chẽ và có khả năng thuyết phục tập thể cao."
            )
            q3_title = "T3.3: Mức độ nhạy bén với các vấn đề chuẩn mực đạo đức, sự liêm chính và tinh thần thượng tôn pháp luật trong lối sống hàng ngày của bạn:"
            q3_opts = (
                "A. Ít khi để tâm đến các quy tắc hay chuẩn mực, đôi khi xem nhẹ việc tuân thủ nội quy.",
                "B. Chỉ tuân thủ khi có sự giám sát trực tiếp từ người có thẩm quyền.",
                "C. Chấp hành tương đối tốt các quy định chung nhưng ít khi phân tích sâu về tính đúng sai đạo đức.",
                "D. Nhạy bén với các hành vi sai lệch, luôn cố gắng sống chuẩn mực và tôn trọng quy định.",
                "E. Luôn đặt lên hàng đầu tinh thần thượng tôn pháp luật, tính liêm chính và các giá trị công bằng trong mọi mặt đời sống."
            )
            q4_text = "T3.4: Cha mẹ và người thân coi trọng sự ổn định, uy tín xã hội hoặc định hướng tôi công tác trong cơ quan nhà nước, tổ chức tư pháp, xã hội."
            q5_text = "T3.5: Điều kiện kinh tế gia đình đủ vững vàng để hỗ trợ tôi theo đuổi ngành Luật/Xã hội trong suốt quá trình đào tạo đại học và sau đại học."
            q6_text = "T3.6: Năng lực học tập các môn Ngữ văn, Lịch sử, Giáo dục công dân/Kinh tế & Pháp luật là điểm tựa kết quả học tập tốt nhất của tôi ở trường."
            q7_text = "T3.7: Các tiết học pháp luật, diễn đàn học sinh, hoạt động tranh biện hoặc góp ý từ thầy cô giáo giúp tôi tự tin vào tư duy lập luận của mình."
            q8_text = "T3.8: Vị thế xã hội, tính chất công việc bảo vệ quyền lợi con người và nhu cầu chuyên gia pháp lý/chính sách ngày càng cao khiến tôi chọn ngành này."
            q9_text = "T3.9: Hình ảnh các luật sư sắc sảo, các nhà ngoại giao bản lĩnh hoặc nhà hoạt động xã hội uy tín trên truyền thông thôi thúc tôi dấn thân."
            q10_text = "T3.10: Tôi đã từng tham gia câu lạc bộ tranh biện, các buổi tọa đàm, phiên tòa giả định hoặc các hoạt động công tác tình nguyện xã hội."

        elif "Nhóm 4" in grp:
            q1_title = "T4.1: Khi đối mặt với nhiệm vụ phải tiếp nhận, ghi nhớ và hệ thống hóa một khối lượng kiến thức chi tiết, chính xác tuyệt đối, thái độ của bạn là gì?"
            q1_opts = (
                "A. Cực kỳ ngán ngẩm, mau nản, cảm thấy quá tải và không muốn tiếp thu các chi tiết phức tạp.",
                "B. Cảm thấy căng thẳng, chỉ ghi chép qua loa đại khái chứ không muốn hệ thống hóa sâu.",
                "C. Có thể hoàn thành việc học tập ở mức trung bình nếu có sự đôn đốc hoặc có đề cương sẵn.",
                "D. Khá cẩn thận, chủ động ghi chép và sắp xếp lại tài liệu để dễ dàng ghi nhớ và ôn tập.",
                "E. Tỉ mỉ, kiên nhẫn ghi chép và ghi nhớ sâu, đòi hỏi độ chính xác cao trong từng chi tiết nhỏ nhất."
            )
            q2_title = "T4.2: Khả năng giữ bình tĩnh, kiểm soát cảm xúc cá nhân khi chứng kiến các tình huống nguy cấp, tai nạn hoặc môi trường áp lực cao của bạn:"
            q2_opts = (
                "A. Hoảng loạn, trốn tránh, dễ bị mất bình tĩnh hoặc ngất xỉu khi thấy máu, vết thương hoặc cảnh nguy cấp.",
                "B. Hơi lúng túng, bối rối và khó giữ được sự tập trung khi đối mặt với tình huống căng thẳng.",
                "C. Có thể kiềm chế cảm xúc ở mức tạm ổn nhưng tâm lý vẫn bị ảnh hưởng sau sự việc.",
                "D. Khá vững vàng, biết cách trấn an bản thân để hỗ trợ xử lý tình huống xung quanh.",
                "E. Giữ được bình tĩnh và tập trung xử lý, không bị chi phối bởi cảm xúc tiêu cực trong mọi tình huống khẩn cấp."
            )
            q3_title = "T4.3: Bạn đánh giá mức độ sẵn sàng hy sinh thời gian cá nhân (học tập dài năm, trực đêm, áp lực sinh mệnh) vì mục tiêu cứu chữa người bệnh ở mức nào?"
            q3_opts = (
                "A. Hoàn toàn không chấp nhận, ưu tiên thời gian cá nhân, sợ áp lực và sợ công việc vất vả, trực đêm.",
                "B. Khá e ngại việc học tập kéo dài và lịch trình làm việc khắc nghiệt của ngành y tế.",
                "C. Chấp nhận ở mức độ vừa phải nếu đó là công việc mang lại nguồn thu nhập ổn định.",
                "D. Sẵn sàng thích nghi với lịch trình vất vả vì hiểu rõ đặc thù cứu người của ngành nghề.",
                "E. Sẵn sàng dấn thân vì sứ mệnh nghề, xem việc chữa bệnh cứu người là lý tưởng sống bất chấp áp lực thời gian và không gian."
            )
            q4_text = "T4.4: Gia đình tôi có người làm trong ngành y hoặc cha mẹ đặt kỳ vọng rất lớn muốn tôi trở thành y bác sĩ, dược sĩ."
            q5_text = "T4.5: Gia đình tôi có điều kiện kinh tế đủ vững để nuôi tôi theo học ngành y dài hạn (từ 5 – 7 năm) với mức học phí đặc thù khá cao."
            q6_text = "T4.6: Điểm số và năng lực giải quyết các bài tập phân hóa cao ở tổ hợp môn Hóa học – Sinh học (hoặc Toán – Hóa – Sinh) của tôi ở mức nổi bật."
            q7_text = "T4.7: Các bài học chuyên sâu về cơ thể sống, chương trình tư vấn tuyển sinh khối ngành y dược của trường giúp tôi hiểu rõ tính khốc liệt của ngành."
            q8_text = "T4.8: Tính ổn định lâu dài, sự trọng vọng của xã hội và nhu cầu chăm sóc sức khỏe không bao giờ lỗi thời củng cố niềm tin chọn nghề của tôi."
            q9_text = "T4.9: Sự cống hiến quên mình và y đức của các y bác sĩ tuyến đầu trên truyền thông tạo ra sự xúc động và truyền động lực lớn cho tôi."
            q10_text = "T4.10: Tôi đã từng chủ động tham gia tập huấn sơ cấp cứu học đường, tình nguyện viên tại cơ sở y tế hoặc tự tìm hiểu sâu về đời sống sinh viên y khoa."

        elif "Nhóm 5" in grp:
            q1_title = "T5.1: Khi hướng dẫn bài hoặc truyền đạt một kỹ năng cho người khác mà họ chưa hiểu ngay, thái độ thực tế của bạn là gì?"
            q1_opts = (
                "A. Cáu gắt, bỏ mặc, cảm thấy bực bội khi người khác chậm hiểu hoặc hỏi lại nhiều lần.",
                "B. Hơi thiếu kiên nhẫn, chỉ giải thích thêm một lần ngắn gọn rồi thôi.",
                "C. Kiềm chế được cảm xúc ở mức trung bình, giải thích lại theo cách cũ nhưng không đổi mới cách diễn đạt.",
                "D. Khá kiên nhẫn, tìm cách nói lại đơn giản hơn để người nghe dễ hình dung vấn đề.",
                "E. Kiên nhẫn tìm nhiều cách diễn đạt khác nhau đến khi họ hiểu, luôn tạo cảm giác thoải mái cho người học."
            )
            q2_title = "T5.2: Khả năng đọc vị cảm xúc, lắng nghe sâu không phán xét và gợi mở giúp người khác vượt qua cảm xúc tiêu cực của bạn:"
            q2_opts = (
                "A. Rất vụng về, không biết an ủi, đôi khi vô tình nói những câu khiến đối phương thêm chạnh lòng.",
                "B. Lúng túng, chỉ biết ngồi im nghe người khác kể lể chứ không biết cách khuyên nhủ.",
                "C. Có thể đưa ra một số lời khuyên mang tính lý thuyết chung chung khi bạn bè gặp chuyện buồn.",
                "D. Biết cách lắng nghe khá tốt, đồng cảm với cảm xúc của người đối diện và đưa ra lời động viên chân thành.",
                "E. Thấu cảm cao, giao tiếp tinh tế, biết lắng nghe sâu sắc không phán xét và khéo léo gỡ rối tâm lý cho người khác."
            )
            q3_title = "T5.3: Mức độ say mê của bạn đối với việc đọc sách, tìm hiểu sâu về tâm lý con người, các giá trị văn hóa và sự tiến bộ của giáo dục:"
            q3_opts = (
                "A. Hoàn toàn không thích, thấy buồn ngủ hoặc chán nản khi phải đọc sách hay nghiên cứu về con người và xã hội.",
                "B. Rất ít khi đọc sách, chỉ đọc khi có yêu cầu bắt buộc từ nhà trường.",
                "C. Thỉnh thoảng đọc các loại sách giải trí hoặc bài viết ngắn trên mạng liên quan đến đời sống.",
                "D. Khá yêu thích việc đọc sách, quan tâm đến các vấn đề xã hội và sự phát triển của giáo dục.",
                "E. Rất đam mê nghiên cứu và chiêm nghiệm các giá trị văn hóa, tâm lý học và các phương pháp đổi mới giáo dục."
            )
            q4_text = "T5.4: Cha mẹ đề cao môi trường giáo dục mẫu mực, sự thanh cao, ổn định và rất khuyến khích tôi trở thành giáo viên hoặc chuyên gia tâm lý."
            q5_text = "T5.5: Gia đình tôi thấy phù hợp với các chính sách hỗ trợ học phí của nhà nước dành cho khối ngành sư phạm và chi phí đào tạo khối khoa học xã hội."
            q6_text = "T5.6: Điểm số các môn Ngữ văn, Lịch sử, Ngoại ngữ hoặc các môn khoa học cơ bản của tôi luôn giữ vững ở mức khá, giỏi."
            q7_text = "T5.7: Hình mẫu tận tụy của các thầy cô giáo tại trường THPT Trung Giã chính là tấm gương trực tiếp truyền cảm hứng chọn nghề cho tôi."
            q8_text = "T5.8: Sự gia tăng của các vấn đề sức khỏe tinh thần và yêu cầu đổi mới căn bản nền giáo dục mở ra nhiều cơ hội phát triển cho khối ngành này."
            q9_text = "T5.9: Những người thầy đổi mới, các nhà tâm lý học hay các diễn giả truyền cảm hứng trên mạng xã hội khiến tôi khát khao làm công việc lan tỏa giá trị."
            q10_text = "T5.10: Tôi đã từng thử sức làm gia sư, làm người dẫn dắt hoạt động học tập, phụ trách công tác tư vấn bạn đồng trang lứa hoặc lớp học từ thiện."

        else:
            q1_title = "T6.1: Khi nhìn một poster, trang web, bao bì sản phẩm hay công trình kiến trúc, bạn có phản xạ tự nhiên là săm soi đường nét, bố cục và màu sắc của nó không?"
            q1_opts = (
                "A. Không bao giờ để ý, chỉ xem nội dung thông thường và hoàn toàn không quan tâm đến hình thức trình bày.",
                "B. Rất hiếm khi, chỉ chú ý nếu thiết kế quá xấu hoặc có điểm kỳ lạ đập ngay vào mắt.",
                "C. Thỉnh thoảng có nhìn qua nhưng chỉ dừng lại ở mức đẹp hay xấu chung chung, không phân tích sâu.",
                "D. Khá thường xuyên quan sát cách phối màu và sắp xếp bố cục của các sản phẩm xung quanh.",
                "E. Luôn quan sát tỉ mỉ và tự đánh giá thẩm mỹ từng chi tiết về đường nét, font chữ, cách phối màu và bố cục của thiết kế"
            )
            q2_title = "T6.2: Khả năng hình dung không gian, phối trộn màu sắc hoặc chuyển hóa một ý tưởng trừu tượng trong đầu thành hình ảnh/sản phẩm cụ thể:"
            q2_opts = (
                "A. Rất kém, không biết vẽ/tạo hình, gặp khó khăn lớn khi phải tưởng tượng ra bố cục hình ảnh.",
                "B. Hơi lúng túng, cần có mẫu (template) hoặc hình mẫu có sẵn để làm theo chứ không tự sáng tạo được.",
                "C. Có thể phác thảo hoặc thiết kế ở mức cơ bản, đúng yêu cầu tối thiểu nhưng thiếu điểm nhấn độc đáo.",
                "D. Khá linh hoạt trong việc phối màu và chuyển hóa ý tưởng thành hình ảnh trực quan khá bắt mắt.",
                "E. Rất nhạy bén và khéo léo, có khả năng hình dung không gian xuất sắc và hiện thực hóa ý tưởng trừu tượng thành sản phẩm sắc sảo."
            )
            q3_title = "T6.3: Khi có một ý tưởng thẩm mỹ khác biệt bị người khác hoài nghi, mức độ tự tin và bản lĩnh kiên trì bảo vệ dấu ấn sáng tạo riêng của bạn:"
            q3_opts = (
                "A. Dễ dàng từ bỏ theo số đông, nhanh chóng thay đổi ý tưởng theo ý kiến của người khác để an toàn.",
                "B. Hơi rụt rè, dễ bị dao động và thiếu tự tin khi vấp phải ý kiến trái chiều.",
                "C. Bảo vệ ý tưởng ở mức độ vừa phải nhưng nếu bị phản đối nhiều thì sẽ thỏa hiệp theo số đông.",
                "D. Tự tin giải thích ưu điểm của thiết kế và sẵn sàng tiếp thu các góp ý hợp lý để hoàn thiện hơn.",
                "E. Tự tin giải trình ý nghĩa tác phẩm, giữ vững bản lĩnh và bảo vệ mạnh mẽ phong cách sáng tạo mang dấu ấn riêng biệt của mình."
            )
            q4_text = "T6.4: Cha mẹ thấu hiểu thiên hướng nghệ thuật, tôn trọng cá tính sáng tạo và không ngăn cấm tôi theo đuổi ngành thiết kế/nghệ thuật."
            q5_text = "T6.5: Gia đình sẵn sàng chu cấp kinh phí đầu tư dụng cụ vẽ, máy tính đồ họa chuyên dụng và học phí các khóa học kỹ năng sáng tạo chuyên sâu."
            q6_text = "T6.6: Năng khiếu mỹ thuật hoặc khả năng ứng dụng công nghệ đồ họa máy tính, tư duy hình học không gian của tôi được thầy cô ghi nhận ở trường."
            q7_text = "T6.7: Các hoạt động trang trí bảng tin, thiết kế kỷ yếu, sự kiện văn nghệ hoặc sân chơi sáng tạo tại trường tạo đất diễn cho năng khiếu của tôi."
            q8_text = "T6.8: Sự bùng nổ của ngành công nghiệp sáng tạo số (Game, UI/UX, phim ảnh, thời trang) mang lại mức thu nhập và đầu ra việc làm hấp dẫn cho tôi."
            q9_text = "T6.9: Tác phẩm của các nhà thiết kế, kiến trúc sư hoặc nghệ sĩ danh tiếng trên không gian mạng truyền cảm hứng mạnh mẽ đến phong cách của tôi."
            q10_text = "T6.10: Tôi đã từng tự tay thiết kế sản phẩm đồ họa, vẽ tranh dự thi, dựng video clip hoặc tham gia các triển lãm nghệ thuật thực tế."

        c1_opt = st.radio(q1_title, q1_opts, key=f"c1_{grp}")
        c1 = lay_diem_lua_chon(c1_opt)

        c2_opt = st.radio(q2_title, q2_opts, key=f"c2_{grp}")
        c2 = lay_diem_lua_chon(c2_opt)

        c3_opt = st.radio(q3_title, q3_opts, key=f"c3_{grp}")
        c3 = lay_diem_lua_chon(c3_opt)

        st.markdown(
            "📌 **Thang đo Likert đánh giá mức độ:**\n\n"
            "- **1 điểm:** Hoàn toàn không đồng ý / Rất thấp\n"
            "- **2 điểm:** Không đồng ý / Thấp\n"
            "- **3 điểm:** Phân vân / Trung bình\n"
            "- **4 điểm:** Đồng ý / Khá\n"
            "- **5 điểm:** Hoàn toàn đồng ý / Rất cao"
        )

        g1 = st.slider(f"{q4_text} (1-5):", 1, 5, 3, key=f"g1_{grp}")
        g2 = st.slider(f"{q5_text} (1-5):", 1, 5, 3, key=f"g2_{grp}")
        
        n1 = st.slider(f"{q6_text} (1-5):", 1, 5, 3, key=f"n1_{grp}")
        n2 = st.slider(f"{q7_text} (1-5):", 1, 5, 3, key=f"n2_{grp}")
        
        x1 = st.slider(f"{q8_text} (1-5):", 1, 5, 3, key=f"x1_{grp}")
        x2 = st.slider(f"{q9_text} (1-5):", 1, 5, 3, key=f"x2_{grp}")
        
        t1 = st.slider(f"{q10_text} (1-5):", 1, 5, 3, key=f"t1_{grp}")
        
        score_noi_luc = (c1 + c2 + c3) / 3
        score_gia_dinh = (g1 + g2) / 2
        score_nha_truong = (n1 + n2) / 2
        score_xa_hoi = (x1 + x2) / 2
        score_trai_nghiem = float(t1)
        
        overall_score = (score_noi_luc + score_gia_dinh + score_nha_truong + score_xa_hoi + score_trai_nghiem) / 5
        
        group_report_data[grp] = {
            "noi_luc": score_noi_luc,
            "gia_dinh": score_gia_dinh,
            "nha_truong": score_nha_truong,
            "xa_hoi": score_xa_hoi,
            "trai_nghiem": score_trai_nghiem,
            "overall": overall_score
        }
        st.write("---")

    if st.button("🚀 XUẤT BẢN BÁO CÁO PHẢN HỒI CÁ NHÂN HÓA (OUTPUT REPORT)"):
        if not name.strip():
            st.warning("Vui lòng nhập Họ và tên ở Phần 1!")
        else:
            st.session_state["show_report"] = True

    if st.session_state.get("show_report", False):
        if not name.strip():
            st.warning("Vui lòng nhập Họ và tên ở Phần 1!")
        else:
            st.success(f"### 📊 BÁO CÁO HƯỚNG NGHIỆP CÁ NHÂN HÓA DÀNH CHO: {name.upper()} ({grade})")
            st.info("📌 **Cách đọc báo cáo:** Công cụ không trả lời 'ngành nào chắc chắn phù hợp', mà giúp bạn nhận diện mức độ tương thích hiện tại, yếu tố đang hỗ trợ/cản trở và việc nên làm tiếp theo.")

            if len(group_report_data) >= 2:
                st.markdown("## 🆚 So sánh các nhóm ngành đang cân nhắc")
                compare_rows = []
                for g, d in group_report_data.items():
                    strengths, priorities = tao_ho_so_ca_nhan(d)
                    s_label = FACTOR_LABELS[strengths[0][0]] if strengths else "Đang cập nhật"
                    p_label = FACTOR_LABELS[priorities[0][0]] if priorities else "Đang cập nhật"
                    compare_rows.append({
                        "Nhóm ngành": g.split(": ", 1)[-1],
                        "Tương thích tham khảo": f"{d.get('overall', 3.0):.2f}/5",
                        "Điểm tựa nổi bật": s_label,
                        "Yếu tố cần củng cố": p_label
                    })
                st.table(compare_rows)
                st.caption("Bảng này hỗ trợ so sánh hai lựa chọn theo cùng một hệ tiêu chí; không phải bảng xếp hạng ngành nghề.")

            for grp, data in group_report_data.items():
                st.markdown(f"#### 🔍 Phân tích chi tiết: **{grp}**")
                
                # TẦNG 1: RADAR CHART
                st.markdown(f"**Tầng 1: Radar Chart:**")
                categories = ['Nội lực hành vi', 'Nền tảng gia đình', 'Hậu thuẫn nhà trường', 'Đón đầu xã hội', 'Cọ xát trải nghiệm']
                values = [data['noi_luc'], data['gia_dinh'], data['nha_truong'], data['xa_hoi'], data['trai_nghiem']]
                
                fig = go.Figure()
                fig.add_trace(go.Scatterpolar(r=values, theta=categories, fill='toself', name=grp, line_color='rgb(31, 119, 180)'))
                fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=False, height=400, margin=dict(t=30, b=30, l=30, r=30))
                st.plotly_chart(fig, use_container_width=True)
                st.write(f"⭐ **Điểm tương thích tổng thể: {round(data['overall'], 2)} / 5.0**")
                
                # ==========================================
                # TẦNG 2: THUẬT TOÁN NHẬN DIỆN KHOẢNG CÁCH (GAP ANALYSIS)
                # ==========================================
                st.markdown(f"**Tầng 2: Gap Analysis:**")
                avg_score = student_data.get("avg_to_hop", 24.0) if student_data else 24.0
                
                if data['noi_luc'] >= 4.0 and data['nha_truong'] < 3.5:
                    st.warning("⚠️ *Xung đột Sở thích - Năng lực/Điểm số:* Phát hiện lệch pha giữa đam mê cá nhân và kết quả học tập chuyên môn.")
                    if grade == "Khối 10":
                        st.info("📌 **Cảnh báo hệ thống:**\nBạn có đam mê tự nhiên rất lớn với ngành nhưng kết quả học tập môn chuyên môn hiện tại chưa phải là lợi thế. Để tránh rủi ro khi xét tuyển, bạn cần:\n(1) Hãy xem xét lại và lựa chọn tổ hợp môn thi phù hợp với năng lực của bản thân;\n(2) Lập kế hoạch phụ đạo tăng cường tổ hợp môn xét tuyển ngay trong học kỳ này.")
                    elif grade == "Khối 11":
                        st.info("📌 **Cảnh báo hệ thống:**\nBạn có đam mê tự nhiên rất lớn với ngành nhưng kết quả học tập môn chuyên môn hiện tại chưa phải là lợi thế. Để tránh rủi ro khi xét tuyển, bạn cần:\n(1) Lập kế hoạch phụ đạo tăng cường tổ hợp môn xét tuyển ngay trong học kỳ này;\n(2) Tìm hiểu thêm các phương thức xét tuyển của trường đại học bạn dự định thi vào;\n(3) Tham khảo thêm các hệ đào tạo cao đẳng thực hành hoặc đại học top giữa của nhóm ngành này.")
                    else:
                        st.info("📌 **Cảnh báo hệ thống:**\nBạn có đam mê tự nhiên rất lớn với ngành nhưng kết quả học tập môn chuyên môn hiện tại chưa phải là lợi thế. Để tránh rủi ro khi xét tuyển, bạn cần:\n(1) Tìm hiểu thêm các phương thức xét tuyển của trường đại học bạn dự định thi vào;\n(2) Tham khảo thêm các hệ đào tạo cao đẳng thực hành hoặc đại học top giữa của nhóm ngành này.\n\n**💡 Gợi ý phân bổ nguyện vọng:** Chia đều nguyện vọng vào 3 nhóm (mức tham khảo cao hơn, tương đương và thấp hơn).\n👉 *Tra cứu quy chế tuyển sinh chi tiết tại [Cổng thông tin tuyển sinh Bộ GD&ĐT](https://tuyensinh.moet.gov.vn).*")

                elif data['noi_luc'] >= 4.0 and data['gia_dinh'] < 3.0:
                    st.warning("⚠️ *Xung đột Cá nhân - Gia đình/Kinh tế:* Nội lực cao nhưng nguồn lực tài chính/hậu thuẫn từ gia đình hạn chế.")
                    st.markdown("""📉 **Phiếu đối thoại cùng cha mẹ & Gợi ý trường công lập học phí tốt tại Hà Nội theo nhóm ngành:**
Bạn có thể cởi mở chia sẻ với bố mẹ rằng: Trong quá trình học đại học, bạn hoàn toàn có thể chủ động tìm các công việc làm thêm phù hợp (như gia sư, trợ lý, bán thời gian) từ năm thứ 2, thứ 3 để tự chi trả một phần sinh hoạt phí hàng ngày. Đồng thời, hãy khẳng định với bố mẹ về triển vọng việc làm thực tế, mức thu nhập và khả năng tự lập tài chính sau khi ra trường nếu bản thân nỗ lực học tập tốt.
Để giảm bớt gánh nặng tài chính ngay từ bước đầu cho gia đình, hệ thống gợi ý bạn nên ưu tiên xem xét các trường công lập có mức học phí tiêu chuẩn hoặc các nhóm ngành có chính sách hỗ trợ tốt dưới đây:""")
                    
                    if "Nhóm 1" in grp:
                        st.markdown(
                            "- **[Đại học Bách Khoa Hà Nội (HUST)]**\n"
                            "- **[Đại học Công nghiệp Hà Nội (HaUI)]**\n"
                            "- **[Đại học Giao thông Vận tải (UTC)]**\n"
                            "- **[Đại học Thủy lợi (TLU)]**"
                        )
                    elif "Nhóm 2" in grp:
                        st.markdown(
                            "- **[Đại học Kinh tế Quốc dân (NEU)]**\n"
                            "- **[Đại học Thương mại (TMU)]**\n"
                            "- **[Học viện Ngân hàng (BA)]**\n"
                            "- **[Đại học Mở Hà Nội (HOU) & Lao động Xã hội (ULSA)]**"
                        )
                    elif "Nhóm 3" in grp:
                        st.markdown(
                            "- **[Đại học Luật Hà Nội (HLU)]**\n"
                            "- **[Đại học KHXH&NV – ĐHQGHN (USSH)]**\n"
                            "- **[Học viện Báo chí và Tuyên truyền (AJC)]**"
                        )
                    elif "Nhóm 4" in grp:
                        st.markdown(
                            "- **[Đại học Y Hà Nội (HMU)]**\n"
                            "- **[Đại học Dược Hà Nội (HUP)]**\n"
                            "- **[Học viện Y Dược học Cổ truyền VN]**\n"
                            "- **[Đại học Y tế Công cộng (HUPH)]**"
                        )
                    elif "Nhóm 5" in grp:
                        st.markdown(
                            "- **[Đại học Sư phạm Hà Nội (HNUE) & HNUE2]** *(Miễn 100% học phí theo Nghị định 116 + Hỗ trợ 3,63 triệu đồng/tháng sinh hoạt phí)*\n"
                            "- **[Đại học Thủ đô Hà Nội (HNMU)]**"
                        )
                    else:
                        st.markdown(
                            "- **[Đại học Kiến trúc Hà Nội (HAU)] & [Xây dựng (HUCE)]**\n"
                            "- **[Đại học Mở Hà Nội (Khoa Thiết kế)]**"
                        )
                    
                    st.info(
                        "💡 **Tra cứu chi tiết học phí:** Để tham khảo mức học phí chi tiết theo tín chỉ hoặc năm học mới nhất của các trường công lập trên, học sinh và phụ huynh có thể tra cứu tại cổng thông tin: "
                        "[Khoa học VietJack - Thông tin tuyển sinh](https://khoahoc.vietjack.com/thong-tin-tuyen-sinh)."
                    )

                elif data['noi_luc'] >= 4.0 and data['trai_nghiem'] < 3.0:
                    st.warning("⚠️ *Thiếu cọ xát thực tế:* Hứng thú hiện tại của bạn chủ yếu đến từ hình dung qua phim ảnh/truyền thông. Bạn cần tham gia ngay một hoạt động trải nghiệm thực tế (nói chuyện với cựu học sinh trường đang làm trong ngành, tham quan doanh nghiệp) để kiểm chứng xem công việc thực tế có đúng như kỳ vọng không")
                else:
                    st.info("✅ Các chỉ số tương đối đồng bộ, chưa phát hiện khoảng cách lớn giữa các nhóm yếu tố.")

                # ==========================================
                # TẦNG 3: HỒ SƠ CÁ NHÂN + HÀNH ĐỘNG TIẾP THEO
                # ==========================================
                hien_thi_ho_so_tong_quan(data, grp, grade)

                # ==========================================
                # TẦNG 4: THÔNG TIN TUYỂN SINH THAM KHẢO THEO NGÀNH
                # ==========================================
                st.markdown("---")
                st.subheader(f"🏛️ NGÀNH & CƠ SỞ ĐÀO TẠO THAM KHẢO CHO: {grp}")
                st.info(
                    "📌 **Cách đọc:** Điểm tham khảo được gắn với **từng ngành/chương trình**, "
                    "không phải một điểm đại diện cho toàn trường. Dữ liệu được phân loại theo "
                    "năm, tổ hợp và phương thức khi cơ sở dữ liệu có thông tin tương ứng. "
                )

                to_hop_hs = student_data.get("to_hop", "") if student_data else ""
                diem_hs = student_data.get("avg_to_hop", 0.0) if student_data else 0.0
                ds_nganh_all = PROGRAM_DATABASE.get(grp, [])
                
                if "Nhóm 5" in grp:
                    ds_nganh = loc_nganh_tham_khao(ds_nganh_all, to_hop_hs, cho_phep_nang_khieu=False)
                else:
                    ds_nganh = loc_nganh_tham_khao(ds_nganh_all, to_hop_hs)
                loc_theo_to_hop = True
                to_hop_loc_hien_tai = to_hop_hs

                if "Nhóm 5" in grp and not ds_nganh and ds_nganh_all:
                    st.warning(
                        f"⚠️ Chưa tìm thấy ngành trong cơ sở dữ liệu hiện tại có tổ hợp **{to_hop_hs}**. "
                        "Bạn có thể nhập một tổ hợp khác để hệ thống lọc lại danh sách ngành Sư phạm – Tâm lý & Nhân văn."
                    )
                    to_hop_nhap_them = st.text_input(
                        "Nhập trực tiếp mã tổ hợp khác:",
                        placeholder="Ví dụ: C00, C03, D01, D14...",
                        key="custom_to_hop_nhom5"
                    ).strip().upper()
                    if to_hop_nhap_them:
                        to_hop_loc_hien_tai = to_hop_nhap_them
                        ds_nganh = loc_nganh_tham_khao(ds_nganh_all, to_hop_loc_hien_tai, cho_phep_nang_khieu=False)
                        if ds_nganh:
                            st.success(f"✓ Đã tìm thấy **{len(ds_nganh)}** ngành/chương trình có tổ hợp **{to_hop_loc_hien_tai}**.")
                        else:
                            st.info("Chưa tìm thấy bản ghi đã xác minh cho tổ hợp vừa nhập trong cơ sở dữ liệu hiện tại.")

                if not ds_nganh and ds_nganh_all and "Nhóm 5" not in grp:
                    ds_nganh = [x for x in ds_nganh_all if x.get("verified", False)]
                    loc_theo_to_hop = False

                ds_nganh = chon_10_lua_chon_phu_diem(ds_nganh, so_luong=10)
                cao, tuong_duong, thap = phan_loai_nganh(ds_nganh, diem_hs)

                if not ds_nganh:
                    st.warning(
                        "⚠️ Nhóm ngành này hiện chưa có đủ bản ghi điểm chuẩn đã được chuẩn hóa trong "
                        "phiên bản thử nghiệm. Đây là khoảng dữ liệu cần tiếp tục cập nhật."
                    )
                else:
                    if loc_theo_to_hop:
                        st.caption(
                            f"Hiện có {len(ds_nganh)} bản ghi đã xác minh phù hợp với tổ hợp **{to_hop_loc_hien_tai}**."
                        )
                    else:
                        st.warning(
                            f"⚠️ Nhóm này có ngành đặc thù hoặc dữ liệu tổ hợp chưa đồng nhất với **{to_hop_loc_hien_tai}**. "
                            "Hệ thống vẫn hiển thị các lựa chọn đã xác minh để học sinh tiếp tục tìm hiểu, "
                            "nhưng **không dùng chúng để kết luận khả năng xét tuyển**. Cần kiểm tra riêng tổ hợp, "
                            "môn năng khiếu và phương thức của từng ngành."
                        )
                    if len(ds_nganh) < 10:
                        st.warning(
                            f"⚠️ Cơ sở dữ liệu hiện mới có {len(ds_nganh)} lựa chọn đã xác minh cho nhóm này "
                            f"với tổ hợp {to_hop_loc_hien_tai}."
                        )
                    hien_thi_danh_sach_nganh(
                        "📈 Mức tham khảo cao hơn", cao, diem_hs
                    )
                    st.write("")
                    hien_thi_danh_sach_nganh(
                        "🎯 Mức tham khảo tương đương", tuong_duong, diem_hs
                    )
                    st.write("")
                    hien_thi_danh_sach_nganh(
                        "📉 Mức tham khảo thấp hơn", thap, diem_hs
                    )

                st.caption(
                    "⚠️ Điểm trúng tuyển 2026 là dữ liệu tham khảo của kỳ tuyển sinh 2026, không phải dự đoán khả năng trúng tuyển cho các năm sau. "
                    "Điểm chuẩn có thể thay đổi theo từng năm, ngành, phương thức, tổ hợp và quy định tuyển sinh."
                )

                st.markdown("---")
                st.markdown(
                    "🔗 *Tra cứu quy chế tuyển sinh chính thức tại [Cổng thông tin tuyển sinh Bộ GD&ĐT](https://tuyensinh.moet.gov.vn).* "
                    "💡 **Gợi ý tra cứu thêm:** Để xem chi tiết đề án tuyển sinh, điểm chuẩn các năm và học phí cụ thể của từng trường đại học trên toàn quốc, bạn có thể truy cập cổng thông tin tổng hợp tại: "
                    "[Khoa học VietJack - Thông tin tuyển sinh](https://khoahoc.vietjack.com/thong-tin-tuyen-sinh)."
                )
