import re
import pandas as pd

categories = {

    r"McDonald|McDonalds|KFC|Burger King|Cafe|Restaurant|Pizza|Subway|Greggs|GDK|Starbucks|Cotti\+Coffee|Nandos|Wagamama|Yangtze": "Eating Out",

    r"Rescue Rooms|Roxy Ball Room|Bunk|Slug & Lettuce|Revolution|Yates|Walkabout|Wetherspoon": "Night Out",

    r"Asda|Tesco|Sainsbury|Lidl|Aldi|Co-op|Coop|Morrisons|Boots|Superdrug|WH Smith|T J Morris|Savers|Paper Kisses|Supermarkets|Lawson Store|Argos": "Groceries",

    r"Foreign|Conversion Fee|Overdraft|Interest": "Bank Charges",

    r"Shell|BP|Esso|Petrol|Garage|Trainline|Bus|Taxi|Uber|Travel|Translink|Arriva": "Transport",

    r"Netflix|Spotify|Disney|Amazon Prime|Cinemas|Cinema|YouTube|Now|Showcase|Odeon|Prime Video": "Entertainment",

    r"Primark|H&M|H & M|Zara|Next|Clothes|Clothing|Boux Avenue|Ann Summers|Lucy and Yak": "Clothes",

    r"Plum|Monzo Savings|Savings": "Savings",
    r"Parking|Car Park|NCP|Mipermit": "Parking",
    r"Steam|Epic Games|Xbox|PlayStation|Nintendo|Game": "Games",
    r"Student Loan|SLC|Student Finance": "Student Loans",
    r"Salary|PAYE|Wages|Transfer from|Refund": "Income",
    r"Faster Payment|Transfer to|Transfer from|Ruby Holmes|Lee-Roy Dobson": "Transfers",
    r"BT|Sky|Virgin|EE|Vodafone|O2|Gas|Electric|Water": "Bills",
}


def categorise(desc):
    for pattern, cat in categories.items():
        if re.search(pattern, str(desc), re.IGNORECASE):
            return cat
    return "Other"

df = pd.read_excel('Statement_cleaned.xlsx')
df['Category'] = df['Description'].apply(categorise)

def total_per_category(df):
    return df.groupby("Category", as_index=False).agg(
        {
            "Money In": "sum",
            "Money Out": "sum"
        }
    ).sort_values(by="Money Out", ascending=False)

# remove transfers as a category, and any associated money in/outs
df = df[df['Category'] != 'Transfers']

print(total_per_category(df).to_string())

#print(df[["Description", "Category"]].to_string())