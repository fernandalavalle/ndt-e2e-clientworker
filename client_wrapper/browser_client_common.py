# Copyright 2016 Measurement Lab
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium import webdriver
from selenium.common import exceptions

import names
import results

ERROR_FAILED_TO_LOAD_URL_FORMAT = 'Failed to load URL: %s'


def create_browser(browser):
    """Creates a Selenium-controlled web browser.

    Args:
        browser: Can be one of 'firefox', 'chrome', 'edge', or 'safari'

    Returns:
        An instance of a Selenium webdriver browser class corresponding to
        the specified browser.
    """
    if browser == names.FIREFOX:
        return webdriver.Firefox()
    elif browser == names.CHROME:
        return webdriver.Chrome()
    elif browser == names.EDGE:
        return webdriver.Edge()
    elif browser == names.SAFARI:
        return webdriver.Safari()
    raise ValueError('Invalid browser specified: %s' % browser)


def load_url(driver, url, errors):
    """Loads the URL in a Selenium driver for an NDT test.

    Args:
        driver: An instance of a Selenium webdriver.
        url: The URL to load.
        errors: A list of errors that will be appended to if the URL cannot be
            loaded.

    Returns:
        True if loading the URL was successful.
    """
    try:
        driver.get(url)
    except exceptions.WebDriverException:
        errors.append(results.TestError(ERROR_FAILED_TO_LOAD_URL_FORMAT % url))
        return False
    return True