from playwright.sync_api import sync_playwright
import pandas as pd
import time
import re
base_url = "https://www.nytimes.com/search?query="
query = "artificial%20intelligence"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(java_script_enabled=False)
    page = context.new_page()
    page.goto(base_url + query)
    time.sleep(5) 
    context.close()
    browser.close()
