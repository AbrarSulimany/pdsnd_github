import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    city = input("Would you like to see data for Chicago, New York city or Washington? \n").lower().strip()
    while(city not in cities):
        city = input("invalid city name! please enter a valid city name:\n").lower().strip()

    # TO DO: get user input for month (all, january, february, march, april, may, june)

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Which month? January, February, March, April, May, June or all. \n").lower().strip()
    while(month not in months):
        month = input("invalid month name! please enter a valid month name: \n").lower().strip()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input("Which day of week? sunday, monday, tuesday, wednesday, thursday, friday, saturday \n").lower().strip()
    while(day not in days):
        day = input("invalid day number! please enter a valid day number: \n").lower().strip()

    print('-'*40)
    return (city, month, day)

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month
    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df.loc[df['month'] == month]

    # filter by day of week
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
    except:
        print("no gender data")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df["Birth Year"].min()
        recent_birth_year = df["Birth Year"].max()
        popular_birth_year = df["Birth Year"].mode()
    except:
        print("no year of birth data")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        #Display row data
    while True:
        display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if display_data.lower() != 'yes':
            break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)




    if __name__ == "__main__":
      	main()
