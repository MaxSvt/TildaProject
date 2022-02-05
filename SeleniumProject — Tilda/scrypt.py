from selenium import webdriver
from selenium.webdriver.support.select import Select

from auth_data import *
import time
import pickle

driver = webdriver.Safari(executable_path="/usr/bin/safaridriver")
url = "https://tilda.cc/login/"
company_list = ['maxon', 'максим', 'ozon']



def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
        window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)


def automation():
    i = 1
    try:
        # Авторизация по куки
        driver.get("https://tilda.cc/login/")
        time.sleep(3)

        for cookie in pickle.load(open(f"{site_log}_cookies", "rb")):
            driver.add_cookie(cookie)

        time.sleep(5)
        driver.refresh()
        time.sleep(10)

        # Авторизация по логину и паролю
        # driver.get(url=url)
        # time.sleep(3)
        #
        # log_input = driver.find_element_by_id('email')
        # log_input.clear()
        # log_input.send_keys(site_log)
        # time.sleep(3)
        #
        # pass_input = driver.find_element_by_id('password')
        # pass_input.clear()
        # pass_input.send_keys(site_pass)
        # time.sleep(3)
        #
        # log_button = driver.find_element_by_id('send').click()
        # time.sleep(4)
        #
        # pickle.dump(driver.get_cookies(), open(f"{site_log}_cookies", "wb"))

        # Навигация по сайту
        close_button = driver.find_element_by_xpath('//*[@id="myModalContent"]/div[1]/button').click()
        time.sleep(2)
        main_project = driver.find_element_by_xpath('//*[@id="project5141784"]/div/a/div[1]').click()
        time.sleep(3)
        settings_btn = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]').click()
        time.sleep(3)
        personal_cabinet = driver.find_element_by_xpath('//*[@id="formss"]/div[3]/div[1]/ul/li[13]/a').click()
        time.sleep(3)
        user_control = driver.find_element_by_xpath('//*[@id="ss_menu_members"]/div[2]/div/a').click()
        driver.close()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(4)
        driver.refresh()
        print(driver.window_handles)
        time.sleep(5)
        open_for_group = driver.find_element_by_xpath('//*[@id="left_column"]/div[1]/div[2]/a[1]/span[1]').click()
        time.sleep(3)
        count = driver.find_elements_by_xpath('//*[@id="member_to_group"]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/span[1]')

        print(len(count))
        time.sleep(4)

        while i <= len(count):
            # Открыть форму
            all_application = driver.find_element_by_xpath('//*[@id="member_to_group"]/div/div[2]/div[1]/div[2]/div[2]/div[' + str(i) + ']/div[1]/span[1]')
            company_title = str(all_application.text).lower()
            if company_title in company_list:
                copy_email = driver.find_element_by_xpath(
                    '//*[@id="member_to_group"]/div/div[2]/div[1]/div[2]/div[2]/div[' + str(i) + ']/div[2]/span')
                email = copy_email.text
                print(email)
                # all_application.click()
                time.sleep(2)
                add_btn = driver.find_element_by_xpath('//*[@id="member_to_group"]/div/div[2]/div[1]/div[2]/div[2]/div[' + str(i) + ']/div[6]/div/label/span[1]').click()
                time.sleep(2)
                # driver.refresh()

            else:
                print('Пользователь не найден')

            i = i + 1

    except Exception as ex:
        print(ex)
