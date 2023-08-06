
## Installation

Install celestis using pip

```bash
  pip install celestis
```
    
## Documentation

### How to run celestis server?

First, you must create the files necessary for your project. You can do this by running the following command:

```bash
celestis create-files
```

The above command will prompt you to enter your project name. Once you provide this information, the necessary files are created in the current directory of the terminal

Say your project name is example. Then, run the following commands on your terminal:

```bash
cd example
python server.py
```

Now, you can navigate to http://localhost:8080 to view your website.

### Creating custom routes

Say you want your users to visit your website's about page when they hit the route /about-us.

This can be coded by using the urls.py file. In it, write the following code:

```python
# First value of tuple refers to the route and the second value names the function that returns the HTML for the about page
urls = [("/", "home"), ("/about-us", "about")]
```

The most important part is to not make the array multiline as that would give an error.

The about function must be created in views.py:

```python

def home():
  return "<h1>Home page</h1>"

def about():
  return "<h1>About us</h1>"

```

### Rendering an HTML template
In the previous example, we returned a string that contained HTML code. But if you want to link an HTML file to the url, you can use the render_template function:

```python
from celestis.view import render as rd

def home():
  # Relative path can be the following: static/home.html
  return rd.render_template("relative/path/to/home.html")

def about():
  # Relative path can be the following: static/about.html
  return rd.render_template("relative/path/to/about.html")
```
## Authors

- [@aryaanhegde](https://www.github.com/VOYAGERX013)

