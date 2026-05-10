import pandas as pd 

df = pd.read_csv("C:\\SkillGap Analytics Job Market & Talent Demand Intelligence\\DataAnalyst.csv")

#print(df.head())

#print(df.columns)

#print(df.info)

#print(df.drop('Unnamed: 0', axis=1, inplace=True))

#print(df.info)

df.drop_duplicates(inplace=True)

df['Company Name'] = df['Company Name'].str.split('\n').str[0]


#print(df['Salary Estimate'].head())

skills = ['Python', 'SQL', 'Excel', 'Power BI', 'Tableau', 'R']

df['Salary Estimate'] = df['Salary Estimate'].str.replace('(Glassdoor est.)', '', regex=False)

df[['Min Salary', 'Max Salary']] = df['Salary Estimate'].str.split('-', expand=True)

def extract_skills(text):
    found_skills = []

    for skill in skills:
        if skill.lower() in str(text).lower():
            found_skills.append(skill)

    return ', '.join(found_skills)

df['Skills'] = df['Job Description'].apply(extract_skills)


#print(df)

#df.to_csv("Cleaned_DataAnalyst.csv", index=False)

df = pd.read_csv("DataAnalyst.csv", index_col=0)  # kills Unnamed:0
df['Job Description'] = df['Job Description'].str.replace('\n', ' ', regex=False)
df.to_csv("DataAnalyst_clean.csv", index=False)  # clean export


#print(df)

from sqlalchemy import create_engine

# Step 1: Load and clean
df = pd.read_csv("DataAnalyst_clean.csv")

# Drop unnamed index column
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Strip all newlines/carriage returns from every column
for col in df.select_dtypes(include='str').columns:
    df[col] = df[col].str.replace('\n', ' ', regex=False).str.replace('\r', ' ', regex=False)


df['Salary Estimate'] = df['Salary Estimate'].str.replace('(Glassdoor est.)', '', regex=False)

df['Salary Estimate'] = df['Salary Estimate'].str.replace('$', '', regex=False)

df['Salary Estimate'] = df['Salary Estimate'].str.replace('K', '', regex=False)

# Step 2: Connect to MySQL and push directly
engine = create_engine("mysql+mysqlconnector://root:liveptrak@127.0.0.1:3306/job_market_analysis")

df.to_sql("jobs", con=engine, if_exists="replace", index=False)

print("Done. Rows inserted:", len(df))
