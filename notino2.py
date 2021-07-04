
import unittest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class NotinoRegistration(unittest.TestCase):
    # Warunki wstępne testów
    def setUp(self):
        print("Przygotowanie testu")
        # Tutaj właczymy przeglądarkę
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        # Wejdziemy na stronę notino
        self.driver.maximize_window()
        self.driver.get('https://www.notino.pl')

    #
    def tearDown(self):
        print("Sprzątanie po teście")
        # Wyłączamy przeglądarkę
        self.driver.quit()


    def testInvalidEmail(self):
        print("Prawdziwy test")


        # Kliknij "Zaloguj"

        driver = self.driver
        zaloguj_bn = driver.find_element_by_xpath("//a[@href='/myaccount.asp']")

        zaloguj_bn.click()

        time.sleep(2)





        #login

        imie_input = driver.find_element_by_xpath('//input[@name="logon_login"]')
        imie_input.send_keys("kamilurbanowski1990@gmail.com")
        time.sleep(2)

        #haslo
        haslo_input = driver.find_element_by_xpath('//input[@name="logon_password"]')
        haslo_input.send_keys("1qazxsw2")
        time.sleep(6)




        driver.find_element_by_xpath("//button[@type='submit' and @data-sitekey='6Ld2nGQUAAAAAGiZoObvOUiRAcecpwiAk1UA2hRq']").click()

        #zakup
        zakup_bn = driver.find_element_by_xpath("//a[@href='/order-multistep.asp']")
        zakup_bn.click()
        time.sleep(4)
        #rabat
        rabat_input = driver.find_element_by_xpath('//input[@name="voucher_code"]')
        rabat_input.send_keys("123")
        time.sleep(4)

        driver.find_element_by_xpath("//button[@name='submit_discount']").click()
        time.sleep(4)

        #### UWAGA! TUTAJ BĘDZIE TEST !!!

        possible_errors = driver.find_elements_by_xpath('//span[@class="message error-message"]')

        visible_errors = []

        for error in possible_errors:

            if error.is_displayed():
                visible_errors.append(error)

        assert len(visible_errors) == 1
        self.assertEqual(len(visible_errors), 1)

        print("Tekst błędu na stronie: ", visible_errors[0].text)
        assert visible_errors[0].text == "Nieprawidłowy kod kupon."
        self.assertEqual(visible_errors[0].text, "Nieprawidłowy kod kupon.")
        time.sleep(3)



if __name__=="__main__":

    unittest.main()




