import pandas as pd
import numpy as np
import datetime
# working on version control-branch -refactoring

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    EndSt = df["End Station"].copy()
    
    # concatenating team with name column 
    # overwriting name column 
    df["trips"] = df["Start Station"].str.cat(EndSt, sep =" - ") 

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def display_stats(s,e):
    the_months = ['january', 'february', 'march', 'april', 'may', 'june']
    the_days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    print("Hello Let\'s explore some US Bikeshare Data!")
    city = ""
    
    while True:
        city   = input("Would you like to see data for chicago,new york city or washington ?").lower()
        if city in CITY_DATA:
                filter_answer = input("Would you like to filter the data by month,day,both or not at all? type none if you don\'t need time filter :").lower()
                if(filter_answer=="both"):
                    m  = input("which Month ? january,february,march,may or june :").lower()
                   
                    if(m=="january" or m=="february" or m=="march" or m=="may" or m=="june"):
                        d  = input("which day ?Please type your response as string e.g, sunday or monday :").lower()
                        if(d=="monday" or d=="tuesday" or d=="wednesday" or d=="thusday" or d=="friday" or d=="saturday" or d=="sunday"):
                                db=load_data(city,m,d)
                                u  = input("Do you wish to see 5 lines of raw data ? Yes or No :").lower()
                                if(u=="yes"):
                                    print("Raw data:")
                                    print("------------------------------------")
                                    print(db.iloc[s:e]) 
                                    print("------------------------------------") 
                                else:
                                    print("------------------------------------") 
                                print("Statistics :filter by both Month and Day")
                                print("------------------------------------")
                                print("Popular Times of Travel:")
                                print("     Common Month       :",db['month'].value_counts().idxmax())
                                print("     Common day of week :",db['day_of_week'].value_counts().idxmax())
                                print("     Common hour of day :",db['hour'].value_counts().idxmax())
                                print("Popular Station and trip:")
                                print("     Common start station :",db['Start Station'].value_counts().idxmax())
                                print("     Common end station   :",db['End Station'].value_counts().idxmax())
                                print("     Common trip from start to end:",db['trips'].value_counts().idxmax())
                                print("Trip duration:")
                                print("      Total travel time:",db['Trip Duration'].sum())
                                print("      Average travel time:",db['Trip Duration'].mean())
                                print("User count info:")
                                print("      By type:")
                                print(db['User Type'].value_counts())
                                if 'Gender' in db.columns:
                                    print("By gender:")
                                    print(db['Gender'].value_counts())
                                else:
                                    print ("Gender data not found") 
                                if 'Birth Year' in db.columns:
                                    print("Common year of birth:",db['Birth Year'].value_counts().idxmax())
                                else:
                                    print ("Birth Year data not found")
                        else:
                            print("unknow day")  
                    else:
                        print("unknow month") 
                elif(filter_answer=="month"):
                    m  = input("which Month ? january,february,march,may or june :").lower()
                    if(m=="january" or m=="february" or m=="march" or m=="may" or m=="june"):
                                db=load_data(city,m,"all")
                                u  = input("Do you wish to see 5 lines of raw data ? Yes or No :").lower()
                                if(u=="yes"):
                                    print("Raw data:")
                                    print("------------------------------------")
                                    print(db.iloc[s:e]) 
                                    print("------------------------------------") 
                                else:
                                    print("------------------------------------") 
                                print("Statistics :filter by both Month and Day")
                                print("------------------------------------")
                                print("Popular Times of Travel:")
                                print("     Common Month       :",db['month'].value_counts().idxmax())
                                print("     Common day of week :",db['day_of_week'].value_counts().idxmax())
                                print("     Common hour of day :",db['hour'].value_counts().idxmax())
                                print("Popular Station and trip:")
                                print("     Common start station :",db['Start Station'].value_counts().idxmax())
                                print("     Common end station   :",db['End Station'].value_counts().idxmax())
                                print("     Common trip from start to end:",db['trips'].value_counts().idxmax())
                                print("Trip duration:")
                                print("      Total travel time:",db['Trip Duration'].sum())
                                print("      Average travel time:",db['Trip Duration'].mean())
                                print("User count info:")
                                print("      By type:")
                                print(db['User Type'].value_counts())
                                if 'Gender' in db.columns:
                                    print("By gender:")
                                    print(db['Gender'].value_counts())
                                else:
                                    print ("Gender data not found") 
                                if 'Birth Year' in db.columns:
                                    print("Common year of birth:",db['Birth Year'].value_counts().idxmax())
                                else:
                                    print ("Birth Year data not found")
                    else:
                        print("unknow month") 
                elif(filter_answer=="day"):
                    d  = input("which day ?Please type your response as string e.g, sunday or monday :").lower()
                    if(d=="monday" or d=="tuesday" or d=="wednesday" or d=="thusday" or d=="friday" or d=="saturday" or d=="sunday"):
                                db=load_data(city,"all",a)
                                u  = input("Do you wish to see 5 lines of raw data ? Yes or No :").lower()
                                if(u=="yes"):
                                    print("Raw data:")
                                    print("------------------------------------")
                                    print(db.iloc[s:e]) 
                                    print("------------------------------------") 
                                else:
                                    print("------------------------------------")
                                print("Statistics :filter by both Month and Day")
                                print("------------------------------------")
                                print("Popular Times of Travel:")
                                print("     Common Month       :",db['month'].value_counts().idxmax())
                                print("     Common day of week :",db['day_of_week'].value_counts().idxmax())
                                print("     Common hour of day :",db['hour'].value_counts().idxmax())
                                print("Popular Station and trip:")
                                print("     Common start station :",db['Start Station'].value_counts().idxmax())
                                print("     Common end station   :",db['End Station'].value_counts().idxmax())
                                print("     Common trip from start to end:",db['trips'].value_counts().idxmax())
                                print("Trip duration:")
                                print("      Total travel time:",db['Trip Duration'].sum())
                                print("      Average travel time:",db['Trip Duration'].mean())
                                print("User count info:")
                                print("      By type:")
                                print(db['User Type'].value_counts())
                                if 'Gender' in db.columns:
                                    print("By gender:")
                                    print(db['Gender'].value_counts())
                                else:
                                    print ("Gender data not found") 
                                if 'Birth Year' in db.columns:
                                    print("Common year of birth:",db['Birth Year'].value_counts().idxmax())
                                else:
                                    print ("Birth Year data not found")
                    else:
                        print("unknow day") 
                elif(filter_answer=="none"):
                                db=load_data(city,"all","all")
                                u  = input("Do you wish to see 5 lines of raw data ? Yes or No").lower()
                                if(u=="yes"):
                                    print("Raw data:")
                                    print("------------------------------------")
                                    print(db.iloc[s:e]) 
                                    print("------------------------------------") 
                                else:
                                    print("------------------------------------")
                                print("Statistics :filter by both Month and Day")
                                print("------------------------------------")
                                print("Popular Times of Travel:")
                                print("     Common Month       :",db['month'].value_counts().idxmax())
                                print("     Common day of week :",db['day_of_week'].value_counts().idxmax())
                                print("     Common hour of day :",db['hour'].value_counts().idxmax())
                                print("Popular Station and trip:")
                                print("     Common start station :",db['Start Station'].value_counts().idxmax())
                                print("     Common end station   :",db['End Station'].value_counts().idxmax())
                                print("     Common trip from start to end:",db['trips'].value_counts().idxmax())
                                print("Trip duration:")
                                print("      Total travel time:",db['Trip Duration'].sum())
                                print("      Average travel time:",db['Trip Duration'].mean())
                                print("User count info:")
                                print("      By type:")
                                print(db['User Type'].value_counts())
                                if 'Gender' in db.columns:
                                    print("By gender:")
                                    print(db['Gender'].value_counts())
                                else:
                                    print ("Gender data not found") 
                                if 'Birth Year' in db.columns:
                                    print("Common year of birth:",db['Birth Year'].value_counts().idxmax())
                                else:
                                    print ("Birth Year data not found") 
                else:
                    print("unknow filter")     
                break    
        else: 
             print("Entered city is not in our database")  
t_start=0
t_end=5
while True:
    
    display_stats(t_start,t_end)
    option = input("Would you like to restart? yes/no :").lower()
    t_start=t_end
    t_end=t_end+5
    if option == "no":
         break