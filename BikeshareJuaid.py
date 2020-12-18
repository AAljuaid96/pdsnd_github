import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \nRemember, a helmet today keeps concussion away :)')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Choose a city: (Chicago, NYC, or Washington) ").lower().strip()
    while (city not in ["chicago", "nyc", "washington"]): 
       input("invalid city input, please only choose between: (Chicago, NYC, or Washington) ").lower().strip()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    filter_by = input("filter data by: (month, day, both, neither) ").lower().strip()
    if (filter_by == "both"):
        month = input("Choose a month: (All, January, February, or... June) ").lower().strip()
        day = input("Choose a day: (All, Monday, Tuesday, or...) ").lower().strip()
    elif (filter_by == "month"):
        month = input("Choose a month: (All, January, February, or... June) ").lower().strip()
    elif (filter_by == "day"):
        day = input("Choose a day: (All, Monday, Tuesday, or...) ").lower().strip()
    else:
        pass
   
    print('-'*40)
    return city, month, day

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
    # data filtered by city
    #print(city)
    df = pd.read_csv(CITY_DATA[city])

    # From string Start Time and End Time to datetime (learned from https://docs.python.org/3/library/datatypes.html)
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    
    # Day and month columns 
    df["day"] = df["Start Time"].dt.day_name()
    df["month"] = df["Start Time"].dt.month_name()
    
    #print(day + " " + month)
    #print(df.to_string(index=False))
    #print(df[['day', 'month']].head(5))
    #print(df['day'].head(5))
    #print(df['month'].head(5))
    #print(df.shape, 'shape')
    #In case of filtering
    
    if(month != "all"):
        df = df[df["month"]  == month.title()]
        
    if(day != "all"):
        df = df[df["day"] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #print(df.size)
    #print(df.shape)
    most_common_month = df["month"].mode()[0]
    print("The most common month: {}".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df["day"].mode()[0]
    print("The most common day: {}".format(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df["Start Time"].dt.hour.mode()[0]
    print("The most common start hour: {}".format(most_common_hour))
    # (helped me with refreshing my mind about the syntax https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print("The most common start station: {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print("The most common end station: {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df["combination of stations"] = df["Start Station"] + " " + df["End Station"]
    most_freq_combination = df["combination of stations"].mode()[0]
    print("The most frequent combination of start station and end station: " + str(most_freq_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("The total travel time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("The average travel time: {}".format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The user types count:\n{}".format(user_types))
    
    # (while I was refreshing my mind about .mode() I saw .value_count too. Here is the reference again https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html)

    if city != "washington":
        
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The user gender count:\n{}".format(gender))

        # TO DO: Display earliest, most recent, and most common year of birth
        eldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        most_common_age = df['Birth Year'].mode()[0]
        print("eldest user's birth year: {}".format(eldest))
        print("Youngest user's birht year: {}".format(youngest))
        print("Most common birth year of users: {}".format(most_common_age))
    # Refactoring idea 1 (try and except is my section lead's, Yaqeen Almahdi, idea :) is another way to do it too)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        
        # Refactoring idea 2 (can be def outside main()) In case user wants to see raw data
        raw_data = input("Interested to see the raw trip data? (yes, no) ").lower().strip()
        
        if(raw_data == "no"):
            print("happily, you are not curious enough :)")
        elif(raw_data == "yes"):
            start_row = 0
            end_row = 5
            while(raw_data == "yes"):
                display_rows = df.iloc[start_row:end_row]
                start_row += 5
                end_row += 5
                print(display_rows)
                
                raw_data = input("More raw data rows? (yes, no) ").lower().strip()
                if(raw_data == "no"):
                    break
        else:
            pass
                  
        restart = input('\nWould you like to restart? (yes, no).\n')
        if restart.lower().strip() != 'yes':
            print("See you again!")
            break

if __name__ == "__main__":
	main()
