from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import random 

def randomSelectChoice(driver, element):
    div_selection = driver.find_element(*element)
    options = div_selection.find_elements(By.TAG_NAME, 'option')[1:]
    randomly_selection = random.choice(options).text

    select = Select(div_selection)
    select.select_by_visible_text(randomly_selection)

    print(randomly_selection)
    return randomly_selection
    