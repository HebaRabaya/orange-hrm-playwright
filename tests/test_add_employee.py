from playwright.sync_api import sync_playwright

def test_add_employee():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')

        page.click("text=PIM")
        page.click("text=Add Employee")

        page.fill('input[name="firstName"]', "Test")
        page.fill('input[name="lastName"]', "User")

        page.click('button[type="submit"]')

        browser.close()
