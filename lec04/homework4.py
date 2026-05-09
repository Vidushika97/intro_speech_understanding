def next_birthday(date, birthdays):
    '''
    Find the next birthday after the given date.

    @param:
    date - a tuple of two integers specifying (month, day)
    birthdays - a dict mapping from date tuples to lists of names

    @return:
    birthday - the next day after given date on which somebody has a birthday
    list_of_names - list of all people with birthdays on that date
    '''

    sorted_birthdays = sorted(birthdays.keys())

    for birthday in sorted_birthdays:
        if birthday > date:
            return birthday, birthdays[birthday]

    first_birthday = sorted_birthdays[0]
    return first_birthday, birthdays[first_birthday]


# Example
birthdays = {
    (1, 10): ["Alice"],
    (5, 20): ["Bob", "Charlie"],
    (12, 25): ["David"]
}

print(next_birthday((5, 21), birthdays))