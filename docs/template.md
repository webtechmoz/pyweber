# Template Class Documentation

## Overview
The `Template` class in PyWeber is responsible for managing and rendering templates for web applications. It supports both inline content and external HTML files stored in the `templates` directory.

## Usage

### Example 1: Using an HTML File as a Template
To use an external HTML file as a template, place the file inside the `templates` folder and reference it in the `Template` class.

```python
import pyweber as pw

def main(app: pw.Router):
    app.add_route(route='/', template=pw.Template(template='index.html'))

if __name__ == '__main__':
    pw.run(target=main)
```

### Example 2: Using a String as a Template
If the template content is provided as a string instead of an HTML file, it is processed directly without requiring an external file.

```python
import pyweber as pw

def main(app: pw.Router):
    app.add_route(route='/', template=pw.Template(template='<h1>Welcome to PyWeber</h1>'))

if __name__ == '__main__':
    pw.run(target=main)
```

## Behavior
- If the `template` argument is a `.html` file, it must be placed inside the `templates` folder.
- If the `template` argument is a string, it is processed as-is without requiring an external file.
- If the specified `.html` file does not exist, a `FileNotFoundError` is raised.

## Notes
- Ensure that the `templates` folder exists and contains the necessary `.html` files.
- This class provides a simple method to handle templates in PyWeber applications.