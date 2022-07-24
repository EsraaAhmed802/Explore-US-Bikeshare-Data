import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
   
        print('Hello! Let\'s explore some US bikeshare data!')
        cities_data=('chicago','new york','washington')
        city = input(" Enter The City From This Cites to see Data (chicago , new york , washington) \n").lower()
        while (city not in cities_data):
            city = input(" Please Enter The Valid City \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
        
        monthes_data = ['january', 'february', 'march', 'april', 'may', 'june','all']    
        while True:
            month = input(" Enter The Month (all, january, february, ... , june) to Filter The Months or 'ALL' to Apply No Month Filter \n").lower()
            if month in monthes_data:
                break
            else:
                print ("\n SORRY, this is not Valid \n")
                
            
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
      
        days_data = ['monday' , 'tuesday' , 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday','all' ]    
        while True:
            day = input(" Enter The Day to Filter The Days or 'ALL' to Apply No Day Filter \n").lower()
            if day in days_data:
                break
            else:
                print ("\n SORRY, this is not Valid \n")    
            


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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = pd.DatetimeIndex(df['Start Time']).day_name() 
    # extract hour from Start Time to create new columns
    df['Hour']=df['Start Time'].dt.hour
    
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day Of Week'] == day.title()]
    
    return df
   

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].value_counts().idxmax()
    print('The Most Common Month is : ',common_month)

    
    # TO DO: display the most common day of week
    common_day = df['Day Of Week'].value_counts().idxmax()
    print('The Most Common Day Of Week is : ', common_day)


    # TO DO: display the most common start hour
    common_hour = df['Hour'].value_counts().idxmax()
    print('The Most Common Start Hour is : ', common_hour)
    
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The Most Commonly Used Start Station is : ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The Most Commonly Used End Station is : ', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_frequent = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The Most Frequent Combination Of Start Station And End Station Trip is : ', common_frequent)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The Total Travel Time is : ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The Mean Travel Time is : ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The Counts of User Types is :  ', df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if (city =='chicago') or (city =='new york'):
        print('The Counts of Gender is :  ',df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
        print('The Earliest Year Of Birth is : ',int(df['Birth Year'].min()))
        print('The Most Recent Year Of Birth is : ',int(df['Birth Year'].max()))
        print('The Most Common Year Of Birth is : ',int(df['Birth Year'].mode()[0]))
    else:
        print('There is no Data about Gender in this City')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def display_data(df):
    start_loc = 0
    View_Data=['yes','no']
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    if view_data not in View_Data:
        print('please enter valid choice \n')
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    elif view_data == 'no':
        print('Thank You')
    else: 
       while start_loc+5 < df.shape[0]:
            print(df.iloc[start_loc:start_loc+5])
            start_loc+=5
            view_data = input('\nWould you like to view more 5 rows of individual trip data? Enter yes or no\n').lower()
            if view_data == 'no':
               print('Thank You')
               break
    
    start_loc = 0
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
