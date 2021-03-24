from pages.sql_editor import SqlEditor
from utils.test_base import *


@pytest.mark.parametrize("name, address", CUSTOMERS_NAME_ADDRESS_DATA)
def test_customers_table_address_for_user(browser, name, address):
    """
    Verify the correctness of Address field for
    CustomerName records in Customers table
    """
    se = SqlEditor(browser)
    se.get()

    se.run_sql_query()
    current_address = se.get_table_address_by_contact_name(name)
    assert current_address == address, \
        f"The address does not match expected result. " \
        f"Expected result- {address}. " \
        f"Actual result - {current_address}"


@pytest.mark.parametrize("city, rows_num", CUSTOMERS_CITY_ROWS_NUM_DATA)
def test_customers_table_for_city(browser, city, rows_num):
    """
    Verify the number of rows for a city in Customers table
    """
    se = SqlEditor(browser)
    se.get()

    se.set_query_to_filter_by_city(city)
    se.run_sql_query()
    table_len = se.get_table_length()
    assert table_len == rows_num, \
        f"Table len is incorrect for {city} city. " \
        f"Actual Result - {table_len}. " \
        f"Expected Result - {rows_num}"


@pytest.mark.parametrize('row_to_insert', CUSTOMERS_TABLE_ROW_DATA)
def test_insert_row_in_customers_table(browser, row_to_insert):
    """
    Verify the ability to insert a new row into Customers table
    """
    se = SqlEditor(browser)
    se.get()

    se.set_query_to_insert_row(row_to_insert)
    se.run_sql_query()

    assert se.if_db_affected(), "Database was not affected"

    se.set_query_to_select_all_from_customers()
    se.run_sql_query()

    assert se.if_row_inserted(row_to_insert), "New row is not found in the table"


@pytest.mark.parametrize('row_to_update', CUSTOMERS_TABLE_ROW_DATA)
def test_update_row_in_customers_table(browser, row_to_update):
    """
    Verify the ability to update a row in Customers table
    """
    se = SqlEditor(browser)
    se.get()

    se.set_query_to_update_row(row_to_update)
    se.run_sql_query()

    assert se.if_db_affected(), "Database was not affected"

    se.set_query_to_select_all_from_customers()
    se.run_sql_query()

    assert se.if_row_updated(row_to_update), "Row is not updated"


@pytest.mark.parametrize('row_to_delete', CUSTOMERS_TABLE_ROW_DATA)
def test_delete_row_in_customers_table(browser, row_to_delete):
    """
    Verify the ability to delete a row in Customers table
    """
    se = SqlEditor(browser)
    se.get()

    se.set_query_to_delete_row_by_id(row_to_delete)
    se.run_sql_query()

    assert se.if_db_affected(), "Database was not affected"

    se.set_query_to_select_all_from_customers()
    se.run_sql_query()

    assert se.if_row_deleted(row_to_delete), "The row is still exist in the Customer table"
