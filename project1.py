import pandas as pd
import matplotlib.pyplot as plt

# ============================
# A. Load Data
# ============================

data = {
    'Rank':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
            41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,
            79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,
            113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,
            141,142,143,144,145,146,147,148,149,150,151],
    
    'Country':['Finland','Denmark','Norway','Iceland','Netherlands','Switzerland','Sweden','New Zealand','Canada','Austria',
               'Australia','South Africa','Israel','Afghanistan','United Kingdom','Ireland','Germany','Belgium','United States','Egypt',
               'Zambia','South Sudan','India','Liberia','Taiwan','Chile','Central African Republic','Saudi Arabia','Qatar','Spain','Panama',
               'Brazil','Uruguay','Singapore','El Salvador','Italy','Bahrain','Bangladesh','Iraq','Poland','Armenia','Iran','Colombia',
               'South Africa','Nicaragua','Nepal','Pakistan','Russia','Cyprus','Japan','Kuwait','Thailand','Latvia','South Korea','Estonia',
               'Jamaica','Mauritius','Japan','Honduras','Kazakhstan','Bolivia','Hungary','Paraguay','Northern Cyprus','Peru','Portugal',
               'Pakistan','Russia','Philippines','Serbia','Pakistan','Russia','Philippines','Vietnam','Malaysia','Ivory','Indonesia',
               'Cameroon','Ghana','Nigeria','Albania','Venezuela','Guinea','Georgia','Senegal','Mozambique','Nepal','Gabon','malesia',
               'Honduras','Kenya','Togo','Mali','Sierra Leone','Laos','Libya','Swaziland','Sri Lanka','Cameroon','Congo','Iraq','Benin',
               'Gambia','Burkina Faso','Guinea-Bissau','Namibia','Haiti','Lesotho','Ethiopia','Mauritania','Somalia','Niger','Zambia',
               'Burundi','Uganda','Liberia','Togo','Malawi','Madagascar','Chad','Congo (Kinshasa)','Zimbabwe','Afghanistan','Bolivia',
               'Ecuador','Kyrgyzstan','Montenegro','Colombia','Mongolia','Venezuela','Indonesia','Armenia','Bulgaria','South Africa',
               'North Macedonia','Algeria','Hong Kong SAR of China','Albania','Tajikistan','Mozambique','Georgia','Iraq','Nepal','Laos',
               'Gabon','India','Georgia','Iraq','Nepal','Laos','Gabon'],
    
    'Score':[7.769,7.6,7.554,7.494,7.488,7.48,7.343,7.307,7.278,7.246,7.228,4.722,7.139,3.203,7.054,7.021,6.985,6.923,6.892,4.166,
             4.107,2.853,4.015,3.975,6.446,6.444,3.083,6.375,6.374,6.354,6.321,6.3,6.293,6.262,6.253,6.223,6.199,4.456,4.437,6.182,
             4.559,4.548,6.125,4.722,6.105,4.913,5.653,5.648,6.046,5.886,6.021,6.008,5.94,5.895,5.893,5.89,5.888,5.886,5.86,5.809,
             5.779,5.758,5.743,5.718,5.697,5.693,5.603,5.603,5.809,5.779,5.758,5.19,5.08,5.05,5.04,5.02,5.01,4.98,4.95,4.92,4.9,
             4.88,4.87,4.87,4.85,4.84,4.84,4.81,4.79,4.76,4.75,4.72,4.71,4.69,4.68,4.66,4.65,4.65,4.62,4.61,4.59,4.58,4.57,4.56,
             4.55,4.54,4.51,4.5,4.49,4.48,4.46,4.43,4.42,4.41,4.4,4.39,4.37,4.33,4.32,4.29,4.28,5.78,5.73,5.71,5.71,5.7,5.7,5.61,
             5.57,5.56,5.56,5.51,5.46,5.42,5.37,5.36,5.3,5.22,5.19,5.17,5.16,5.14,5.11,5.22,5.19,5.17,5.16,5.14,5.11],
    
    'Healthy life expectancy':[0.986,0.996,1.028,1.026,0.999,1.052,1.009,1.026,1.039,1.016,1.036,0.469,1.029,0.361,0.996,0.999,0.987,0.986,
                               0.874,0.644,0.426,0.295,0.588,0.443,0.914,0.92,0.105,0.795,0.871,1.062,0.91,0.802,0.891,1.141,0.789,1.039,
                               0.871,0.723,0.574,0.884,0.815,0.785,0.841,0.469,0.835,0.677,0.535,0.726,1.042,1.088,0.808,0.828,0.812,
                               1.036,0.874,0.831,0.798,1.088,0.828,0.729,0.706,0.828,0.777,1.042,0.854,0.999,0.854,0.854,0.987,0.911,
                               0.9,0.694,0.772,0.407,0.672,0.354,0.491,0.359,0.814,0.584,0.339,0.627,0.419,0.366,0.622,0.485,0.738,
                               0.706,0.463,0.274,0.301,0.267,0.598,0.534,0.229,0.725,0.354,0.354,0.49,0.315,0.428,0.323,0.308,0.435,
                               0.407,0.222,0.379,0.431,0.297,0.295,0.308,0.231,0.353,0.292,0.274,0.316,0.36,0.229,0.262,0.334,0.246,
                               1.37,1.5,1.23,1.59,1.51,1.49,1.23,1.36,1.52,1.65,1.65,1.5,1.55,2.05,1.42,1.21,0.81,1.38,1.65,1.06,1.27,
                               1.67,0.81,1.38,1.65,1.06,1.27,1.67],
    
    'Generosity':[0.153,0.252,0.271,0.354,0.322,0.263,0.267,0.33,0.285,0.244,0.332,0.13,0.261,0.158,0.348,0.298,0.261,0.16,0.28,
                  0.076,0.247,0.202,0.2,0.233,0.242,0.187,0.235,0.08,0.22,0.153,0.109,0.099,0.127,0.271,0.093,0.158,0.255,0.166,
                  0.148,0.117,0.095,0.27,0.099,0.13,0.2,0.285,0.22,0.082,0.047,0.069,0.142,0.359,0.075,0.175,0.103,0.107,0.107,
                  0.069,0.246,0.146,0.137,0.081,0.184,0.191,0.083,0.047,0.137,0.137,0.146,0.137,0.081,0.126,0.203,0.098,0.231,
                  0.091,0.178,0.183,0.129,0.052,0.101,0.103,0.137,0.117,0.285,0.076,0.088,0.208,0.198,0.088,0.091,0.147,0.209,
                  0.142,0.106,0.187,0.091,0.091,0.104,0.102,0.155,0.107,0.096,0.099,0.201,0.094,0.134,0.076,0.165,0.103,0.137,
                  0.063,0.151,0.135,0.088,0.16,0.079,0.082,0.101,0.125,0.151,0.67,1.38,1.39,1.5,1.44,1.41,1.51,1.46,1.28,1.15,1.45,
                  1.43,1.02,1.04,1.15,1.27,1.17,1.09,1.19,1.13,1.1,1.4,1.17,1.09,1.19,1.13,1.1,1.4]
}

# Create DataFrame
df = pd.DataFrame(data)

# B. Data Cleaning
print("Initial DataFrame:")
print(df.head())

# 1. Check missing values
df= isnull().sum()
print("\nMissing values: ");

# 2. Drop missing values
df.dropna(inplace=True)

# 3. Remove duplicates
df.drop_duplicates(inplace=True)

# 4. Standardize column names
df.columns = df.columns.str.strip().str.lower()

# 5. Correct inconsistent country names
df['country'] = df['country'].str.strip().str.replace('malesia', 'Malaysia')

# 6. Change data type
df['score'] = df['score'].astype(float)
# C. Data Analysis

print("\nAverage Healthy life expectancy:");
df['healthy life expectancy'].mean()
print("Maximum Score:");
df['score'].max()
print("\nTop 10 Generosity values:\n")
df['generosity'].value_counts()
print("\nTop 10 countries by average score:\n");
df.groupby('country')['score'].mean().sort_values(ascending=False)
print("\nSorted by Country:\n", df.sort_values(by='country'))

# D. Data Visualization

# 1. Bar Chart: Top 10 Countries by Score
top_countries = df.sort_values(by='score', ascending=False).head(10)
plt.figure(figsize=(12,6))
plt.bar(top_countries['country'], top_countries['score'], color='skyblue')
plt.title("Top 10 Countries by Score")
plt.xticks(rotation=45)
plt.ylabel("Score")
plt.show()

# 2. Pie Chart: Score distribution categories
bins = [0, 4, 6, 8]
labels = ['Low (0-4)', 'Medium (4-6)', 'High (6-8)']
df['score_category'].value_counts()
plt.title("Score Distribution")
plt.ylabel("")
plt.show()

# 3. Scatter Plot: Score vs Healthy life expectancy
plt.figure(figsize=(10,6))
plt.scatter(df['score'], df['healthy life expectancy'], color='purple')
plt.title("Score vs Healthy Life Expectancy")
plt.xlabel("Score")
plt.ylabel("Healthy Life Expectancy")
plt.show()

