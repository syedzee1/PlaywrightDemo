from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto("https:www.google.com/")
    page.locator("//input[@title='Search']").fill("playwright")
    page.screenshot(path = "demo.png")
    page.close()
