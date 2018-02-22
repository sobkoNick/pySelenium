class UserPageLocators:
    SUBMIT_BTN = "//*[@name='submit']"
    CHECKBOXES_IN_TABLE = "//*[@id='maintable']/tbody/tr/td[1]"
    CHECKBOXES_IN_TABLE_WITH_ID = '//*[@type="checkbox" and @id=%s]'
    MODIFY_BUTTONS_IN_TABLE = "//*[@id='maintable']/tbody/tr/td[8]"
    VIEW_BUTTONS_IN_TABLE = "//*[@id='maintable']/tbody/tr/td[7]"
    TABLE_ROWS = "//tr[@name='entry']"
    DELETE_BTN = "//*[@value='Delete']"
