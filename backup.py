import pandas as pd
from loader import db
# Faylni yuklash
file_path = "users.csv"  # Sizning fayl yo'lingiz
data = pd.read_csv(file_path, header=None)  # CSV faylni o'qish

# C ustunidagi qiymatni olish (indeks 2 bo'ladi, chunki indeks 0 dan boshlanadi)

n = 1172
while True:
    try:
        user_id = data.iloc[0,n]
        #print(type(user_id))
        user_id = int(user_id)
        #print(type(user_id))
    
        db.add_user(int(user_id),name=user_id,active=1)
        print(f"User N={n} | {user_id} added succesfully!")
        n += 1
    except Exception as e:
        print(f"{n}-user")
        print(e)


c_ustun_qiymati = data.iloc[0, 2]  # 1-qatordan qiymat olish (1-satr, C ustun)
print(f"C ustunidagi qiymat: {c_ustun_qiymati}")