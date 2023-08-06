import re
from time import time, sleep


def _format_url_for_selenium(url):
    ishttps = re.search(r"^\s*https", url.lower(), flags=re.IGNORECASE) is not None
    withouthttps = (re.sub(r"^\s*https?://", "", url, flags=re.IGNORECASE)).strip()
    if not ishttps:
        wholelink = "http://" + withouthttps
    else:
        wholelink = "https://" + withouthttps
    return wholelink


def get_site_with_timeout(driver, url, timeout=5, ready_state=True):
    url = _format_url_for_selenium(url)
    siteloaded = False
    oldvalue = driver.__dict__["caps"]["timeouts"]["script"]
    try:

        driver.set_script_timeout(timeout)
        finaltime = time() + timeout + 0.5
        while time() < finaltime:
            try:
                driver.execute_script(f"window.location.href='{url}'")
                if not ready_state:
                    siteloaded = True

                break
            except Exception as F:
                continue

        if ready_state:
            while time() < finaltime and siteloaded is False:
                siteloaded = (
                    driver.execute_script("return document.readyState") == "complete"
                )
                sleep(0.01)
    finally:
        driver.set_script_timeout(oldvalue)
    return siteloaded
