# Import niezbędnych bibliotek
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
        # Wejdziemy na stronę wizzaira
        self.driver.maximize_window()
        self.driver.get('https://www.notino.pl')

    # Instrukcje po każdym teście
    def tearDown(self):
        print("Sprzątanie po teście")
        # Wyłączamy przeglądarkę
        self.driver.quit()

    # Metody testowe - zaczynają się od słowa "test"
    def testInvalidEmail(self):
        print("Prawdziwy test")
        # Tutaj będziemy wykonywać KROKI
        # KROK 1 : Kliknij "Zaloguj"

        driver = self.driver
        zaloguj_bn = driver.find_element_by_xpath("//a[@href='/myaccount.asp']")
        # webDriver.findElement(By.xpath("//a[@href='/docs/configuration']")).click();
        zaloguj_bn.click()

        time.sleep(2)





        #login

        # driver.find_element_by_xpath("//input[@type='submit' and @value='Zaloguj']").click()
        imie_input = driver.find_element_by_xpath('//input[@name="logon_login"]')
        imie_input.send_keys("kamilurbanowski1990@gmail.com")
        time.sleep(2)

        #haslo
        imie_input = driver.find_element_by_xpath('//input[@name="logon_password"]')
        imie_input.send_keys("1qazxsw2")
        time.sleep(6)




        driver.find_element_by_xpath("//button[@type='submit' and @data-sitekey='6Ld2nGQUAAAAAGiZoObvOUiRAcecpwiAk1UA2hRq']").click()







        driver.find_element_by_xpath("//div[@data-cypress='mainMenu-Perfumy']").click()
        driver.find_element_by_xpath("//div[@data-filter='1-1-55544-55549']").click()



        # driver.find_element_by_xpath("//div[@class='item js-filter ca-collapsed']").click()
        # time.sleep(4)
        # name_toilet = driver.find_element_by_xpath('//input[@name="brand"]')
        # name_toilet.send_keys("hugo")
        driver.find_element_by_xpath("//div[@class='item ca-collapsed']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//a[@title='Aldehydowe']").click()
        # driver.find_element_by_xpath('//input[@name="brand"]')

        time.sleep(4)


        cena_min = driver.find_element_by_xpath("//label[@for='price-from']")
        cena_min.send_keys("110")
        cena_max = driver.find_element_by_xpath("//label[@for='price-to']")
        cena_max.send_keys("210")

        driver.find_element_by_xpath("//div[@class='item ca-default-expanded ca-expanded']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@class='item ca-collapsed']").click()
        time.sleep(4)

        zakup_bn = driver.find_element_by_xpath("//a[@href='/order-multistep.asp']")
        # webDriver.findElement(By.xpath("//a[@href='/docs/configuration']")).click();
        zakup_bn.click()




        # driver.find_element_by_xpath("//div[@class='SgEJ_LJlBqqH-Y19PzXRu _2ZQC8Vx4eWrjjVpy9iEGih']").click()
        #
        # driver.find_element_by_xpath("//div[@class='_3ifkYj6o74bCTjrEyfb6gC _3Mn_sogdR8xq2iMSviZ5kK']").click()
        # driver.find_element_by_xpath("//div[@class='_3ErFAD8CSuOXG1mO3HG9Bh dYWEq-La5-A-0a0iqqDy0']").click()
        # driver.find_element_by_xpath("//a[@class='_2wKvURHJBZWGavg_Gquwn3 NQ5LQEhv6OuStrDBpY4j8']").click()
        # aaa = driver.find_elements_by_xpath("//input[@class'_2qwXK-vv7lFlvT83sBDFtt _1S64F93IP84WC9I6KtYxco' and placeholder='nazwa produktu, marka']")
        # aaa.sendkeys("hugo")
        # driver.find_elements_by_id('productsList')
        # driver.find_elements_by_xpath("//li[@data-product='REMPABU_AEDP10']")



        # driver.find_element_by_xpath("//li[@href='https://www.notino.pl/reminiscence/patchouli-blanc-woda-perfumowana-unisex/']")

        # driver.find_element_by_xpath("//a[@href='https://www.notino.pl/reminiscence/patchouli-blanc-woda-perfumowana-unisex/']").click()
        #
        # item_perfum = driver.find_element_by_class_name('spc push-to-dl')
        # webdriver.ActionChains(driver).move_to_element(item_perfum).click(item_perfum).perform()

        # driver.find_element_by_xpath("//div[@class='product-list product-list-facelift recommendations']").click()
        # driver.find_element_by_link_text('Patchouli Blanc').click()
        # driver.find_elements_by_xpath("//a[@class='spc push-to-dl']")

        # driver.find_element_by_xpath("//li[@title='Reminiscence Patchouli Blanc  Woda perfumowana unisex  100 ml']").click()
        # driver.find_element_by_class_name('brand').click()
        # driver.find_element_by_xpath("//a[@data-url-redirect="/reminiscence/patchouli-blanc-woda-perfumowana-unisex/"]").click()


        time.sleep(10)





        # driver.find_element_by_xpath("//div[@class='item js-filter ca-collapsed']").click()
        # time.sleep(10)
        # name_toilet = driver.find_element_by_xpath('//input[@name="brand"]')
        # name_toilet.send_keys("hugo")
        # time.sleep(10)
        # driver.find_element_by_xpath("//a[@title='Aldehydowe']").click()
        # time.sleep(5)
        #
        #
        #
        # #klikanie rejestracji
        # rejestracja_bn = driver.find_element_by_xpath('//a[@href="https://juvepoland.com/register/"]')
        # rejestracja_bn.click()