import datetime
from datetime import date
import sys


class Select:
    def __init__(self):
        self.type_of_publication = input(f"""Please select type or exit (Enter digit):
                            1 - News
                            2 - Private Ad
                            3 - Weather forecast with wishes
                            4 - Exit
""")


class Publication:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.text_of_publication = input(f'Please enter the text:\n')
        self.content = ''

    def write_to_file(self, file_name="News.txt"):
        with open(file_name, "a") as news_feed:
            news_feed.write(self.content)


class News(Publication):
    def __init__(self):
        super().__init__()
        self.city = input('Please enter the city:\n')
        news_date = f"{self.city}, {self.date.strftime('%d/%m/%Y')}"
        self.content = f"News------------------\n{self.text_of_publication}\n{news_date}\n"\
                       f"----------------------\n\n"


class Ads(Publication):
    def __init__(self):
        super().__init__()
        actual_year = int(input('Please enter the year until which the ad will be valid\n'))
        actual_month = int(input('Please enter the month until which the ad will be valid\n'))
        actual_day = int(input('Please enter the day of month until which the ad will be valid\n'))
        actual_date = datetime.date(actual_year, actual_month, actual_day)
        self.ad_actual_date = f"{actual_date.strftime('%d/%m/%Y')}"
        self.count_days_until = (actual_date - self.date.date()).days
        self.content = f"Private Ad------------\n{self.text_of_publication}\nActual until:" \
                       f"{self.ad_actual_date}, {self.count_days_until} days left\n"\
                       f"----------------------\n\n"


class WeatherForecastWithWishes(Publication):  # and the number of days until spring
    def __init__(self):
        super().__init__()
        self.actual_date = f"{self.date.strftime('%d/%m/%Y')}"
        self.country = input("Please enter the country:\n")
        self.city = input("Please enter the city:\n")
        self.temperature = input("Please enter the temperature:\n")
        start_spring = datetime.datetime(2022, 3, 1)
        self.until_spring = (start_spring - self.date).days
        self.content = f"Weather forecast------\nToday {self.actual_date} the weather in {self.country} in the {self.city} city is {self.temperature} degrees Celsius\n" \
                       f"and there are {self.until_spring} days left until spring!\n" \
                       f"Wish for today: {self.text_of_publication}\n" \
                       f"----------------------\n\n"


while True:
    select_type = Select()
    if select_type.type_of_publication == '1':
        News().write_to_file()
    elif select_type.type_of_publication == '2':
        Ads().write_to_file()
    elif select_type.type_of_publication == '3':
        WeatherForecastWithWishes().write_to_file()
    elif select_type.type_of_publication == '4':
        sys.exit()