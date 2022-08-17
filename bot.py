from sre_parse import CATEGORIES
import requests
import json

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
mobile_emulation = {"deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},"userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " "Version/13.0.3 Mobile/15E148 Safari/604.1"}
prefs = {'disk-cache-size': 4096}
options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("useAutomationExtension", False)
driver = webdriver.Chrome(options=options, executable_path=DriverOptions.CHROME_DRIVER_PATH)
wait = WebDriverWait(driver, 10)
def get_product(product_id, product_colour_id, size):
    url = 'https://www.supremenewyork.com/mobile/#products/' + str(product_id) + '/' + str(product_colour_id)
    driver.get(url)
    wait.until(EC.presence_of_element_located((By.ID, 'size-options')))
    options = Select(driver.find_element_by_id('size-options'))
    options.select_by_visible_text(size)
    driver.find_element_by_xpath("//*[@id='cart-update']/span").click()


driver = webdriver.Chrome(executable_path='')


def find_item(name):
    url = 'https://www.supremenewyork.com/mobile_stock.json'
    html = requests.get(url=url)
    output = json.loads(html.text)

    for item in output['products_and_categories']:
        for product in output['products_and_categories'][item]:
            if product['name'] == name:
                return product['id']


def get_color(product_id, color, product_size):
    url = f'https://www.supremenewyork.com/shop/'+{product_id}+'.json'
    html = requests.get(url=url)
    output = json.loads(html.text)

    for product_color in output:
        if color in product_color['name']:
            for product_size in product_color['sizes']:
                if product_size['name']:
                    return product_color['id']

def get_product(product_id, color_id, size):
    url =  'https://www.supremenewyork.com/mobile/#products/' + str(product_id) + '/' + str(color_id)

    driver.get(url)

    wait.until(EC.presence_of_all_elements_located((By.ID, 'size-options')))

    options = Select(driver.find_element_by_id('size-options'))
    options.select_by_visible_text(size)






def checkout():
    url = 'https://www.supremenewyork.com/mobiel/#checkout.json'
    driver.get(url)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'order_billing_name')))

    driver.execute_script(
    f'document.getElementById("order_billing_name").value="{UserDetails.NAME}";'
    f'document.getElementById("order_email").value="{UserDetails.EMAIL}";'
    f'document.getElementById("order_tel").value="{UserDetails.TELE}";'
    f'document.getElementById("order_billing_address").value="{UserDetails.ADDRESS_1}";'
    f'document.getElementById("order_billing_address").value="{UserDetails.ADDRESS_2}";'
    f'document.getElementById("order_billing_address_3").value="{UserDetails.ADDRESS_3}";'
    f'document.getElementById("order_billing_city").value="{UserDetails.CITY}";'
    f'document.getElementById("order_billing_zip").value="{UserDetails.POSTCODE}";'
    f'document.getElementById("credit_card_number").value="{PaymentDetails.CARD_NUMBER}";'
    f'document.getElementById("credit_card_cvv").value="{PaymentDetails.CVV}";'
  )

    card_type = Select(driver.find_element_by_id('credit_card_type'))
    card_type.select_by_visible_text(PaymentDetails.CARD_TYPE)

    card_month = Select(driver.find_element_by_id('credit_card_month'))
    card_month.select_by_value(str(PaymentDetails.EXP_MONTH))

    card_year = Select(driver.find_element_by_id('credit_card_year'))
    card_year.select_by_value(str(PaymentDetails.EXP_YEAR))

    driver.find_element_by_id('order_terms').click()
    driver.find_element_by_id('submit_button').click()



if __name__ == '__main__':
    product_id = find_item(ProductDetails.KEYWORDS)
    color_id = get_color(product_id, ProductDetails.COLORS, ProductDetails.SIZE)
    get_product(product_id, color_id, ProductDetails.SIZE)
