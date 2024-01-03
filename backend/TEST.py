from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://github.com/')
# driver.get("file:C:///Users/BanhMiBietBay/Downloads/chromedriver-win64/chromedriver-win64\chromedriver.exe")
# driver.get("file:///C:/Users/BanhMiBietBay/Desktop/Front_End/4_TheBigCat/index.html")

print(driver.title)

driver.maximize_window()
driver.fullscreen_window()
driver.set_window_size(500, 400)

# # driver.get('https://www.apress.com')
# #
# # button = driver.find_element_by_link_text("Apress Access")
# # webdriver.ActionChains(driver).context_click(button).perform()

