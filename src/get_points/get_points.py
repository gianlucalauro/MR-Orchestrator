import os
import pathlib
import sys
import time
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import get_all_profiles, write_points

chrome_user_data_dir = next(
    open(pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), "chrome-user-data-dir.txt"), "r"))

# raspberry pi: assumes driver already installed via `sudo apt-get install chromium-chromedriver`
driver_path = r"/usr/lib/chromium-browser/chromedriver" if platform.machine() in ["armv7l", "aarch64"] \
    else ChromeDriverManager().install()

for profile in get_all_profiles():
    options = Options()
    options.add_argument(r"--user-data-dir={}".format(chrome_user_data_dir))
    options.add_argument(r"--profile-directory={}".format(profile))
    driver = webdriver.Chrome(service=Service(driver_path), options=options)

    driver.get("https://rewards.bing.com/")

    time.sleep(5)

    try:
        points = driver.find_element(By.CSS_SELECTOR, "div#balanceToolTipDiv span")
        write_points(profile, points.text)
    except:
        write_points(profile, "error")

    driver.quit()
