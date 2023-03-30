from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("playwright")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").press("Enter")
    page.get_by_role("link", name="Playwright: Fast and reliable end-to-end testing for modern ... Playwright https://playwright.dev").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
