
import pandas as pd

# Đọc dữ liệu
df = pd.read_csv(
    "data/spam.csv",
    encoding="cp1252",
    usecols=[0, 1]
)

# Đổi tên cột
df.columns = ["label", "message"]

# 1. Thống kê số lượng nhãn
print("===== SO LUONG NHAN =====")
print(df["label"].value_counts())

# 2. Tính tỷ lệ phần trăm
print("\n===== TY LE NHAN =====")
print(df["label"].value_counts(normalize=True) * 100)

# 3. Kiểm tra dữ liệu trống
print("\n===== DU LIEU TRONG =====")
print(df.isnull().sum())

# 4. Kiểm tra dòng trùng lặp hoàn toàn
print("\n===== DU LIEU TRUNG LAP =====")
print("So dong trung:", df.duplicated().sum())

# 5. Kiểm tra nội dung giống nhau nhưng khác nhãn
label_count = df.groupby("message")["label"].nunique()

conflict = label_count[label_count > 1]

print("\n===== TIN NHAN KHAC NHAN =====")
print("So tin nhan co nhieu nhan:", len(conflict))

# 6. Hiển thị một số dòng trùng lặp
print("\n===== VI DU DU LIEU TRUNG =====")
print(df[df.duplicated(keep=False)].head(10))

