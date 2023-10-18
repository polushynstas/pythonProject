from datetime import datetime

class Person:
    def __init__(self, first_name, last_name=None, middle_name=None, birth_date=None, death_date=None, gender=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date)
        self.gender = gender

    def parse_date(self, date_str):
        if date_str:
            cleaned_date_str = date_str.replace(" ", ".").replace("-", ".").replace(",", ".").replace("/", ".")
            formats = ["%d.%m.%Y"]
            for format in formats:
                try:
                    return datetime.strptime(cleaned_date_str, format).date()
                except ValueError:
                    pass
        return None


    def calculate_age(self, reference_date=None):
        reference_date = reference_date or datetime.now().date()
        birth_date = self.birth_date
        if birth_date:
            if not self.death_date:
                return reference_date.year - birth_date.year - ((reference_date.month, reference_date.day) < (birth_date.month, birth_date.day))
            else:
                return self.death_date.year - birth_date.year - ((self.death_date.month, self.death_date.day) < (birth_date.month, birth_date.day))
        return None

    def display_info(self):
        info = f'{self.first_name} {self.middle_name} {self.last_name}' if self.middle_name else f'{self.first_name} {self.last_name}'
        info += f', {self.calculate_age()} років, {self.gender}.'

        gender_message = "Народився" if self.gender == "m" else "Народилась"

        info += f' {gender_message} {self.birth_date.strftime("%d.%m.%Y")}'
        if self.death_date:
            info += f', Помер{self.death_date.strftime(" %d.%m.%Y")}'
        print(info)
