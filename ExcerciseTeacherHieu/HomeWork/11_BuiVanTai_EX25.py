import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/anhdung98/diem_thi_2022/main/diem_thi_thpt_2022.csv"
df = pd.read_csv(url)
total_candidates = len(df)
print("Total candidates nationwide: ", total_candidates)
foreign_lang_candidates = len(df[df["ngoai_ngu"].notnull()])
print("Total candidates taking the foreign language exam: ", foreign_lang_candidates)
quang_ninh_candidates = len(df[df["sbd"].astype(str).str[:2] == "17"])
print("Total candidates taking the exam at the Quang Ninh: ",
      quang_ninh_candidates)

quang_ninh_df = df[df["sbd"].astype(str).str[:2] == "17"]
quang_ninh_df = quang_ninh_df[["ngu_van", "ngoai_ngu", "vat_li", "dia_li"]].notnull().astype(int).sum()
quang_ninh_df.plot(kind="bar")
ax = quang_ninh_df.plot(kind="bar")
for i, v in enumerate(quang_ninh_df):
    ax.text(i - 0.15, v + 100, str(v), color='blue', fontweight='bold')
plt.title("Number of candidates taking exams at the Quang Ninh Department of Education and Training")
plt.xlabel("Subjects")
plt.ylabel("Number of candidates")
plt.show()
