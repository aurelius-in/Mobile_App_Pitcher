import pandas as pd
import os

# The process_raw_data() function reads the raw data from three csv files, drops irrelevant columns,
# and concatenates the data into one data frame. It then drops duplicate rows and saves the processed
# data to a new csv file.

# The clean_app_ideas() function reads the app ideas data, drops rows with missing values, removes special 
# characters and digits from the text, and converts the text to lowercase. It then saves the cleaned app 
# ideas to the same csv file.

# Note that the file paths are constructed using os.path.join() to ensure platform independence.

def process_raw_data():
    # read raw social media data
    social_media_data = pd.read_csv(os.path.join("data", "raw_data", "social_media_data.csv"))

    # drop irrelevant columns and rename remaining columns
    social_media_data = social_media_data.drop(columns=["date", "time"])
    social_media_data = social_media_data.rename(columns={"post": "text", "platform": "source"})

    # read raw news articles data
    news_articles_data = pd.read_csv(os.path.join("data", "raw_data", "news_articles_data.csv"))

    # drop irrelevant columns and rename remaining columns
    news_articles_data = news_articles_data.drop(columns=["author", "published_date"])
    news_articles_data = news_articles_data.rename(columns={"title": "text", "website": "source"})

    # read raw company websites data
    company_websites_data = pd.read_csv(os.path.join("data", "raw_data", "company_websites_data.csv"))

    # drop irrelevant columns and rename remaining columns
    company_websites_data = company_websites_data.drop(columns=["page_url"])
    company_websites_data = company_websites_data.rename(columns={"content": "text", "website": "source"})

    # concatenate all data frames into one
    processed_data = pd.concat([social_media_data, news_articles_data, company_websites_data])

    # drop duplicate rows
    processed_data = processed_data.drop_duplicates(subset=["text"])

    # save processed data to csv
    processed_data.to_csv(os.path.join("data", "processed_data", "investor_data.csv"), index=False)

def clean_app_ideas():
    # read app ideas data
    app_ideas_data = pd.read_csv(os.path.join("data", "processed_data", "app_ideas.csv"))

    # drop rows with missing values
    app_ideas_data = app_ideas_data.dropna()

    # remove special characters and digits from the text
    app_ideas_data["text"] = app_ideas_data["text"].str.replace("[^a-zA-Z]", " ")

    # convert text to lowercase
    app_ideas_data["text"] = app_ideas_data["text"].str.lower()

    # save cleaned app ideas to csv
    app_ideas_data.to_csv(os.path.join("data", "processed_data", "app_ideas.csv"), index=False)
