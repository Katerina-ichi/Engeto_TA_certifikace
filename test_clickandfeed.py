import time
from playwright.sync_api import sync_playwright, expect

def test_clickandfeed(page):
    start_time = time.time()
    page.goto("https://clickandfeed.cz/", wait_until="load")
    load_time = time.time() - start_time
        
    print(f"🌐 {browser_type.name}: {load_time:.2f} sekund")
    
def test_clickandfeed_button(page):
    page.goto("https://clickandfeed.cz/", wait_until="load")
    button = page.locator("#feed-button").click()

    confirmation_msg = page.get_by_role("heading", name="Váš klik byl započítán! Děkujeme, přijďte zase zítra!")
    if confirmation_msg:
        print("První klik úspěšný")
    else:
        print("Chyba první klik")

    logo = page.locator(".elementor-widget-container > a").first.click()
    button = page.get_by_role("button", name="Klikni zdarma a naplň misku")

    failure_msg = page.get_by_role("heading", name="Dnes už jste jednou pomohli! Děkujeme, přijďte zase zítra!")
    if failure_msg:
        print("Druhý klik za den")
    else:
        print("Chyba failure_msg")

def test_clickandfeed_menu(page):
    page.goto("https://clickandfeed.cz/", wait_until="load")

    menu = page.get_by_role("link", name="Jak pomáhat")

    try:
        expect(menu).to_be_visible(timeout=10000)
        print("vidím menu")
    except:
        print("nevidím menu")

    menu.hover()

    submenu = menu.locator("nav.elementor-nav-menu--dropdown").locator('text:"Charitativní partneři"')
    
    if submenu:
        print("Submenu se zobrazilo")
    else:
        print("Chyba, submenu není viditelné")

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox]:
        print(f"Spouštím test v prohlížeči: {browser_type.name}")
        browser = browser_type.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        test_clickandfeed(page)
        test_clickandfeed_button(page)
        test_clickandfeed_menu(page)
        browser.close()