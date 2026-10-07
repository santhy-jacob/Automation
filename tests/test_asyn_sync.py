#Work----->

#from playwright.sync_api import sync_playwright,expect
from playwright.async_api import async_playwright,expect
import asyncio
# #sync--->
# #open a browser
# #with sync_playwright() as p:
#     #chrome browser
#     browser =p.chromium.launch(headless=False)
#     user_context = browser.new_context()
#     page=user_context.new_page()
#     page.goto("https://www.facebook.com/")
#     print(page.title()) #give tittle of the page
#     expect(page).to_have_title("Facebook")
# #test---->Banking
# #login->manger
# #login-->user
#
# #Async--->
# #async def test_async_sync_exp2():
#     #async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         user_context = await browser.new_context()
#         page = await user_context.new_page()
#         await page.goto("https://www.facebook.com/")
#        print(page.title())  # give tittle of the page
#         await expect(page).to_have_title("Facebook")
#
# #asyncio.run(test_async_sync_exp2())
#
# @pytest.mark.asyncio
#  async def test_async_sync_exp3(page):
#      await page.goto("https://www.facebook.com/")
#      print(await page.title())  # give tittle of the page
#      await expect(page).to_have_title("Facebook")

# @pytest.mark.asyncio
# async def test_async_sync_exp4(page):
#     page.goto("https://www.facebook.com/")
#     print(page.tittle())
#     expect(page).to_have_title("Facebook")
#     page.goto("https://www.amazon.in/")
#     expect(page).to_have_url("https://www.amazon.in/")
#     page.go_back()
#     page.go_forward()
#     page.reload()
