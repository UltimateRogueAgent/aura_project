# Beautiful Soup 4 Documentation

Beautiful Soup is a Python library for pulling data out of HTML and XML files, providing idiomatic ways to navigate, search, and modify the parse tree.

## Installation

### Using pip (Recommended)

```bash
pip install beautifulsoup4
```

### Using easy_install

```bash
easy_install beautifulsoup4
```

### From Source

```bash
# Download source tarball and extract
python setup.py install
```

### Installing Parsers

#### lxml Parser (Fast and Lenient)

```bash
# Ubuntu/Debian
apt-get install python-lxml

# Using pip
pip install lxml

# Using easy_install
easy_install lxml
```

#### html5lib Parser (Pure Python, Browser-like)

```bash
# Ubuntu/Debian
apt-get install python-html5lib

# Using pip
pip install html5lib

# Using easy_install
easy_install html5lib
```

## Quick Start

### Basic Setup

```python
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
```

### Parser Selection

```python
from bs4 import BeautifulSoup

# Python's built-in HTML parser
soup = BeautifulSoup(markup, "html.parser")

# lxml HTML parser (fast, lenient)
soup = BeautifulSoup(markup, "lxml")

# lxml XML parser (fast, XML-only)
soup = BeautifulSoup(markup, "xml")

# html5lib parser (slow, extremely lenient, browser-like)
soup = BeautifulSoup(markup, "html5lib")
```

## Basic Navigation

### Accessing Tags

```python
# Get the title tag
print(soup.title)
# <title>The Dormouse's story</title>

# Get tag name
print(soup.title.name)
# title

# Get tag text
print(soup.title.string)
# The Dormouse's story

# Get parent tag name
print(soup.title.parent.name)
# head

# Get first paragraph
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>

# Get first anchor tag
print(soup.a)
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
```

### Working with Attributes

```python
# Access attributes like a dictionary
tag = soup.b
print(tag['class'])  # Access class attribute
print(tag.attrs)     # Get all attributes as dict

# Modify attributes
tag['class'] = 'verybold'
tag['id'] = 1

# Remove attributes
del tag['class']
del tag['id']

# Safe access with .get()
print(tag.get('class'))  # Returns None if not found
```

## Finding Elements

### find() and find_all()

```python
# Find first occurrence
first_link = soup.find('a')
title_p = soup.find('p', class_='title')

# Find all occurrences
all_links = soup.find_all('a')
all_paragraphs = soup.find_all('p')

# Find with attributes
sister_links = soup.find_all('a', class_='sister')
link2 = soup.find_all(id='link2')

# Find with multiple attributes
soup.find_all('a', {'class': 'sister', 'id': 'link1'})

# Using attrs parameter for complex attribute names
soup.find_all(attrs={'data-foo': 'value'})
```

### Using Regular Expressions

```python
import re

# Find tags whose names start with 'b'
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

# Find tags with href containing 'elsie'
soup.find_all(href=re.compile("elsie"))

# Find tags whose names contain 't'
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
# html
# title
```

### CSS Selectors

```python
# Select by tag
soup.select('title')

# Select by class
soup.select('.sister')

# Select by id
soup.select('#link1')

# Select by attribute
soup.select('a[href]')

# Complex selectors
soup.select('p.story')  # p tags with class 'story'
soup.select('p > a')    # a tags directly inside p tags
soup.select('p a')      # a tags anywhere inside p tags

# Language attribute selector
multilingual_soup.select('p[lang|=en]')  # Matches lang="en", "en-us", etc.
```

### Advanced Finding

```python
# Find by function
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)

# Find by text content
soup.find_all(text="Elsie")
soup.find_all(text=re.compile("Dormouse"))

# Limit results
soup.find_all('a', limit=2)

# Find only direct children (not recursive)
soup.find_all('title', recursive=False)
```

## Modifying the Tree

### Changing Text and Attributes

```python
# Change tag text
tag = soup.find('b')
tag.string = "New text"

# Change attributes
tag['class'] = 'new-class'
tag['id'] = 'new-id'

# Add new attributes
tag['data-custom'] = 'custom-value'
```

### Adding and Removing Elements

```python
# Create new tag
new_tag = soup.new_tag('a', href='http://example.com')
new_tag.string = "Link text"

# Insert new tag
soup.p.insert(1, new_tag)

# Append to end
soup.p.append(new_tag)

# Remove elements
tag = soup.find('a', id='link1')
tag.decompose()  # Completely remove from memory

# Or extract (remove but keep in memory)
extracted_tag = tag.extract()
```

## Output and Formatting

### Pretty Printing

```python
# Pretty print entire document
print(soup.prettify())

# Pretty print specific tag
print(soup.a.prettify())
```

### String Conversion

```python
# Convert to string
html_string = str(soup)
unicode_string = unicode(soup)  # Python 2

# Get text content only
text_only = soup.get_text()
text_with_separator = soup.get_text(separator=' | ')
```

## Advanced Features

### SoupStrainer (Parsing Only Parts)

```python
from bs4 import BeautifulSoup, SoupStrainer

# Parse only anchor tags
only_a_tags = SoupStrainer("a")
soup = BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tags)

# Parse only tags with specific id
only_link2 = SoupStrainer(id="link2")
soup = BeautifulSoup(html_doc, "html.parser", parse_only=only_link2)

# Parse only short text strings
def is_short_string(string):
    return len(string) < 10

only_short_strings = SoupStrainer(text=is_short_string)
soup = BeautifulSoup(html_doc, "html.parser", parse_only=only_short_strings)
```

### XML Parsing

```python
# Parse as XML (requires lxml)
xml_soup = BeautifulSoup(xml_doc, "xml")

# XML preserves self-closing tags
xml_soup = BeautifulSoup("<a><b /></a>", "xml")
print(xml_soup.prettify())
# <?xml version="1.0" encoding="utf-8"?>
# <a>
#  <b/>
# </a>
```

### Encoding Handling

```python
# Beautiful Soup automatically detects encoding
soup = BeautifulSoup(html_bytes)

# Force specific encoding
soup = BeautifulSoup(html_bytes, from_encoding="iso-8859-1")

# Output in specific encoding
soup.encode('utf-8')
```

## Parser Comparison

| Parser      | Speed  | Lenient | External Dependency | Notes                           |
| ----------- | ------ | ------- | ------------------- | ------------------------------- |
| html.parser | Medium | Medium  | No                  | Built-in, decent for most cases |
| lxml        | Fast   | High    | Yes (C)             | Best performance, very lenient  |
| html5lib    | Slow   | Highest | Yes (Python)        | Most browser-like parsing       |
| xml         | Fast   | Low     | Yes (C)             | XML only, strict parsing        |

## Common Patterns

### Web Scraping

```python
import requests
from bs4 import BeautifulSoup

# Fetch and parse web page
response = requests.get('https://example.com')
soup = BeautifulSoup(response.content, 'html.parser')

# Extract data
titles = [h2.text for h2 in soup.find_all('h2')]
links = [a['href'] for a in soup.find_all('a', href=True)]
```

### Form Data Extraction

```python
# Find form elements
form = soup.find('form')
inputs = form.find_all('input')

# Extract form data
form_data = {}
for input_tag in inputs:
    name = input_tag.get('name')
    value = input_tag.get('value', '')
    if name:
        form_data[name] = value
```

### Table Parsing

```python
# Parse HTML table
table = soup.find('table')
rows = table.find_all('tr')

data = []
for row in rows:
    cells = row.find_all(['td', 'th'])
    row_data = [cell.get_text(strip=True) for cell in cells]
    data.append(row_data)
```

## Error Handling

```python
from bs4 import BeautifulSoup
import requests

try:
    response = requests.get('https://example.com')
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # Safe element access
    title = soup.find('title')
    if title:
        print(title.get_text())
    else:
        print("No title found")

except requests.RequestException as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"Parsing failed: {e}")
```

## Best Practices

1. **Choose the Right Parser**: Use `lxml` for speed, `html5lib` for accuracy
2. **Handle Missing Elements**: Always check if elements exist before accessing
3. **Use CSS Selectors**: Often more readable than complex find_all() calls
4. **Memory Management**: Use `decompose()` for large documents to free memory
5. **Encoding**: Let Beautiful Soup auto-detect encoding when possible
6. **Error Handling**: Wrap parsing in try-catch blocks for robust applications

This documentation covers the essential features of Beautiful Soup 4 for HTML and XML parsing, navigation, and manipulation.
