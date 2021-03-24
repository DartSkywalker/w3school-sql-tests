import pytest

"""
File for storing test data is a workaround. Will be better to use a database
or test data provider services
"""

CUSTOMERS_CITY_ROWS_NUM_DATA = [
    ('London', 6),
    ('Madrid', 3),
    pytest.param('Berlin', 2, marks=pytest.mark.xfail)
]

CUSTOMERS_NAME_ADDRESS_DATA = [
    ('Giovanni Rovelli', 'Via Ludovico il Moro 22'),
    pytest.param('Thomas Hardy', 'Some Incorrect address', marks=pytest.mark.xfail),
]

CUSTOMERS_TABLE_ROW_DATA = [
    {
        'CustomerID': 10,
        'CustomerName': 'Nuclear Power Plant',
        'ContactName': 'Homer Simpson',
        'Address': '742 Evergreen Terrace',
        'City': 'Springfield',
        'PostalCode': '123456',
        'Country': 'USA'
    },
    {
        'CustomerID': 10,
        'CustomerName': 'Springfield Municipal School',
        'ContactName': '₿♀Rt S1mps∅n',
        'Address': '742 Evergreen Terrace',
        'City': 'Springfield',
        'PostalCode': '123456',
        'Country': 'Mexico'
    }
]
