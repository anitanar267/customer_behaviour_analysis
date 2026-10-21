import pandas as pd
from sqlalchemy import create_engine

# Load CSV
df = pd.read_csv('F:/consumer data/cleaned_data.csv')

# Connect using your MySQL root password
engine = create_engine('mysql+pymysql://root:anitanar%40267@127.0.0.1:3306/portfolio')

# Create table automatically and insert data
df.to_sql('customer_data', con=engine, if_exists='replace', index=False)

print("Done! Table created and populated.")