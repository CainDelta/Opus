import pandas as pd
import random
from faker import Faker
import os
from sqlalchemy import create_engine
import sqlite3
import pathlib

if __name__ == '__main__':



    # cd = pd.read_csv(r"C:\Users\ThinkPad\Desktop\alpha\Daisy\data\GBCounties.csv")
    # cd.rename(columns={"ctyua16nm":"County"},inplace=True)
    #
    # ###Apply weights to different areas to skew result
    # cities = ['North Yorkshire','Cardiff','Merseyside','Liverpool','Birmingham','Lancashire','Leicester','Lincolnshire','Gloucester','West Midlands','Devon','Oxford','Northumberland','Surrey','Suffolk','Greater London']
    # cd['weight'] = cd.County.apply(lambda x : 5 if x in(cities) else 2 )
    #
    # os.getcwd()
    # #Get Weights and list of counties
    # county_names = cd.County.tolist()
    # weights = cd.weight.tolist()

    ##Create database connection
    sqlcon = sqlite3.connect('./data/exercise1.db')
    faker = Faker('en_GB')


    #os.chdir('.\Chelete/Daisy')
    #Lockdown’s Effect on Activity Levels

    sample_size = 5000
    q1=[]
    waves = ['wave 1','wave 2', 'wave 3','wave 4','wave 5', 'wave 6']
    for i in range(5000):
        for wave in waves:
            q1.append((random.choice(['more','less']),random.choices(['male','female'],weights=[10,7])[0],wave, random.choices(county_names,weights=weights)[0]))

    q1_df = pd.DataFrame(q1, columns=['Answer', 'Gender','Wave','County'])


    #Lockdowns effect on on desire for fitness improvement
    sample_size = 7000
    q2 = []
    Ages = pd.DataFrame(list(range(16,80)),columns=['Age'])
    Ages['weight'] = Ages.Age.apply(lambda x : 10 if x in list(range(24,35)) else 6 ) #adjust 24-36 Group
    Ages['weight'] = Ages.apply(lambda x : 9 if x['Age'] in list(range(16,24)) else x['weight'] ,axis=1) ##Adjust 16-24 age group
    Agelist = Ages.Age.tolist()
    WeightList = Ages.weight.tolist()


    for i in range(sample_size):
        q2.append((random.choices(Agelist,weights=WeightList)[0],random.choice(['yes','no']),random.choices(county_names,weights=weights)[0]))

    q2_df = pd.DataFrame(q2, columns=['Age', 'Response','County'])

    ##Types of exercise during Lockdown
    exercise_types = ['Running','Home Workouts','Walking','Cycling','Other']
    sample_size = 6000

    q3=[]
    for i in range(sample_size):
        q3.append((faker.date_between(start_date=pd.to_datetime('01-01-2020'), end_date=pd.to_datetime('06-06-2021')),random.choice(exercise_types),random.choices(county_names,weights=weights)[0]))

    q3_df = pd.DataFrame(q3, columns=['Date', 'Activity','County'])


    ###Digital platforms for Online workouts
    sample_size = 8173
    platforms = ['App','Youtube','Zoom','Instagram Live','Facebook live']
    q4 = []
    for i in range(sample_size):
        q4.append((faker.date_between(start_date=pd.to_datetime('01-01-2020'), end_date=pd.to_datetime('06-06-2021')),
        random.choices(platforms,weights=[8,5,2,1,0.2])[0],random.choices(county_names,weights=weights)[0]))

    q4_df = pd.DataFrame(q4, columns=['Date', 'Platform','County'])
    perc_q4 = q4_df.groupby(["Platform"]).describe().reset_index().droplevel(1,axis=1)
    q4 = perc_q4.iloc[:, 0:2].rename(columns={'Date':'Count'})
    q4['%'] = (q4['Count']/q4['Count'].sum())*100


    ###Lockdown Sales trend
    equipment = ['Home Bikes','Elliptical Trainer','Trampoline','Biking','Stepper','Step','Treadmills','Equipment Accessories','Rower','Jump Rope']
    size = 21403
    q5=[]
    for i in range(size):
        q5.append((faker.date_between(start_date=pd.to_datetime('01-01-2019'), end_date=pd.to_datetime('06-06-2020')),random.choice(equipment),random.choices(county_names,weights=weights)[0]))

    q5_df = pd.DataFrame(q5, columns=['Date', 'Equipment','County'])


    ###AFTER LOCKDOWN TRENDS
    workout_location = ['home','gym','home + gym']
    size = 7123
    q6=[]
    for i in range(size):
        q6.append((faker.date_between(start_date=pd.to_datetime('01-01-2019'), end_date=pd.to_datetime('06-06-2020')),
        random.choices(workout_location,weights=[3,6,12])[0],random.choices(county_names,weights=weights)[0]))
    q6_df = pd.DataFrame(q6, columns=['Date', 'Workout Answer','County'])


    likelihood = ['likely','unlikely']
    membership = ['members','non-members']

    size = 1929
    q7=[]
    for i in range(size):
        member = random.choices(membership,weights=[5,1])[0]
        if(member == 'non-members'):
            q7.append((faker.date_between(start_date=pd.to_datetime('01-01-2019'), end_date=pd.to_datetime('06-06-2020')),'non-member',
                random.choices(likelihood,weights=[3,7])[0],random.choices(county_names,weights=weights)[0]))
        else:
            q7.append((faker.date_between(start_date=pd.to_datetime('01-01-2019'), end_date=pd.to_datetime('06-06-2020')),'member',
                random.choices(likelihood,weights=[8,2])[0],random.choices(county_names,weights=weights)[0]))

    q7_df = pd.DataFrame(q7, columns=['Date','Membership', 'Likelihood','County'])


    A8 = ['A' + str(i) for i in range(1,7)]
    Answers = {'A1':'As Soon as it opens',
               'A2':"Once I've seen how its complying with government regulations",
               'A3':'When I get back to my normal routine',
               'A4':"Once I've been reassured by feedback from others",
               'A5':'Once there is a vaccine',
               'A6':"I dont think i'll be  going back"}

    size = 5981
    q8=[]
    for i in range(size):
        q8.append((faker.date_between(start_date=pd.to_datetime('01-01-2019'), end_date=pd.to_datetime('06-06-2020')),
        random.choices(A8,weights=[10,7,2,1.7,1.4,1])[0],random.choices(county_names,weights=weights)[0]))



    q8_df = pd.DataFrame(q8, columns=['Date','Answer','County'])
    q8_df['Label'] = q8_df['Answer'].apply(lambda x: Answers[x])
    q2_group = q2_df.groupby('County')['Response'].describe().reset_index()


    #### Q10 ##############33

    ##how postcodes were generated, file not included because its too big but trimmed version is Q11.csv and is provided
    # postcodes = pd.read_csv(r"C:\Users\ThinkPad\Downloads\postcodes.csv")
    # counties = ['North Yorkshire','Merseyside','Lancashire','Lincolnshire','Gloucestershire','West Midlands','Devon','Oxfordshire','Northumberland','Surrey','Suffolk','Greater London']
    # postcode_trimmed = postcodes[postcodes['County'].isin(counties)]
    # survey = postcode_trimmed.sample(13000)
    # # survey.to_csv('q11.csv',index=False)
    # survey = pd.read_csv('q11.csv')
    survey = pd.read_sql('select * from q11',sqlcon)
    survey_list = list(zip(survey.Latitude.tolist(),survey.Longitude.tolist()))

    ###Function returns Gym visits and label
    Ages = pd.DataFrame(list(range(16,80)),columns=['Age'])
    Ages['weight'] = Ages.Age.apply(lambda x : 10 if x in list(range(24,35)) else 6 ) #adjust 24-36 Group
    Ages['weight'] = Ages.apply(lambda x : 9 if x['Age'] in list(range(16,24)) else x['weight'] ,axis=1) ##Adjust 16-24 age group
    Agelist = Ages.Age.tolist()
    WeightList = Ages.weight.tolist()
    ##locality
    def generateLabel(age):

        ##Generate label based on age with the assumption older people are less likely to live closer to the gym
        habits = ['Regular Gym Goer','Casual Gym Goer','Competitive','Ultra Gym Goer','Rarely visit Gym']
        avg_visits_habit = {'Regular Gym Goer':(50,100),'Casual Gym Goer':(6,50),'Competitive':(101,250),'Ultra Gym Goer':(251,300),'Rarely visit Gym':(0,5)}
        if(age <= 24):
            label = random.choices(habits,weights=[10,8,7,6,5])[0]
            (min,max) = avg_visits_habit[label] #get min and maximum gym visits from visits_habit dictionary
            visits = round(random.uniform(min,max),2) ##get number of visits float
            return visits,label

        elif(age >= 25 and age <= 35):
            label = random.choices(habits,weights=[8,7,8,4,6])[0]
            (min,max) = avg_visits_habit[label] #get min and maximum gym visits from visits_habit dictionary
            visits = round(random.uniform(min,max),2) ##get number of visits float
            return visits,label
        elif(age >= 36 and age <= 50):
            label = random.choices(habits,weights=[5,5,3,1,8])[0]
            (min,max) = avg_visits_habit[label] #get min and maximum gym visits from visits_habit dictionary
            visits = round(random.uniform(min,max),2) ##get number of visits float
            return visits,label
        elif(age >= 51 and age <= 61):
            label = random.choices(habits,weights=[3,3,2,0.5,13])[0]
            (min,max) = avg_visits_habit[label] #get min and maximum gym visits from visits_habit dictionary
            visits = round(random.uniform(min,max),2) ##get number of visits float
            return visits,label
        else:
            label = random.choices(habits,weights=[0.5,0.5,0,0,15])[0]
            (min,max) = avg_visits_habit[label] #get min and maximum gym visits from visits_habit dictionary
            visits = round(random.uniform(min,max),2) ##get number of visits float
            return visits,label
    def generateDistance(age):

        ##Generate distance based on age with the assumption older people are less likely to live closer to the gym
        distance = [1,2,3,4,5,6]
        if(age <= 24):
             return(random.choices(distance,weights=[10,8,7,3,1,1])[0])
        elif(age >= 25 and age <= 35):
            return(random.choices(distance,weights=[10,9,8,4,3,2])[0])
        elif(age >= 36 and age <= 50):
            return(random.choices(distance,weights=[6,7,9,10,8,8])[0])
        elif(age >= 51 and age <= 61):
            return(random.choices(distance,weights=[4,3,5,7,10,10])[0])
        else:
            return(random.choices(distance,weights=[2,2,5,12,14,15])[0])
    def localityGen(distance):
        if(distance == 1):
            return round(random.uniform(1,2),2)
        elif(distance == 2):
            return round(random.uniform(2,3),2)
        elif(distance == 3):
            return round(random.uniform(3,4),2)
        elif(distance == 4):
            return round(random.uniform(4,5),2)
        elif(distance == 5):
            return round(random.uniform(5,6),2)
        else:
            return round(random.uniform(6,10),2)

    respondents = []
    habits = ['Regular Gym Goer','Casual Gym Goer','Competitive','Ultra Gym Goer','Rarely visit Gym']

    for i in survey_list:
        age = random.choices(Agelist,weights=WeightList)[0]
        #locality = localityGen(random.choices(distance,weights=[33,27,22,14,3,1])[0])
        locality = localityGen(generateDistance(age))
        (visits_per_year,habit_label) = generateLabel(age) ##takes distance/locality and generates visits and habit label
        respondents.append((age,random.choice(['more','less']),random.choices(['male','female'],weights=[10,7])[0],habit_label,visits_per_year,locality,i))

    survey_respondents = pd.DataFrame(respondents, columns=['Age','Q2','Gender','Habit','Gym Visits','Distance to Gym','coords'])
    survey_respondents[['Lat', 'Long']] = pd.DataFrame(survey_respondents['coords'].tolist(), index=survey_respondents.index)
    survey_respondents['Lat'] = survey_respondents['Lat'].astype(float)
    survey_respondents['Long'] = survey_respondents['Long'].astype(float)
    survey_respondents.drop(['coords'],inplace=True,axis=1)
    survey_respondents['Habit Code'] = survey_respondents.Habit.map({'Regular Gym Goer':3,'Casual Gym Goer':2,'Competitive': 4,'Ultra Gym Goer': 5,'Rarely visit Gym':1})

    q10_df = survey_respondents


    ####EXPORT TO DATABASE
    q1_df.to_sql(name='q1',con=sqlcon,if_exists='replace')
    q2_df.to_sql(name='q2',con=sqlcon,if_exists='replace')
    q3_df.to_sql(name='q3',con=sqlcon,if_exists='replace')
    q4_df.to_sql(name='q4',con=sqlcon,if_exists='replace')
    q5_df.to_sql(name='q5',con=sqlcon,if_exists='replace')
    q6_df.to_sql(name='q6',con=sqlcon,if_exists='replace')
    q7_df.to_sql(name='q7',con=sqlcon,if_exists='replace')
    q8_df.to_sql(name='q8',con=sqlcon,if_exists='replace')
    q10_df.to_sql(name='q10',con=sqlcon,if_exists='replace',index=False)






    ##EXport TO CSV
    # q1_df.to_csv('Q1.csv',index=False)
    # q2_df.to_csv('Q2.csv',index=False)
    # q3_df.to_csv('Q3.csv',index=False)
    # q4_df.to_csv('Q4.csv',index=False)
    # q5_df.to_csv('Q5.csv',index=False)
    # q6_df.to_csv('Q6.csv',index=False)
    # q7_df.to_csv('Q7.csv',index=False)
    # q8_df.to_csv('Q8.csv',index=False)
