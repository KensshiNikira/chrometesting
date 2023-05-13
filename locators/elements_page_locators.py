from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "input[id='#output #name']")
    CREATED_EMAIL = (By.CSS_SELECTOR, "input[id='#output #email']")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='#output #currentAddress']")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='#output #permanentAddress']")
    CREATED_SUBMIT = (By.CSS_SELECTOR, "button[id='#output #submit']")