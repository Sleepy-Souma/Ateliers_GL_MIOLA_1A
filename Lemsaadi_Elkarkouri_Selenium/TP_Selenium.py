# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#Le chemin vers le chromedriver téléchargé
PATH="/Users/mounalemsaadi/desktop/ensias-miola/cours/Scrum/Selenium/chromedriver"
driver=webdriver.Chrome(PATH)

#Le lien vers le site cookieclicker
driver.get("https://orteil.dashnet.org/cookieclicker/")


#gestion des pubs
all_iframes = driver.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    print("Ad Found\n")
    driver.execute_script("""
        var elems = document.getElementsByTagName("iframe");
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)
    print('Total Ads: ' + str(len(all_iframes)))
else:
    print('No frames found')



driver.implicitly_wait(5)

#Le cookie à cliquer dessus
cookie=driver.find_element_by_id("bigCookie")
#Le score
cookie_count=driver.find_element_by_id("cookies")

#L'item à acheter avec le score
items = [driver.find_element_by_id("productPrice"+str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)



for i in range(5000):
    actions.perform() #Cliquer sur le cookie
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value=int (item.text)
        if value<=count : # Si le prix de l'item est inférieur au score, acheter l'item
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
