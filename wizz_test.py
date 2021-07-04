
import unittest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class WizzairRegistration(unittest.TestCase):

    def setUp(self):
        print("Przygotowanie testu")

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl/#/')


    def tearDown(self):
        print("Sprzątanie po teście")

        self.driver.quit()


    def testInvalidEmail(self):
        print("Prawdziwy test")

        driver = self.driver
        zaloguj_btn = driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_btn.click()

        #klikanie rejestracji
        rejestracja_bn = driver.find_element_by_xpath('//button[@data-test="registration"]')
        rejestracja_bn.click()


        #imie
        imie_input = driver.find_element_by_xpath('//input[@data-test="registrationmodal-first-name-input"]')
        imie_input.send_keys("Kamil")
        time.sleep(3)
        #nazwisko
        nazwisko_input = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
        nazwisko_input.send_keys("Urbanowski")
        time.sleep(3)
        #wybranie plci
        plec_input = driver.find_element_by_xpath('//input[@value="male"]')
        plec_input.click()
        time.sleep(3)

        #wybieranie numeru kierunkowego
        nr_kierunkowy = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        nr_kierunkowy.click()
        time.sleep(3)

        nr_kierunkowy1 = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        nr_kierunkowy1.send_keys("Polska",Keys.ENTER)
        time.sleep(3)

        #wpisanie nr telefonu
        telefon_input = driver.find_element_by_xpath('//input[@data-test="text-input-digits-phone-number-input-input-field"]')
        telefon_input.send_keys("123123456")
        time.sleep(3)

        #wpisanie mail
        mail_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        mail_input.send_keys("marek_kowalskionet.eu")
        time.sleep(3)


        #wpisanie hasla
        haslo_input = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        haslo_input.send_keys("@@34QWasaD")
        time.sleep(3)

        #wpisanie narodowosci
        narodowosc_input = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        narodowosc_input.send_keys("Polska",Keys.ENTER)
        time.sleep(3)

        #newsler
        driver.find_element_by_xpath('//div[@data-test="checkbox-newsletter"]')
        two = driver.find_element_by_xpath('//input[@data-test="registration-newsletter-checkbox"]')
        actions = ActionChains(driver)
        actions.move_to_element(two).click(two).perform()
        time.sleep(3)

        #polityka prywatnosci
        driver.find_element_by_xpath('//div[@data-test="checkbox-privacyPolicy"]')
        one = driver.find_element_by_xpath('//input[@data-test="registration-privacy-policy-checkbox"]')
        actions = ActionChains(driver)
        actions.move_to_element(one).click(one).perform()
        time.sleep(3)

        #wizz polityka
        driver.find_element_by_xpath('//div[@data-test="checkbox-wizzAccountPolicy"]')
        zero = driver.find_element_by_xpath('//input[@data-test="registration-wizz-account-policy-checkbox"]')
        actions = ActionChains(driver)
        actions.move_to_element(zero).click(zero).perform()
        time.sleep(3)

        #zarejestruj
        zarejestracja_bn = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
        zarejestracja_bn.click()
        time.sleep(3)

        time.sleep(5)
        #### UWAGA! TUTAJ BĘDZIE TEST !!!

        possible_errors = driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')

        visible_errors = []

        for error in possible_errors:
            #
            if error.is_displayed():

                visible_errors.append(error)


        assert len(visible_errors) == 1
        self.assertEqual(len(visible_errors), 1)

        print("Tekst błędu na stronie: ", visible_errors[0].text)
        assert visible_errors[0].text == "Nieprawidłowy adres e-mail"
        self.assertEqual(visible_errors[0].text, "Nieprawidłowy adres e-mail")
        time.sleep(15)



if __name__=="__main__":

    unittest.main()
