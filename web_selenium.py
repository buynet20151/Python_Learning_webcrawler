from selenium.webdriver import Chrome
import time
from pytube import Playlist
import os



driver = Chrome("./chromedriver")



# 打開網址
driver.get("https://www.youtube.com/view_all_playlists?nv=1")
# find -> find_element
# find_all => find_elements
driver.find_element_by_id("identifierId").send_keys("chiheyu111415@gmail.com")
driver.find_element_by_id("identifierNext").click()
time.sleep(1)
driver.find_element_by_class_name("whsOnd").send_keys("Niffery2015")
driver.find_element_by_id("passwordNext").click()
time.sleep(5)
# 拿很多個
ps = driver.find_element_by_class_name("vm-video-title-text")
for p in ps:
    title = p.text
    url = p.get_attibute("href")
    print(title, url)

    pl = Playlist(url, suppress_exception=True)
    dirname = "youtube/" + title + "/"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    pl.download_all(dirname)
time.sleep(3)
driver.close()
