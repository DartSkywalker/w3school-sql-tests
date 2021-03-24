import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators.sql_editor_locators import *
from utils.constants import *


class SqlEditor:
    """
    Page object for W3SCHOOL SQL Editor page
    """

    def __init__(self, browser):
        self.browser = browser

    def __get_result_table(self):
        """
        Parse results html table into pandas dataframe
        :return: Pandas dataframe
        """
        results_table = WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(
            EC.visibility_of_element_located(RESULT_SQL_TABLE))
        try:
            dfs = pd.read_html(results_table.get_attribute('outerHTML'))
            data_frame = dfs[0]
            return data_frame
        except (AttributeError, KeyError) as e:
            print(e, "Result table is empty or does not exist")

    def __insert_sql_query(self, sql_query):
        """
        Insert SQL query into CodeMirror editor using JS
        :param sql_query: str
        """
        self.browser.execute_script(f'window.editor.setValue("{sql_query}")')

    def __get_table_as_dict(self):
        """
        Parse results html table into dict
        :return: dict
        """
        table = self.__get_result_table()
        return table.to_dict(orient='records')

    def get(self):
        """
        Load W3SCHOOL SQL Editor page
        """
        self.browser.get(SQL_EDITOR_URL)

    def run_sql_query(self):
        """
        Click on RUN SQL button
        """
        self.browser.find_element(*RUN_SQL_BTN).click()

    def get_table_address_by_contact_name(self, contact_name):
        """
        Get Address field by ContactName
        :param contact_name: str
        :return: str
        """
        table = self.__get_result_table()
        return table['Address'][table['ContactName'] == contact_name].values[0]

    def set_query_to_filter_by_city(self, city):
        """
        Set SQL query to get all from Customers table filtered by City field
        :param city: str
        """
        self.__insert_sql_query(f"SELECT * FROM Customers WHERE City='{city}'")

    def set_query_to_select_all_from_customers(self):
        """
        Set SQL query to get all from Customers table
        """
        self.__insert_sql_query("SELECT * FROM Customers")

    def set_query_to_insert_row(self, data):
        """
        Set SQL query to insert new row to Customers table
        :param data: dict of row data
        """
        self.__insert_sql_query(f"INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) "
                                f"VALUES ('{data['CustomerName']}', '{data['ContactName']}', '{data['Address']}',"
                                f" '{data['City']}', '{data['PostalCode']}', '{data['Country']}')")

    def set_query_to_update_row(self, data):
        """
        Set SQL query to update row in Customers table
        :param data: dict of row data
        """
        self.__insert_sql_query(f"UPDATE Customers SET CustomerName='{data['CustomerName']}', "
                                f"ContactName='{data['ContactName']}', Address='{data['Address']}',"
                                f" City='{data['City']}', PostalCode='{data['PostalCode']}', Country='{data['Country']}'"
                                f" WHERE CustomerID={data['CustomerID']};")

    def set_query_to_delete_row_by_id(self, data):
        """
        Set SQL query to delete row from Customers table
        :param data: dict of row data
        """
        self.__insert_sql_query(f"DELETE FROM Customers WHERE CustomerID='{data['CustomerID']}'")

    def get_table_length(self):
        """
        Get length of Customers table
        :return: int
        """
        table = self.__get_result_table()
        return len(table.index)

    def if_db_affected(self):
        """
        Assertion method to check whether table was updated
        by the information message
        :return: boolean
        """
        try:
            WebDriverWait(self.browser, DEFAULT_WAIT_TIME).until(EC.visibility_of_element_located(RESULT_AFFECTED_SPAN))
            return True
        except TimeoutError as e:
            print(e)
            return False

    def if_row_updated(self, data):
        """
        Assertion method to check whether row was updated
        :param data: dict of row data
        :return: boolean
        """
        table_dict = self.__get_table_as_dict()
        return data in table_dict

    def if_row_inserted(self, data):
        """
        Assertion method to check whether row was inserted
        :param data: dict of row data
        :return: boolean
        """
        table_dict = self.__get_table_as_dict()
        # Copying dict to avoid data mutations for further checks
        data_to_check = data.copy()
        data_to_check['CustomerID'] = len(table_dict)
        return data_to_check in table_dict

    def if_row_deleted(self, data):
        """
        Assertion method to check whether row was deleted
        :param data: dict of row data
        :return: boolean
        """
        table_dict = self.__get_table_as_dict()
        return data not in table_dict
