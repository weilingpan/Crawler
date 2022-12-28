from playwright.sync_api import Playwright, sync_playwright

def run_playwright(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True,executable_path="path/chromium/chrome.exe")
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    timeout = 數值
    page.set_default_timeout(timeout) # 如果網頁 loading 需要很久，調整 timeout 時間，或設置 page.set_default_timeout(0) 
    page.goto("網址")

    with page.expect_download() as download_info:
        page.click("text=網頁上呈現的文字")
    download = download_info.value
    download.save_as('要儲存的路徑/檔名.副檔名')

    page.close()
    context.close()
    browser.close()
    
def run():
    with sync_playwright() as playwright:
        run_playwright(playwright)
