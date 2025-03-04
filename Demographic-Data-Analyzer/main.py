import pandas as pd

def calculate_demographic_data():
    df=pd.read_csv("adult.data.csv")

    race_count = df['race'].value_counts()
    average_age_men = int(df['age'].mean())
    percentage_bachelors=  f"{round(((df['education']=="Bachelors").sum()/df['education'].shape[0])*100,2)}%"
    higher_education_rich = f"{round((((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')).sum() / df['education'].shape[0] * 100, 2)}%"
    lower_education_rich=  f"{round((((df['education']!="Bachelors") & (df['education']!="Masters") & (df['education']!="Doctorate") & (df['salary']==">50K")).sum()/df['education'].shape[0])*100,2)}%"
    min_work_hours= int(df['hours-per-week'].min())
    rich_percentage=f"{round((df[(df['hours-per-week']==1) & (df['salary']==">50K")].shape[0]/df['salary'].shape[0])*100,3)}%"

    paises = list(df['native-country'].unique())

    paises_prctg={}
    for pais in paises:
        prctg = round((df[(df['native-country']==pais) & (df['salary']==">50K")].shape[0]/df[df['native-country']==pais].shape[0])*100,2)
        paises_prctg[pais]=prctg
    highest_earning_country =  max(paises_prctg, key=paises_prctg.get)
    highest_earning_country_percentage = f"{paises_prctg[highest_earning_country]}%"
    top_IN_occupation= df[(df['salary']==">50K")&(df['native-country']=='India')]['occupation'].value_counts().idxmax()
    
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

print(calculate_demographic_data())