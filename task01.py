from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    # реалізація класу
    required_num_of_digits = 10

    def __init__(self, phone=None):
        # Перевіряємо чи всі введені дані є цифрами і чи їх кількість відповідає заданому формату
        try:
            if int(phone) and len(phone) == Phone.required_num_of_digits:
                super().__init__(phone)
            else:
                print("Less that 10 digits")
        except:
            print("All characters are not digits")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p for p in self.phones)}"

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone).value)
        except AttributeError:
            print(f"Phone number format is incorrect and was not added.")

    def edit_phone(self, old_number, new_number):
        # Робимо редагування номеру. У разі відсутності обробляємо помилку.
        try:
            index = self.phones.index(old_number)
            self.phones[index] = new_number
        except ValueError:
            print(
                f"Not changed. {old_number} not found in the list of phones.")

    def find_phone(self, phone):
        # Робимо перевірку присутності телефону. У разі відсутності обробляємо помилку.
        try:
            index = self.phones.index(phone)
            return self.phones[index]
        except ValueError:
            return "Phone not found"

    def remove_phone(self, phone):
        # Видаляємо запис. У разі його відсутності, обробляємо виняток.
        try:
            del self.phones[phone]
        except KeyError:
            print(f"Cannoe remove phone. {phone} not found in record.")


class AddressBook(UserDict):
    # реалізація класу

    def add_record(self, record):
        # Робимо перевірку наявності запису в адресній книзі, щоб запобігти дублюванню
        record_exists = list(
            filter(lambda contact: contact == record.name.value, self.data))
        if record_exists:
            print(
                f"Record with name {record.name.value} already exist in address book.")
        else:
            self.data[record.name.value] = record

    def find(self, name):
        # Робимо перевірку присутності запису в адресній книзі. У разі відсутності обробляємо помилку.
        try:
            return self.data[name]
        except KeyError:
            print(f"{name} not found in the address book.")
            return None

    def delete(self, name):
        # Видаляємо запис. У разі його відсутності, обробляємо виняток.
        try:
            del self.data[name]
        except KeyError:
            print(f"Record {name} not found in the address book.")


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")


if __name__ == "__main__":
    main()
