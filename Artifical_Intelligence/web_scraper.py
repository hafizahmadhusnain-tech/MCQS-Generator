import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st



url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
print(soup)


books = []

for book in soup.select(".product_pod"):

    title = book.h3.a["title"]

    price = book.select_one(".price_color").text

    availability = book.select_one(".availability").text.strip()

    price = float(price.replace("£", "").replace("Â", "").strip())

    books.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })


df = pd.DataFrame(books)

st.title("Book Price Finder")

st.write("Books collected using Web Scraping")

st.dataframe(df)


max_price = st.slider(
    "Select Maximum Price",
    min_value=0.0,
    max_value=60.0,
    value=30.0
)


filtered_books = df[df["Price"] <= max_price]


st.subheader("Books Within Your Budget")

st.dataframe(filtered_books)


st.write(
    "Number of books found:",
    len(filtered_books)
)