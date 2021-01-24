def format_one():
    year = 2021
    event = 'Referendum'
    print(f'Results of the {year} {event}')


def format_two():
    yes_notes = 42_572_654
    no_notes = 43_132_495
    percentage = yes_notes / (yes_notes + no_notes)
    print('{:-9} YES votes  {:2.2%}'.format(yes_notes, percentage))


if __name__ == '__main__':
    # format_one()
    format_two()