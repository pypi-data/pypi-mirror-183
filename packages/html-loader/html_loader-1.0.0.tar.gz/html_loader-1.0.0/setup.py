
import setuptools

setuptools.setup(
	name="html_loader",
	version="1.0.0",
	author="WiSpace",
	author_email="wiforumit@gmail.com",
	description="HTML to GUI",
	long_description="""
# html_loader

## LoaderHTML

Arguments: name: str="Document" — Window's name, icon: str | None=None — Window's icon, width: int=700, heigth: int=700

Functions:

- Thread(fun) — start function from thread (decorator)
- load_html(code: str) — load code
- load_from_url(url: str) — load code from url
- load_file(name: str) — load code from file
- load_file_absolute_path(name: str) — load code from file by absolute path
- run() — show window


Example:

```py
from html_loader import LoaderHTML

loader = LoaderHTML("Test", "icon.png")
loader.load_file("index.html")

# this function will start and run until it ends without affecting the window
@load.Thread
def main():
    url = input("url:")
    loader.load_from_url(url)

loader.run()
```
""",
	long_description_content_type="text/markdown",
	url="https://wispace.ru/",
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)