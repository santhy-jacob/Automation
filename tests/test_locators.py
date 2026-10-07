# 1 evn why how when
# 2. requiremtns.txt why what how to use
# 3. HTML
# 4.clcik()/type()
# 5. locators

import playwright.async_api as playwright
import pytest
from utils.config import BASE_URL, USERNAME, PASSWORD
from dotenv import load_dotenv
load_dotenv()
import os

@pytest.mark.asyncio
async def test_evn(async_page):
    await async_page.goto(os.getenv("BASE_URL")) #:-->dotenv load
    print(await async_page.title()) #user name and password
