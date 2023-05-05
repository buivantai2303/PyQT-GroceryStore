import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/anhdung98/diem_thi_2022/main/diem_thi_thpt_2022.csv"
df = pd.read_csv(url)

# Create a data frame df_HCM containing the list of examinees at Ho Chi Minh City Examination Council, whose first 2 digits of the registration number (sbd) are "02".
df_HCM = df[df['sbd'].astype(str).str[:1] == "2"]

# Print to the screen the number of examinees who have taken part in the exam at Ho Chi Minh City Examination Council.
print("Number of examinees who have taken part in the exam at Ho Chi Minh City Examination Council: ", len(df_HCM))

# Print to the screen the number of examinees who have the sum score of mathematics (toan) and physics (vat_li) lower than 5 at the Ho Chi Minh City Examination Council. Display on the screen the list of these examinees.
low_score_examinees = df_HCM[df_HCM['toan'] + df_HCM['vat_li'] < 5.0]
print(
    "Number of examinees who have the sum score of mathematics (toan) and physics (vat_li) lower than 5 at the Ho Chi Minh City Examination Council: ",
    len(low_score_examinees))
print(low_score_examinees)

# Calculate, then compare, the average (mean) foreign languages scores of Ho Chi Minh City Examination Council with those of Quang Ninh. Display the result on the screen.
HCM_avg_foreign_lang = df_HCM['ngoai_ngu'].mean()
QN_avg_foreign_lang = df[df['sbd'].astype(str).str[:2] == "17"]['ngoai_ngu'].mean()
print("The mean of HCM City: ", HCM_avg_foreign_lang)
print("The mean of QN City: ", QN_avg_foreign_lang)

if HCM_avg_foreign_lang > QN_avg_foreign_lang:
    print(
        "The average foreign languages score of Ho Chi Minh City Examination Council is higher than those of Quang Ninh.")
elif HCM_avg_foreign_lang < QN_avg_foreign_lang:
    print(
        "The average foreign languages score of Ho Chi Minh City Examination Council is lower than those of Quang Ninh.")
else:
    print(
        "The average foreign languages score of Ho Chi Minh City Examination Council is equal to those of Quang Ninh.")

# Draw the histogram of the mathematics score of Ho Chi Minh City Examination Council.
plt.hist(df_HCM['toan'])
plt.title("Histogram of Mathematics Scores of Ho Chi Minh City Examination Council")
plt.xlabel("Mathematics Score")
plt.ylabel("Number of Examinees")


# Add a function to show the average in the top of the column chart
def show_average(df, column):
    average = df[column].mean()
    plt.axhline(average, color='red', linestyle='dashed', label='Average: {}'.format(average))
    for i, v in enumerate(plt.gca().get_children()[-1].get_children()):
        plt.text(v.get_x() + v.get_width() / 2, v.get_height() + 5,
                 str(int(df[column].value_counts().sort_index().iloc[i])), ha="center", va="bottom", fontsize=8)


# Show the average in the top of the column chart
show_average(df_HCM, 'toan')

plt.show()