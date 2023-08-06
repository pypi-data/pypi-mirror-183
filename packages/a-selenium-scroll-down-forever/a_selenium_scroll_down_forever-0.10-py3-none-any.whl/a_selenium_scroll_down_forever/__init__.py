from random import randrange, uniform
from time import time, sleep


def random_sleep(pause=(0.5, 0.1)):
    sleep(uniform(pause[0], pause[1]))


def scroll_down_forever(
    driver,
    pause_between_scrolls=(0.5, 0.1),
    max_scrolls=10,
    timeout=3,
    script_timeout=1,
    switch_to_default_content=True,
):
    loopind = 0
    if switch_to_default_content:
        driver.switch_to.default_content()
    timeoutfinal = time() + timeout
    was_there_an_error = False
    oldvalue = driver.__dict__["caps"]["timeouts"]["script"]
    driver.set_script_timeout(script_timeout)
    try:
        while loopind <= max_scrolls:
            if time() > timeoutfinal:
                break
            try:
                if switch_to_default_content:
                    driver.switch_to.default_content()
                lastheight = driver.execute_script(
                    "return document.documentElement.scrollHeight;"
                )
                if not was_there_an_error:
                    if loopind % 2 == 0:
                        lastheight = lastheight - (lastheight // randrange(3, 10))
                        was_there_an_error = False
                driver.execute_script(
                    "window.scrollTo(0, document.documentElement.scrollHeight);"
                )
                random_sleep(pause_between_scrolls)
                newheight = driver.execute_script(
                    "return document.documentElement.scrollHeight;"
                )
                if newheight == lastheight:
                    break
                if max_scrolls != 0:
                    loopind += 1
            except Exception as Fehler:
                was_there_an_error = True
                continue
    finally:
        driver.set_script_timeout(oldvalue)
