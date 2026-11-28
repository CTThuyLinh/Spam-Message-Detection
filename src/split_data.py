
import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Đọc dữ liệu đã làm sạch
df = pd.read_csv("data/processed/cleaned_data.csv")

# 2. Tách dữ liệu thành Train (70%) và phần còn lại (30%)
train_df, temp_df = train_test_split(
    df,
    test_size=0.30,
    random_state=42,
    stratify=df["label"]
)

# 3. Chia phần còn lại thành Validation (15%) và Test (15%)
val_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    random_state=42,
    stratify=temp_df["label"]
)

# 4. Tạo thư mục lưu dữ liệu nếu chưa có
import os
os.makedirs("data/processed/splits", exist_ok=True)

# 5. Lưu ba tập dữ liệu
train_df.to_csv(
    "data/processed/splits/train.csv",
    index=False,
    encoding="utf-8"
)

val_df.to_csv(
    "data/processed/splits/validation.csv",
    index=False,
    encoding="utf-8"
)

test_df.to_csv(
    "data/processed/splits/test.csv",
    index=False,
    encoding="utf-8"
)

# 6. Hiển thị kết quả
print("===== KET QUA CHIA DU LIEU =====")
print("Train:", len(train_df))
print("Validation:", len(val_df))
print("Test:", len(test_df))

print("\n===== TY LE NHAN TRONG TUNG TAP =====")

for name, data in [
    ("Train", train_df),
    ("Validation", val_df),
    ("Test", test_df)
]:
    print(f"\n{name}:")
    print(data["label"].value_counts())
    print(data["label"].value_counts(normalize=True) * 100)

print("\nDa chia va luu du lieu thanh cong!")
