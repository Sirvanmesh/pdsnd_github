import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Gets user input for city, month, and day.
    Returns:
        city (str): name of the city to analyze
        month (str): month to filter by or "all"
        day (str): day of week to filter by or "all"
    """
    print("Hello! Let’s explore some US bikeshare data!")

    # Get city input
    while True:
        city = input("Choose a city (Chicago, New York City, Washington): ").strip().lower()
        if city in CITY_DATA:
            break
        print("Invalid city. Please enter a valid city.")

    # Get month input
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Choose a month (January to June) or 'all': ").strip().lower()
        if month in months:
            break
        print("Invalid month. Try again.")

    # Get day input
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Choose a day of the week or 'all': ").strip().lower()
        if day in days:
            break
        print("Invalid day. Try again.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads and filters data based on user selection.
    Returns:
        df (DataFrame): filtered DataFrame
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays the most frequent travel times."""
    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    print("Most Common Month:", df['month'].mode()[0].title())
    print("Most Common Day of Week:", df['day_of_week'].mode()[0].title())
    print("Most Common Start Hour:", df['hour'].mode()[0])

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays the most commonly used stations and trip."""
    print("\nCalculating The Most Popular Stations and Trip...\n")
    start_time = time.time()

    print("Most Common Start Station:", df['Start Station'].mode()[0])
    print("Most Common End Station:", df['End Station'].mode()[0])
    df['Trip'] = df['Start Station'] + " → " + df['End Station']
    print("Most Frequent Trip:", df['Trip'].mode()[0])

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays total and average trip duration."""
    print("\nCalculating Trip Duration...\n")
    start_time = time.time()

    print("Total Travel Time (s):", df['Trip Duration'].sum())
    print("Average Travel Time (s):", df['Trip Duration'].mean())

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\nCalculating User Stats...\n")
    start_time = time.time()

    print("Counts by User Type:\n", df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print("\nCounts by Gender:\n", df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print("\nEarliest Birth Year:", int(df['Birth Year'].min()))
        print("Most Recent Birth Year:", int(df['Birth Year'].max()))
        print("Most Common Birth Year:", int(df['Birth Year'].mode()[0]))

    print("This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    """Displays 5 lines of raw data upon user request."""
    row = 0
    while True:
        view_data = input('\nWould you like to see 5 rows of raw data? Enter yes or no: ').strip().lower()
        if view_data != 'yes':
            break
        print(df.iloc[row:row+5])
        row += 5
        if row >= len(df):
            print("No more data to display.")
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no: ').strip().lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()
