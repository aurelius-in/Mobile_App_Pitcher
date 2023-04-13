# import necessary libraries
import pandas as pd
import tensorflow as tf
from src.data_preprocessing import preprocess_data
from src.app_ideas_generation import generate_app_ideas

# In this app.py file, the necessary libraries are imported, including pandas,
# tensorflow, and the custom modules from the src directory. The investor data 
# is loaded from the processed_data directory, and the raw data is preprocessed 
# using the preprocess_data function from the data_preprocessing.py module. The 
# machine learning model is loaded from the models directory, and the generate_app_ideas 
# function from the app_ideas_generation.py module is used to generate personalized app ideas.
# Finally, the generated app ideas are saved to a csv file in the processed_data directory.
# This app.py file can be executed to generate personalized app ideas for potential investors 
# based on the given project plan.

# load investor data from processed_data directory
investor_data = pd.read_csv("data/processed_data/investor_data.csv")

# preprocess the raw data
social_media_data = pd.read_csv("data/raw_data/social_media_data.csv")
news_articles_data = pd.read_csv("data/raw_data/news_articles_data.csv")
company_websites_data = pd.read_csv("data/raw_data/company_websites_data.csv")
processed_data = preprocess_data(social_media_data, news_articles_data, company_websites_data)

# load machine learning model from models directory
machine_learning_model = tf.keras.models.load_model("data/models/machine_learning_model.pkl")

# use the machine learning model to generate personalized app ideas
app_ideas = generate_app_ideas(processed_data, investor_data, machine_learning_model)

# save the generated app ideas to a csv file in the processed_data directory
app_ideas.to_csv("data/processed_data/app_ideas.csv", index=False)
