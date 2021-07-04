
import unittest
from selenium import webdriver
import time




class NotinoRegistration(unittest.TestCase):
    # Warunki wstępne testów
    def setUp(self):
        print("Przygotowanie testu")
        # Tutaj właczymy przeglądarkę
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

        self.driver.maximize_window()
        self.driver.get('https://juvepoland.com')

    # Instrukcje po każdym teście
    def tearDown(self):
        print("Sprzątanie po teście")
        # Wyłączamy przeglądarkę
        self.driver.quit()

    # Metody testowe - zaczynają się od słowa "test"
    def testInvalidEmail(self):
        print("Prawdziwy test")

        #Kliknij "Zaloguj"
        driver = self.driver
        zaloguj_bn = driver.find_element_by_xpath("//a[@href='/login']")


        zaloguj_bn.click()

        time.sleep(3)
        #klikanie rejestracji
        rejestracja_bn = driver.find_element_by_xpath('//a[@href="https://juvepoland.com/register/"]')
        rejestracja_bn.click()

        #login
        login1_input = driver.find_element_by_xpath('//input[@data-key="user_login"]')
        login1_input.send_keys("DrekarKamil1990")
        time.sleep(3)

        #nazwa
        nazwa_input = driver.find_element_by_xpath('//input[@data-key="nickname"]')
        nazwa_input.send_keys("FakeName")
        time.sleep(3)


        #wpisanie mail
        mail_input = driver.find_element_by_xpath('//input[@data-validate="unique_email"]')
        mail_input.send_keys("marek_kowalskionet.eu")
        time.sleep(3)

        #wpisanie hasla
        haslo_input = driver.find_element_by_xpath('//input[@data-key="user_password"]')
        haslo_input.send_keys("@@34QWasaD")
        time.sleep(3)

        #potwierdzenie hasla
        haslo_input = driver.find_element_by_xpath('//input[@data-key="confirm_user_password"]')
        haslo_input.send_keys("@@34QWasaD")
        time.sleep(3)


        #zarejestruj
        zarejestracja_bn = driver.find_element_by_xpath('//input[@value="Zarejestruj"]')
        zarejestracja_bn.click()

        time.sleep(3)



#### UWAGA! TUTAJ BĘDZIE TEST !!!

        possible_errors = driver.find_elements_by_xpath('//span[@class="um-field-arrow"]/span')

        visible_errors = []

        for error in possible_errors:
            #
            if error.is_displayed():

                visible_errors.append(error)


        assert len(visible_errors) == 1
        self.assertEqual(len(visible_errors), 1)

        print("Tekst błędu na stronie: ", visible_errors[0].text)
        assert visible_errors[0].text == "To nie jest poprawny e-mail"
        self.assertEqual(visible_errors[0].text, "To nie jest poprawny e-mail")
        time.sleep(15)

# Jeśli uruchamiamy z tego pliku
if __name__=="__main__":
    # Włączamy testy
    unittest.main()
