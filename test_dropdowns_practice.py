from dropdownpractice.flight import FlightHandler
import time
from dropdownpractice.switcher import Switcher
from dropdownpractice.roundtrip import RoundTripHandler


class TestDropdownsRahulShetty():
    def test_flight(self,cross_browser):
        driver = cross_browser[0]
        logger = self.logger
        driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
        flight = FlightHandler(driver,logger)
        flight.set_from("India","Ahmedabad")
        flight.set_to("India","Kolkata")
        flight.set_currency("USD")
        flight.set_currency("INR")
        flight.set_check_list("Family and Friends")
        # flight.select_date("4","5")
        flight.configure_pax()
        flight.get_buttons("Adult")
        flight.add_current_type()
        flight.add_current_type()
        flight.add_current_type()
        flight.add_current_type()
        flight.get_buttons("Infant")
        flight.add_current_type()
        flight.commit_pax()
        # flight.subtract(1)
        # flight.add(1)
        # flight.add(1)
        flight.book()
        flight.handle_alert()

        time.sleep(5)

        pass
    def test_round_trip(self,cross_browser):

        driver = cross_browser[0]
        logger = self.logger
        driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")
        driver = Switcher(driver).switch_to_round()
        time.sleep(5)
        roundtrip = RoundTripHandler(driver,logger)
        roundtrip.select_date("4", "10")
        roundtrip.configure_pax()
        roundtrip.get_buttons("Adult")
        roundtrip.add_current_type()
        roundtrip.add_current_type()
        roundtrip.add_current_type()

        roundtrip.commit_pax()
        roundtrip.set_currency("AED")
        roundtrip.set_from("International", "Bangkok")
        roundtrip.set_to("India", "Goa")
        roundtrip.dismiss_depart_date()


        roundtrip.book()
    pass