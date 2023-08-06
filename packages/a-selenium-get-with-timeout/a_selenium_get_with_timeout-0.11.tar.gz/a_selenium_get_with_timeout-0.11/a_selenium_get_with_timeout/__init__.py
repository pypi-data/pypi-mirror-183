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


def get_site_with_timeout(driver, url, timeout=5):
    url = _format_url_for_selenium(url)
    oldvalue = driver.__dict__["caps"]["timeouts"]["script"]
    try:

        driver.set_script_timeout(timeout)
        driver.execute_async_script(f"window.location.href='{url}'")
    except Exception as b:
        pass

    finally:
        if timeout > 0:
            sleep(timeout)
        driver.set_script_timeout(oldvalue)
