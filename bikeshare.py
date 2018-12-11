import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    while True:
        city_input = input('Please type your city of choice: ').lower()
        if city_input not in CITY_DATA:
            print("\nSorry, this is not a valid city.\nPlease select between: Chicago, New York City and Washington\n")
            continue
        else:
            city = city_input
            print("\nThank you ! {} is a great city".format(city.title()))
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'abril', 'may', 'june', 'all']

    while True:
        month_input = input('\nNow, please select a month: ').lower()
        if month_input not in months:
            print("\nSorry, this is not a valid month.\nSelect between the months of January to June.\nPlease spell it out like January, February, etc.\nFor all months type 'all'\n")
            continue
        else:
            month = month_input
            print("\nThat's great. Thank you for selecting {} as your month.".format(month.title()))
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']

    while True:
        day_input = input('\nI promise this is the last step.\n\nPlease choose a day of the week: ').lower()
        if day_input not in days:
            print("\nSorry, this is not a valid day of the week.\nPlease spell it out like Monday, Tuesday, etc.\nFor all days type 'all'\n")
            continue
        else:
            day = day_input
            print("\nThank you for selecting {} as your day of the week.\n".format(day.title()))
        break

    print("\nWe're all done now. But before we move on, let's re-cap your selections:")
    print("City: {}\nMonth: {}\nDay of week: {}".format(city.title(),month.title(),day.title()))

    # Ask user if wants to see 5 lines of data for the selected city
    print('\nActually, before we move on, would you like to take a peak at 5 lines of the {} data?\n'.format(city.title()))
    word = input("Please enter 'Y' if you would like to see 5 lines of raw data: \n").lower()
    if word == 'y':
        a = 0
        b = a + 4
        with open(CITY_DATA[city],'r') as f:
            lines = f.readlines()[a:b]
            print(lines)
    # in case answer above was 'Y' - ask user if wants to see 5 more lines of data (loops until the answer is different than 'Y'
        while True:
            word = input("\nWanna see some more? Please enter 'Y' if you would like to see 5 more lines of data: ").lower()
            if word == 'y':
                c = b + 1
                d = c + 4
                with open(CITY_DATA[city],'r') as f:
                    lines = f.readlines()[c:d]
                    print(lines)
                    b = d
                continue
            else:
                print('Finished')
            break

    else:
        print('Finished')

    print('-'*40)
    return city, month, day

#get_filters() - tested and working until here

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
    # load data file into df
    df = pd.read_csv(CITY_DATA[city])

    # convert start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to crate the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month_num = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[popular_month_num - 1].title()
    print('The most common month is: {}\n'.format(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day is: {}\n'.format(popular_day))

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['Start Hour'].mode()[0]
    print('The most common start hour is: {}\n'.format(popular_start_hour))

    print("If you have travel plans avoid {}s in {} around {} o'clock.".format(popular_day, popular_month, popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}\n'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}\n'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = 'Start station-' + df['Start Station'] + ' with ' + 'End station-' + df['End Station']
    popular_start_end = df['Start End'].mode()[0]
    print('The most commonly used combination of Start and End station is: {}'.format(popular_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_hrs = (total_travel_time//60) // 60
    print('The total travel time is approximately: {} hours\n'.format(total_travel_hrs))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    avg_travel_min = avg_travel_time // 60
    print('The average travel time is approximately: {} minutes'.format(avg_travel_min))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('This is how many of each user type there are:\n')
    print(user_types)

    # TO DO: Display counts of gender (only NYC & Chicago)
    # TO DO: Display earliest, most recent, and most common year of birth (only NYC & Chicago)
    if 'Gender' and 'Birth Year' in df.columns:
        gender_types = df['Gender'].value_counts()
        print('\nBelow are also some interesting gender stats.\n')
        print("Here's how many of each gender there are:\n{}".format(gender_types))

        early_byear = df['Birth Year'].min()
        recent_byear = df['Birth Year'].max()
        popular_byear = df['Birth Year'].mode()[0]

        print('\nBelow are also some interesting Bday stats.')
        print("\nHere's the earliest Bday year: {}".format(int(early_byear)))
        print("\nHere's the most recent Bday year: {}".format(int(recent_byear)))
        print("\nHere's the most common Bday year: {}".format(int(popular_byear)))
        print("\nIsn't that some cool information?")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
