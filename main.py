import data
import helpers as helpers

from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities

        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {
            "performance": "ALL"
        }

        service = Service(
            ChromeDriverManager().install()
        )

        cls.driver = webdriver.Chrome(
            service=service
        )

        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(
                data.URBAN_ROUTES_URL):
            print(
                "Conectado ao servidor Urban Routes."
            )
        else:
            print(
                "Não foi possível conectar ao Urban Routes."
            )

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        assert (
            self.page.get_from_location()
            == data.ADDRESS_FROM
        )

        assert (
            self.page.get_to_location()
            == data.ADDRESS_TO
        )

    def test_select_plan(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        self.page.click_taxi_option()
        self.page.select_comfort_plan()

        assert self.page.is_comfort_selected()

    def test_fill_phone_number(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        self.page.click_taxi_option()
        self.page.select_comfort_plan()

        self.page.enter_phone_number(
            data.PHONE_NUMBER
        )

        assert (
            self.page.get_phone_number()
            == data.PHONE_NUMBER
        )

    def test_fill_card(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        self.page.click_taxi_option()
        self.page.select_comfort_plan()

        self.page.click_payment_method()
        self.page.click_add_card()

        self.page.add_credit_card(
            data.CARD_NUMBER,
            data.CARD_CODE
        )

        assert (
            self.page.get_current_payment_method()
            == "Cartão"
        )

    def test_comment_for_driver(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        self.page.click_taxi_option()
        self.page.select_comfort_plan()

        self.page.enter_comment(
            data.MESSAGE_FOR_DRIVER
        )

        assert (
            self.page.get_driver_comment()
            == data.MESSAGE_FOR_DRIVER
        )

    def test_order_blanket_and_handkerchiefs(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        self.page.click_taxi_option()
        self.page.select_comfort_plan()

        self.page.order_blanket_and_handkerchiefs()

        assert (
            self.page.is_blanket_and_handkerchiefs_selected()
        )

    def test_order_2_ice_creams(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        self.page.click_taxi_option()
        self.page.select_comfort_plan()

        self.page.order_2_ice_creams()

        assert (
            self.page.get_ice_cream_count()
            == "2"
        )

    def test_car_search_model_appears(self):
        self.page.enter_locations(
            data.ADDRESS_FROM,
            data.ADDRESS_TO
        )

        self.page.click_taxi_option()
        self.page.select_comfort_plan()

        self.page.enter_comment(
            "Por favor, ligue quando chegar."
        )

        self.page.order_taxi()

        assert (
            self.page.is_search_modal_displayed()
        )

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()