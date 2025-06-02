import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? Thi0s should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    males = df[df['sex']=="Male"]
    average_age_men = round(males['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education']=="Bachelors"]) / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df[
        ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) &
        (df['salary'] == '>50K')
    ])
    lower_education = len(df[
        ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate']) & 
        (df['salary'] == '>50K')
    ])

    # percentage with salary >50K
    higher_education_rich = round(higher_education / df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0] * 100, 1)
    lower_education_rich = round(lower_education / df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week']==min_work_hours) & (df['salary']=='>50K')].shape[0]

    rich_percentage = round(num_min_workers / df[df['hours-per-week']==min_work_hours].shape[0] * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_percents = pd.Series(index=df['native-country'].unique(), dtype=float)
    for i in country_percents.index: 
        country_percents[i] = round(
            (df[(df['native-country'] == i) & (df['salary'] == '>50K')].shape[0] / 
            df[df['native-country'] == i].shape[0]) * 100, 1)

    highest_earning_country = country_percents.idxmax()
    highest_earning_country_percentage = country_percents.max()

    # Identify the most popular occupation for those who earn >50K in India.
    occ_IN = df[(df['native-country']=='India') & (df['salary']=='>50K')]['occupation'].value_counts()
    top_IN_occupation = occ_IN.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
