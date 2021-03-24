from selenium.webdriver.common.by import By

SQL_EDITOR_URL = 'https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all'

RUN_SQL_BTN = (By.XPATH, "//button[contains(text(),'Run SQL')]")

RESULT_SQL_TABLE = (By.XPATH, "//div[@id='divResultSQL']//table")

RESULT_AFFECTED_SPAN = (By.XPATH, "//div[contains(text(),'You have made changes to the database')]")
