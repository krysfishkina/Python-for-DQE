import re
import datetime
import sys
import os
from Task4 import normalize_text


class Select:
    def __init__(self):
        self.input_type = input("""Please select input type:
                                1 - Input
                                2 - Load from file
                                3 - Exit
    """)
        if self.input_type == '1':
            self.type_of_publication = input(f"""Please select type or exit (Enter digit):
                            1 - News
                            2 - Private Ad
                            3 - Weather forecast with wishes
                            4 - Exit
""")
        elif self.input_type == '2':
            self.folder_choose = input(f"""Please select folder for file:
                                        1 - Default Folder
                                        2 - User provided file path
            """)
            self.count_of_publications = int(input('Please input count of publications from file'))
            if self.folder_choose == '1':
                self.file_path = sys.path[1]
            elif self.folder_choose == '2':
                self.file_path = input(r"Please enter path to file (format C:\) ")
            self.source_file_name = input('Please enter file name\n')
        elif self.input_type == '3':
            sys.exit()

    def read_from_file(self):
        self.source_file_path = os.path.join(self.file_path, self.source_file_name)
        self.source_file = open(self.source_file_path, 'r').read()
        self.text_from_file = re.split("\\n\\n", self.source_file)
        return self.text_from_file

    def write_from_file(self, file_name="News.txt"):
        with open(file_name, "a") as file:
            if self.count_of_publications > 0:
                for i in self.text_from_file:
                     if self.text_from_file.index(i) < self.count_of_publications:
                        file.write(i + '\n\n')
            os.remove(self.source_file_path)


class Publication:
    def __init__(self):
        self.content = ''
        self.date = datetime.datetime.now()
        self.text_of_publication = normalize_text(input(f'Please enter the text:\n'))

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
    if select_type.input_type == '1':
        if select_type.type_of_publication == '1':
            News().write_to_file()
        elif select_type.type_of_publication == '2':
            Ads().write_to_file()
        elif select_type.type_of_publication == '3':
            WeatherForecastWithWishes().write_to_file()
    elif select_type.input_type == '2':
        select_type.read_from_file()
        select_type.write_from_file()