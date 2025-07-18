from selenium.webdriver.common.by import By


class Locators:

    #кнопка куков
    cookie_button = [By.XPATH, './/button[text()="да все привыкли"]']
    #раздел "Вопросы о важном"
    faq_section = [By.XPATH, '//div[@class = "Home_FAQ__3uVm4"]']
    #кнопки с вопросами

    button_q = {
        0 : [By.XPATH, '//div[@id="accordion__heading-0"]'],
        1 : [By.XPATH, '//div[@id="accordion__heading-1"]'],
        2 : [By.XPATH, '//div[@id="accordion__heading-2"]'],
        3 : [By.XPATH, '//div[@id="accordion__heading-3"]'],
        4 : [By.XPATH, '//div[@id="accordion__heading-4"]'],
        5 : [By.XPATH, '//div[@id="accordion__heading-5"]'],
        6 : [By.XPATH, '//div[@id="accordion__heading-6"]'],
        7 : [By.XPATH, '//div[@id="accordion__heading-7"]']
    }
    #ответы на вопросы
    answers = {
        0 : [By.XPATH, '//div[@id="accordion__panel-0"]'],
        1 : [By.XPATH, '//div[@id="accordion__panel-1"]'],
        2 : [By.XPATH, '//div[@id="accordion__panel-2"]'],
        3 : [By.XPATH, '//div[@id="accordion__panel-3"]'],
        4 : [By.XPATH, '//div[@id="accordion__panel-4"]'],
        5 : [By.XPATH, '//div[@id="accordion__panel-5"]'],
        6 : [By.XPATH, '//div[@id="accordion__panel-6"]'],
        7 : [By.XPATH, '//div[@id="accordion__panel-7"]']
    }

    #кнопка заказа вверху страницы
    high_button_order = (By.XPATH, '//button[text()="Заказать"]')
    #кнопка заказа внизу страницы
    low_button_order = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text() = "Заказать"]')

    #для первой формы заказа
    #поле "Имя"
    field_name = (By.XPATH, '//input[@placeholder = "* Имя"]')
    #поле "Фамилия"
    field_lastname = (By.XPATH, '//input[@placeholder = "* Фамилия"]')
    #поле "Адрес"
    fiels_adress = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]')
    #поле "Станция метро"
    field_subway = (By.XPATH, '//input[@placeholder = "* Станция метро"]')
    #выпадающий список станций метро
    list_of_subway = (By.XPATH, '//div[@class="select-search__select"]')
    #поле "Телефон"
    field_phone = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]')
    #кнопка "Далее"
    button_next = (By.XPATH, '//button[text() = "Далее"]')



    #для второй формы заказа
    #поле "Когда привезти самокат"
    field_when = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]')
    #поле "Срок аренды"
    field_long = (By.XPATH, '//div[@class ="Dropdown-root"]')
    #кнопка выбора суточной аренды из списка
    set_how_long = (By.XPATH, '//div[text()="сутки"]')
    #чекбокс "черный цвет самоката
    checkbox_color = (By.XPATH, '//input[@id="black"]')
    #поле "Комментарий для курьера"
    field_comment = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')
    #кнопка "Заказать"
    button_2f_last = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text()="Заказать"]')


    #кнопка подтверждния оформления заказа
    button_yes = (By.XPATH, '//button[text()="Да"]')
    #кнопка "Посмотреть статус"
    button_status = (By.XPATH, '//button[text()="Посмотреть статус"]')

    #лого "Самокат"
    logo_scooter = (By.XPATH, '//img[@alt="Scooter"]')
    #лого "Яндекс"
    logo_yandex = (By.XPATH, '//img[@alt = "Yandex"]')
    #значок дзена
    logo_dzen = (By.XPATH, '//div[@class ="dzen-layout--desktop-base-header__logoContainer-pu dzen-layout--desktop-base-header__isMorda-2n"]')