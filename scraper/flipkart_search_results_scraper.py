from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selectorlib import Extractor
import requests
import json
import time

    
def search_amazon(item):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    try:
        login_pop = driver.find_element_by_class_name('_2KpZ6l _2doB4z')
        ac = ActionChains(driver)
        ac.move_to_element(login_pop).click().perform()
        print(type(login_pop))
        driver.implicitlywait(5)
        # Here .click function use to tap on desire elements of webpage
        login_pop.click()
        print('pop-up closed')
    except:
        pass
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #driver.maximize_window()
    driver.get('https://www.flipkart.com')
    search_box = driver.find_element_by_class_name('_3704LK').send_keys(item)
    element = driver.find_element_by_class_name('L0Z3Pu')
    print(type(element))
    #print(element.get_property('attributes')[0])
    p= element.location
    print(p)
    actions = ActionChains(driver)
    actions.move_to_element(element).move_by_offset(p.get("x"),p.get("y")).click().perform()
    #driver.implicitly_wait(5)
##    search_button = driver.find_element_by_class_name('L0Z3Pu')
##    print(type(search_button))
##    driver.implicitly_wait(5)
##    search_button.click()
##    search=driver.find_element_by_path("//path[@class='_34RNph']")
##    print(type(search))
##    search.click()
##    driver.implicitly_wait(5)

##    try:
##        num_page = driver.find_element_by_xpath('//*[@class="a-pagination"]/li[6]')
##    except NoSuchElementException:
##        num_page = driver.find_element_by_class_name('a-last').click()
##
##    driver.implicitly_wait(3)

    url_list = []
    #print(num_page.text)
    
    for i in range(1):
        page_ = i + 1
        url_list.append(driver.current_url)
        driver.implicitly_wait(4)
        #click_next = driver.find_element_by_class_name('a-last').click()
        print("Page " + str(page_) + " grabbed")
    print(url_list)
    #driver.quit()


    with open('search_results_urls_flipkart.txt', 'w') as filehandle:
        for result_page in url_list:
            filehandle.write('%s\n' % result_page)

    print("---DONE---")

def scrape(url):

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.flipkart.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Flipkart data please contact" in r.text:
            print("Page %s was blocked by Flipkart. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Flipkart as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create
    return e.extract(r.text)

search_string="redmi note 9 pro max"
#search_amazon(search_string) # <------ search query goes here.

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('search_results_flipkart.yml')


# product_data = []
with open("search_results_urls_flipkart.txt",'r') as urllist, open('search_results_output_flipkart.json','w') as outfile:
    for url in urllist.read().splitlines():
        data = scrape(url)
        print(data)
        if data:
            try:
                for product in data['products']:
                    if product['title']!=None:
                    #if (product['title'].lower()).find(search_string.lower())!=-1:
                        product['search_url'] = url
                    
                        print("Saving Product: %s"%product['title'].encode('utf8'))
                        json.dump(product,outfile)
                        outfile.write("\n")
                        time.sleep(5)
            except TypeError:
                data = scrape(url)
                if data:
                    for product in data['products']:
                        if (product['title'].lower()).find(search_string.lower())!=-1:
                            product['search_url'] = url
                    
                            #print("Saving Product: %s"%product['title'].encode('utf8'))
                            json.dump(product,outfile)
                            outfile.write("\n")
                            time.sleep(5)
                
#import linking_pytodb
