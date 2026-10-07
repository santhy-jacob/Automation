import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_getBytitle(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele=async_page.get_by_text("welcome to our store")
    await expect(ele).to_be_visible()
    print(ele.inner_html())
    # if you have any attribute in web ele
    # css:---->
    # tag.name[an='av']
    # when we have a attribute we need to go with css

@pytest.mark.asyncio
async def test_getBytitle(async_page):
   await async_page.goto("https://demowebshop.tricentis.com/")
   ele = async_page.locator("h2[class='topic-html-content-header']") # locator :notfinding
   await expect(ele).to_be_visible()
   print (await ele.inner_html())


@pytest.mark.asyncio
async def test_getBytitle(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/books")
    ele = async_page.locator(".product-title")#.nth(0)
    # await expect(ele).to_be_visible()
    # print(await ele.inner_html())
#     print all prodcuts in the elements to get 1 by 1
    all_products= await ele.all()
    for i in all_products:
        print(await i.inner_text())

@pytest.mark.asyncio
async def test_getBytitle(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele = async_page.locator(".product-title")


@pytest.mark.asyncio
async def test_getBytitle(async_page):
   await async_page.goto("https://demowebshop.tricentis.com/")
   ele = async_page.locator("input[class='button-2 product-box-add-to-cart-button']") # locator :notfinding
   all_product = await ele.all()
   for i in all_product:
       await i.click()
       break
   await async_page.wait_for_timeout(5000)
# XPath & CSS

# 1. Multiple elements
# - If a locator matches multiple elements, narrow it down when you need to perform an action on a single element.
# - Use nth(), filtering, text, role, or other attributes to identify the required element.
#
# 2. Product-based XPath
# - Locate a product based on its name.
# - From the product name, navigate to the related link/button and click it.
#
# 3. CSS attribute operators
# *=  → contains
# ^=  → starts with
# $=  → ends with
#
# 4. XPath access in Playwright
# async_page.locator("//button")
# async_page.locator("xpath=//button")
#
# 5. jQuery UI Datepicker
# https://jqueryui.com/datepicker/
#
# 6. XPath parent
# //a[@class="ui-state-default ui-state-hover"]/..
#
# /.. → moves to the parent element.

#Xpath acces

# //a[text()='Build your own expensive computer']/ancestor::div[1]//input[@value='Add to cart']
# https://www.moneycontrol.com/
# (//a[text()='Kotak Mahindra'])[2]/parent::td/following-sibling::td[1]
# https://www.w3schools.com/html/html_tables.asp
# //table[@class='ws-table-all']/descendant::tr/td[3]
# //table[@class='ws-table-all']/descendant::tr/td[3]|//th[text()='Country']
# //section[@class='category-section']//div[@role="heading"]
# https://jqueryui.com/datepicker/
# //div[@id='ui-datepicker-div']//th
# https://account.99.com/v3/login.html
# //input[@id='txtUserName' or @id='txtPassword']
