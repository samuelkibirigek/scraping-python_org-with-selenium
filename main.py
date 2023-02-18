from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:/Users/Sam/Desktop/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu li")

events_dictionary = {}
for event in events:
    date = event.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]
    the_event = event.find_element(By.CSS_SELECTOR, "a").text
    index = events.index(event)

    events_dictionary[f"{index}"] = {
        "time": date,
        "name": the_event
    }

# event_dict = {f"{events.index(event)}": {{"time": f'event.find_element(By.TAG_NAME, "time").get_attribute("datetime").split("T")[0]'}, {"name": f'event.find_element(By.CSS_SELECTOR, "a").text'}} for event in events}

print(events_dictionary)

driver.quit()

