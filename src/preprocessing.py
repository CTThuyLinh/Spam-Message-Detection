
import pandas as pd

# 1. Đọc dữ liệu gốc
df = pd.read_csv(
    "data/spam.csv",
    encoding="cp1252",
    usecols=[0, 1]
)

# 2. Đặt lại tên cột
df.columns = ["label", "message"]

# 3. Lưu số lượng dữ liệu ban đầu
print("So dong ban dau:", len(df))

# 4. Xóa các dòng trùng lặp hoàn toàn
df = df.drop_duplicates(
    subset=["label", "message"]
)

# 5. Đưa index về thứ tự mới
df = df.reset_index(drop=True)

# 6. Kiểm tra kết quả
print("So dong sau khi xu ly:", len(df))

print("\nSo luong tung nhan:")
print(df["label"].value_counts())

print("\nSo dong trung lap con lai:")
print(df.duplicated().sum())

# 7. Lưu dữ liệu đã xử lý
df.to_csv(
    "data/processed/cleaned_data.csv",
    index=False,
    encoding="utf-8"
)

print("\nDa luu du lieu thanh cong!")
