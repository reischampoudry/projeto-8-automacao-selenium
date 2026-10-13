from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class UrbanRoutesPage:
    # LOCALIZADORES

    from_field = (By.ID, "from")
    to_field = (By.ID, "to")

    taxi_option = (
        By.XPATH,
        '//button[contains(text(), "Chamar")]'
    )

    comfort_icon = (
        By.XPATH,
        "//div[contains(@class, 'tcard-title') and text()='Comfort']"
    )

    comfort_active = (
        By.XPATH,
        "//div[contains(@class, 'active')]"
    )

    phone_button = (
        By.XPATH,
        "//div[contains(text(), 'Número de telefone')]"
    )

    phone_field = (By.ID, "phone")

    next_button = (
        By.XPATH,
        "//button[text()='Próximo']"
    )

    payment_method = (
        By.CSS_SELECTOR,
        ".pp-button.filled"
    )

    current_payment_method = (
        By.XPATH,
        "//div[contains(@class,'pp-value-text')]"
    )

    add_card = (
        By.XPATH,
        "//div[contains(text(),'Adicionar cartão')]"
    )

    card_number_field = (
        By.ID,
        "number"
    )

    card_code_field = (
        By.ID,
        "code"
    )

    add_card_button = (
        By.XPATH,
        "//button[text()='Adicionar']"
    )

    comment_field = (
        By.ID,
        "comment"
    )

    blanket_switch = (
        By.CSS_SELECTOR,
        "input.switch-input"
    )

    ice_cream_plus = (
        By.CSS_SELECTOR,
        ".counter-plus"
    )

    ice_cream_value = (
        By.CSS_SELECTOR,
        ".counter-value"
    )

    order_button = (
        By.CSS_SELECTOR,
        "button.smart-button"
    )

    car_search_title = (
        By.XPATH,
        "//div[contains(@class, 'order-header-title')]"
    )

    # CONSTRUTOR

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # MÉTODOS BASE (POM)

    def _find(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def _click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self, locator):
        return self._find(locator).get_attribute("value")

    # ENDEREÇO

    def enter_locations(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_location(self):
        return self._get_value(self.from_field)

    def get_to_location(self):
        return self._get_value(self.to_field)

    # PLANO COMFORT

    def click_taxi_option(self):
        button = self._find(self.taxi_option)

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            button
        )

        button.click()

    def select_comfort_plan(self):
        self._click(self.comfort_icon)

    def is_comfort_selected(self):
        try:
            active_card = self.driver.find_element(
                *self.comfort_active
            )

            return (
                "active"
                in active_card.get_attribute("class")
            )

        except:
            return False

    # TELEFONE

    def click_phone_button(self):
        self._click(self.phone_button)

    def enter_phone_number(self, phone):
        self.click_phone_button()
        self._type(self.phone_field, phone)

    def get_phone_number(self):
        return self._get_value(self.phone_field)

    def click_next_button(self):
        self._click(self.next_button)

    # CARTÃO

    def click_payment_method(self):
        self._click(self.payment_method)

    def click_add_card(self):
        self._click(self.add_card)

    def add_credit_card(self, number, code):

        self.driver.find_element(
            *self.card_number_field
        ).send_keys(number)

        code_fields = self.driver.find_elements(
            *self.card_code_field
        )

        visible_code_field = [
            field for field in code_fields
            if field.is_displayed()
        ][0]

        visible_code_field.send_keys(code)

        visible_code_field.send_keys(Keys.TAB)

        time.sleep(2)

        print(
            "Numero:",
            self.driver.find_element(
                *self.card_number_field
            ).get_attribute("value")
        )

        print(
            "CVV:",
            visible_code_field.get_attribute("value")
        )

        self._click(self.add_card_button)

        time.sleep(2)

    def get_current_payment_method(self):
        return self._get_text(
            self.current_payment_method
        )

    # COMENTÁRIO

    def enter_comment(self, comment):
        self._type(
            self.comment_field,
            comment
        )

    def get_driver_comment(self):
        return self._find(
            self.comment_field
        ).get_attribute("value")

    # COBERTOR E LENÇOS

    def order_blanket_and_handkerchiefs(self):

        element = self.driver.find_element(
            *self.blanket_switch
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def is_blanket_and_handkerchiefs_selected(self):

        return self.driver.find_element(
            *self.blanket_switch
        ).is_selected()

    # SORVETES

    def order_2_ice_creams(self):

        plus_button = WebDriverWait(
            self.driver,
            5
        ).until(
            EC.element_to_be_clickable(
                self.ice_cream_plus
            )
        )

        for _ in range(2):
            plus_button.click()

    def get_ice_cream_count(self):

        values = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".counter-value"
        )

        return values[0].text

    # PEDIDO

    def order_taxi(self):
        self._click(self.order_button)

    def is_search_modal_displayed(self):
        try:
            element = self.driver.find_element(
                *self.car_search_title
            )

            return (
                "Buscar carro"
                in element.text
            )

        except:
            return False