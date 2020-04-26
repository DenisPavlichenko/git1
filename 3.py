from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://rozetka.com.ua/')

# Ищем поле для поиска
search = driver.find_element_by_xpath("//input[starts-with(@class, 'search-form__input')]")

# время будет держать паузу 5 секунд
time.sleep(5)
search.send_keys('lucky me') # Вводит нужный нам текст в поле input

# кликает по нужной нам кнопки button "Найти" метод патч, тег button и копируем class (@-не забыть указать class)
auto_complete = driver.find_elements_by_xpath(
    "//button[starts-with(@class, 'button button_color_green button_size_medium search-form__submit')]")
auto_complete[0].click()
time.sleep(5)

link = driver.find_element_by_link_text('Контакты') # метод клика по ссылке элемент по гипер ссылке с текстом
time.sleep(5)
link.click()
driver.quit()
