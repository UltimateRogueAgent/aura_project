# Playwright Python Documentation

Playwright is a Python library for automating Chromium, Firefox, and WebKit browsers with a single API, offering evergreen, capable, reliable, and fast automation.

## Installation

### Basic Installation

```bash
pip install playwright
```

### Install Browser Binaries

```bash
playwright install
```

### Install Specific Browsers

```bash
playwright install chromium
playwright install firefox
playwright install webkit
```

## Quick Start

### Synchronous API

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto('http://playwright.dev')
        page.screenshot(path=f'example-{browser_type.name}.png')
        browser.close()
```

### Asynchronous API

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()
            page = await browser.new_page()
            await page.goto('http://playwright.dev')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.run(main())
```

## Core Concepts

### Browser Management

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)  # Set headless=True for headless mode

    # Create browser context (isolated session)
    context = browser.new_context()

    # Create new page
    page = context.new_page()

    # Navigate to URL
    page.goto("https://example.com")

    # Close resources
    context.close()
    browser.close()
```

### Page Interactions

```python
# Click elements
page.click("button")
page.click("#submit-btn")
page.click("text=Submit")

# Fill forms
page.fill("#username", "john_doe")
page.fill("input[name='password']", "secret123")

# Select options
page.select_option("select#country", "US")

# Upload files
page.set_input_files("input[type='file']", "path/to/file.pdf")

# Wait for elements
page.wait_for_selector("#loading", state="hidden")
page.wait_for_selector(".content", state="visible")

# Get text content
title = page.text_content("h1")
all_links = page.text_content("a")
```

### Element Selectors

```python
# CSS selectors
page.click("#button-id")
page.click(".button-class")
page.click("button[type='submit']")

# Text selectors
page.click("text=Click me")
page.click("text=/Submit/i")  # Case insensitive regex

# XPath selectors
page.click("xpath=//button[@id='submit']")

# Combined selectors
page.click("div >> text=Submit")  # Text inside div
page.click("form >> #submit")     # Element with id inside form
```

### Waiting and Assertions

```python
# Wait for navigation
page.goto("https://example.com")
page.wait_for_load_state("networkidle")

# Wait for elements
element = page.wait_for_selector("#dynamic-content")
page.wait_for_selector("text=Loading", state="hidden")

# Wait for events
with page.expect_navigation():
    page.click("a[href='/next-page']")

# Wait for downloads
with page.expect_download() as download_info:
    page.click("#download-button")
download = download_info.value
download.save_as("downloaded-file.pdf")
```

### Screenshots and PDFs

```python
# Full page screenshot
page.screenshot(path="screenshot.png")

# Element screenshot
element = page.locator("#chart")
element.screenshot(path="chart.png")

# PDF generation (Chromium only)
page.pdf(path="page.pdf", format="A4")
```

### Mobile and Device Emulation

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Use device presets
    iphone = p.devices["iPhone 12"]
    browser = p.webkit.launch()
    context = browser.new_context(**iphone)
    page = context.new_page()

    # Custom viewport
    context = browser.new_context(
        viewport={"width": 375, "height": 667},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    )
```

### Network Interception

```python
# Block images and stylesheets
def handle_route(route):
    if route.request.resource_type in ["image", "stylesheet"]:
        route.abort()
    else:
        route.continue_()

page.route("**/*", handle_route)

# Mock API responses
def handle_api(route):
    if "api/users" in route.request.url:
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"users": [{"name": "John", "id": 1}]}'
        )
    else:
        route.continue_()

page.route("**/api/**", handle_api)
```

### JavaScript Execution

```python
# Execute JavaScript
result = page.evaluate("() => document.title")
page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")

# Pass arguments to JavaScript
result = page.evaluate("(name) => `Hello ${name}!`", "World")

# Evaluate on element
element = page.locator("#my-element")
text = element.evaluate("el => el.textContent")
```

### File Downloads and Uploads

```python
# Handle downloads
with page.expect_download() as download_info:
    page.click("#download-link")
download = download_info.value
download.save_as("./downloads/" + download.suggested_filename)

# Upload files
page.set_input_files("#file-input", ["file1.txt", "file2.pdf"])

# Upload from memory
page.set_input_files("#file-input", files=[
    {"name": "test.txt", "mimeType": "text/plain", "buffer": b"Hello World"}
])
```

### Browser Contexts and Sessions

```python
# Create isolated contexts
context1 = browser.new_context()
context2 = browser.new_context()

# Different sessions, cookies, localStorage
page1 = context1.new_page()
page2 = context2.new_page()

# Set cookies
context.add_cookies([{
    "name": "session_id",
    "value": "abc123",
    "domain": "example.com",
    "path": "/"
}])

# Set localStorage
page.add_init_script("""
    localStorage.setItem('user_preference', 'dark_mode');
""")
```

### Debugging and Development

```python
# Debug mode - opens browser in headed mode with dev tools
browser = p.chromium.launch(headless=False, devtools=True)

# Slow down actions for debugging
browser = p.chromium.launch(slow_mo=1000)  # 1 second delay

# Pause execution for debugging
page.pause()

# Enable tracing
context.tracing.start(screenshots=True, snapshots=True)
# ... perform actions ...
context.tracing.stop(path="trace.zip")
```

### Advanced Locators

```python
# Locator API (recommended)
locator = page.locator("#submit-button")
locator.click()

# Chain locators
form_locator = page.locator("form")
submit_button = form_locator.locator("button[type='submit']")

# Filter locators
rows = page.locator("tr")
active_rows = rows.filter(has_text="Active")

# Get multiple elements
all_links = page.locator("a").all()
for link in all_links:
    print(link.text_content())
```

### Testing Integration

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_homepage(page):
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    assert page.is_visible("h1")
```

### Configuration and Options

```python
# Browser launch options
browser = p.chromium.launch(
    headless=True,
    slow_mo=100,
    args=["--disable-web-security"],
    executable_path="/path/to/chrome"
)

# Context options
context = browser.new_context(
    viewport={"width": 1280, "height": 720},
    user_agent="Custom User Agent",
    locale="en-US",
    timezone_id="America/New_York",
    permissions=["geolocation"],
    geolocation={"latitude": 40.7128, "longitude": -74.0060}
)

# Page options
page.goto("https://example.com", wait_until="networkidle")
page.set_default_timeout(30000)  # 30 seconds
page.set_default_navigation_timeout(60000)  # 60 seconds
```

## Development Setup

### Local Development

```bash
# Clone repository
git clone https://github.com/microsoft/playwright-python

# Setup virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
python -m pip install --upgrade pip
pip install -r local-requirements.txt
pre-commit install
pip install -e .

# Build and install drivers
python -m build --wheel

# Run tests
pytest --browser chromium

# Format code
pre-commit run --all-files
```

### Testing

```bash
# Run all tests
pytest --browser chromium

# Run specific test
pytest tests/test_page.py::test_click --browser chromium

# Run with coverage
pytest --browser chromium --cov-report html --cov=playwright
```

## Best Practices

1. **Use Locators**: Prefer the locator API over direct selectors
2. **Wait Strategies**: Use appropriate wait strategies instead of sleep()
3. **Isolation**: Use browser contexts for test isolation
4. **Resource Cleanup**: Always close browsers and contexts
5. **Error Handling**: Implement proper error handling for network issues
6. **Screenshots**: Take screenshots on failures for debugging
7. **Headless Mode**: Use headless mode in CI/CD pipelines

## Common Use Cases

### Web Scraping

```python
def scrape_products():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example-shop.com")

        products = []
        for product in page.locator(".product").all():
            name = product.locator(".name").text_content()
            price = product.locator(".price").text_content()
            products.append({"name": name, "price": price})

        browser.close()
        return products
```

### Form Automation

```python
def fill_form():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com/form")

        page.fill("#first-name", "John")
        page.fill("#last-name", "Doe")
        page.select_option("#country", "US")
        page.check("#terms-checkbox")
        page.click("#submit-button")

        # Wait for success message
        page.wait_for_selector(".success-message")
        browser.close()
```

This documentation covers the essential aspects of Playwright Python for browser automation, testing, and web scraping.
