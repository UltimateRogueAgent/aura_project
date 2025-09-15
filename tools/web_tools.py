import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from crewai_tools import DuckDuckGoSearchRun

from .base_tool import BaseTool, ToolResult
from typing import Any, Dict

class WebTools(BaseTool):
    """
    A tool for web scraping with Playwright and BeautifulSoup.
    It's designed to be used by the web_scraper_tool function.
    """

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.char_limit = self.config.get("char_limit", 8000)
        self.cache: Dict[str, ToolResult] = {}

    async def ascrape(self, url: str) -> ToolResult:
        if url in self.cache:
            return self.cache[url]
        """
        Asynchronously scrapes a URL using Playwright and cleans the content with BeautifulSoup.
        The content is truncated to a character limit.
        """
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                page = await browser.new_page()
                await page.goto(url, timeout=30000)
                content = await page.content()
                await browser.close()

                soup = BeautifulSoup(content, 'html.parser')

                # Remove script, style, and other non-visible elements
                for element in soup(["script", "style", "header", "footer", "nav", "aside"]):
                    element.decompose()

                text = soup.get_text(separator='\n', strip=True)

                result = ToolResult(success=True, result=text[:self.char_limit])
                self.cache[url] = result
                return result

        except PlaywrightTimeoutError:
            return ToolResult(success=False, result=None, error_message=f"Timeout error while trying to scrape {url}.")
        except Exception as e:
            return ToolResult(success=False, result=None, error_message=f"An error occurred while scraping {url}: {e}")

    def execute(self, url: str) -> ToolResult:
        """
        Synchronous wrapper for the async scrape method.
        """
        if not self.validate_input(url=url):
            return ToolResult(success=False, result=None, error_message="Invalid URL provided.")
        return asyncio.run(self.ascrape(url))

    def validate_input(self, **kwargs) -> bool:
        url = kwargs.get("url")
        return isinstance(url, str) and (url.startswith('http://') or url.startswith('https://'))

    def get_description(self) -> str:
        return "Scrapes a website and returns the cleaned text content, limited to 8000 characters."

    def get_schema(self) -> Dict[str, Any]:
        return {
            "name": "web_scraper",
            "description": self.get_description(),
            "args": {"url": "str"},
            "returns": "str"
        }

# Tool functions to be used by agents
# These are instantiated here to be easily imported and used in the agent setup.
web_scraper_tool = WebTools(config={"char_limit": 8000})
search_tool = DuckDuckGoSearchRun()
