from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

df = pd.read_excel(r'C:\Users\xmari\PycharmProjects\selenium_rpachallange\data\challenge.xlsx', index_col=None, header=0)
print(df)
print("---------------")

driver.get('https://www.rpachallenge.com/')
driver.maximize_window()

start = driver.find_element("xpath", "//button[@class='waves-effect col s12 m12 l12 btn-large uiColorButton' and text()='Start']")

print(start.get_attribute("innerHTML"))
start.click()

wait = WebDriverWait(driver, 10)


for i in range(10):
    address = wait.until(EC.presence_of_element_located(("xpath", "//label[text()='Address']/following-sibling::input")))
    address.send_keys(df['Address'][i])

    email = wait.until(EC.presence_of_element_located(("xpath", "//label[text()='Email']/following-sibling::input")))
    email.send_keys(df['Email'][i])

    lastName = wait.until(EC.presence_of_element_located(("xpath", "//label[text()='Last Name']/following-sibling::input")))
    lastName.send_keys(df['Last Name '][i])

    phoneNumber = wait.until(EC.presence_of_element_located(("xpath", "//label[text()='Phone Number']/following-sibling::input")))
    phoneNumber.send_keys(str(df['Phone Number'][i]))

    roleInCompany = wait.until(EC.presence_of_element_located(("xpath", "//label[text()='Role in Company']/following-sibling::input")))
    roleInCompany.send_keys(df['Role in Company'][i])

    companyName = wait.until(EC.presence_of_element_located(("xpath", "//label[text()='Company Name']/following-sibling::input")))
    companyName.send_keys(df['Company Name'][i])

    firstName = wait.until(EC.presence_of_element_located(("xpath", "//label[text()='First Name']/following-sibling::input")))
    firstName.send_keys(df['First Name'][i])

    wait.until(EC.presence_of_element_located(("xpath", "//label[text()='First Name']/following-sibling::input")))
    submit = wait.until(EC.presence_of_element_located(("xpath", "//input[@value='Submit']")))
    submit.click()

print("---------------")
testResults = wait.until(EC.presence_of_element_located(("xpath", "//div[@class='message2']")))
print(testResults.get_attribute("innerHTML"))
print("---------------")