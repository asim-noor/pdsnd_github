#Bikeshare project is Udacity course requirement.
#It explore bikeshare data of three cities of USA. 
#Reading data, cleaning data, analysing data, and visualization are the major tasks
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = {'all':111, 'january': 1, 'february': 2, 'march': 3,
             'april': 4, 'may': 5, 'june':6}
DAY_DATA = {'all':0, 'monday':1, 'tuesday':2, 'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}

def get_month(month):
    for key, value in MONTH_DATA.items():
        if value == month:
            return key.title()
			

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n provide all input in small case')
    # getting user input for city (chicago, new york city, washington). 

    # while loop to get city input correctly 
    while True:
        try:
            city = input("city - name of the city to analyze 'washington' or 'new york city' or 'chicago': ")
            if city.lower() in CITY_DATA:
                break
        except:
            print('Incorrect city try again in except block')
        else: 
            print('Incorrect city try again')
      
    
<<<<<<< .merge_file_a14176
    #get user input for month (all, january, february, ... , june)
    #while loop to get input month
||||||| .merge_file_a15232
    #get user input for month (all, january, february, ... , june)
    #second while loop to get input month
=======
    #get user input for month (all, january, february, ... , june)
    #while loop to get  month input correctly
>>>>>>> .merge_file_a07492
    #get user input for month (all, january, february, ... , june)
    #while loop to get  month input correctly
    while True:
        try:
            month = input("month - name of the month (january to june) to filter by, or 'all' to apply no month filter: ")
            if month.lower() in MONTH_DATA:
                break
        except:
            print('Incorrect Month try again')
        else: 
            print('Incorrect month try again')

 #getting user input for day of week (all, monday, tuesday, ... sunday)
 #while loop to get 'day of month' input correctly
    while True:
        try:
            day = input("day - name of the day of week to filter by, or 'all' to apply no day filter: ")
            if day.lower() in DAY_DATA:
                break
        except:
            print('Incorrect day try again in except block')
        else: 
            print('Incorrect day try again')

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
    month = month.title()
    day = day.title()
    city = CITY_DATA.get(city)
    if month == 'All' and day =='All':
        df = pd.read_csv(city)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
    elif month != 'All' and day =='All':
        df = pd.read_csv(city)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df =df.loc[df['Start Time'].dt.month == MONTH_DATA.get(month.lower()),:]
    elif month =='All' and day !='All':
        df = pd.read_csv(city)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df =df.loc[df['Start Time'].dt.weekday_name == day,:]
    elif month !='All' and day !='All':
        df = pd.read_csv(city)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time'] = pd.to_datetime(df['End Time'])
        df =df.loc[df['Start Time'].dt.month == MONTH_DATA.get(month.lower()),:]
        df =df.loc[df['Start Time'].dt.weekday_name == day,:]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displaying the most common month
    month_df = df['Start Time'].dt.month.value_counts().head(1)

    month = month_df.index
    
    print('The most common month is: {}.'.format(get_month(month[0])))

    # displaying the most common day of week
    dow = df['Start Time'].dt.weekday_name.value_counts().head(1)
    print('The most common day of week is: {}.'.format(dow))

    # displaying the most common start hour
    hr = df['Start Time'].dt.hour.value_counts().head(1)
    print('The most common Start Hours is: {}.'.format(hr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # displaying most commonly used start station
    print('The most commonly used Start Station is: ', df.loc[:,'Start Station'].value_counts().head(1))
    
    # displaying most commonly used end station
    df.loc[:,'End Station'].value_counts().head(1)

    # displaying most frequent combination of start station and end station trip
    print('The most commonly used End Station is: ', df.loc[:,'End Station'].value_counts().head(1))
   
    df_temp = pd.crosstab(df['Start Station'], df['End Station'])
    ind =0
    col =0
    col_val = 0
    for c in df_temp.columns:
        if col_val < df_temp.loc[:,c].max():
            col_val = df_temp.loc[:,c].max()
            col = c
            ind = df_temp[c].idxmax()

    print('The most commone trip is between: ', ind, " and ", col, 'with ', col_val, 'trips between the stations')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displaying total travel time
       
    total  = df['Trip Duration'].sum()
    minutes = total / 60
    hours = minutes / 60
    days = hours /24
    print('Total trips duration in Seconds is: {}, in Minutes is: {}, in Hours {},  and in Days is: {}'.format(a, minutes, hours, days))
         

    # Tdisplaying mean travel time
    
    avg  = df['Trip Duration'].mean()
    print("Mean trip duration in seceonds is; ", avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # displaying counts of user types
    print('Counts of user Types:\n', df['User Type'].value_counts())
   
    if 'Gender' in df.columns:
        # displaying counts of gender
        print('Gender Count:\n', df['Gender'].value_counts())

        # displaying earliest, most recent, and most common year of birth
        min_year = df['Birth Year'].min()
        max_year = df['Birth Year'].max()
        avg_year = df['Birth Year'].mean()
        print('Minimum Birth Year is: {}, Maximum Birth Year is{},  and Mean Birth Year is {}'.format(int(min_year), int(max_year), int(avg_year)))
    else:
        print('No gender or birth year data available for the city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_raw_data(df):
#it diplays raw dat in cremental fashion to the enduser. They can enter yes to view more data or enter No to quit the function.  
    num = 0
    choice = input("Enter yes if you want to see raw data")
    if choice.lower() =='yes':
        while True:
            num = num + 5
            print(df.head(num))
            continue_or_not = input('\nWould you like to see more raw data? Enter yes or no.\n')
            if continue_or_not.lower() !='yes':
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
