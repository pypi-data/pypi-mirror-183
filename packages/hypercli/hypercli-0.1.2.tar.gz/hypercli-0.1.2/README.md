```txt
 _                               _ _
| |                             | (_)
| |__  _   _ _ __   ___ _ __ ___| |_
| '_ \| | | | '_ \ / _ \ '__/ __| | |
| | | | |_| | |_) |  __/ | | (__| | |
|_| |_|\__, | .__/ \___|_|  \___|_|_|
        __/ | |
       |___/|_|
```


# Foobar

`hypercli` is a Python library for creating a good looking command line interface. Primarily it can generate menu with very simple steps. We can also create some banners as well.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `hypercli`.

```bash
pip install hypercli
```

## Usage

```python
from hypercli import Menu, Banner
import webbrowser

b = Banner("Hello", "Just a demo")
b.show_banner(show_descr=False)


def author_name():
    print("HYP3R00T")


def open_website():
    webbrowser.open("https://hyperoot.live")


mm = Menu()
mm.create_menu("Main Menu")
mm.add_options("Main Menu", "Checkout the Sub Menu", "Sub Menu")
mm.add_options("Main Menu", "Print Author Name", author_name)

mm.create_menu("Sub Menu")
mm.add_options("Sub Menu", "Go Back to Main Menu", "Main Menu")
mm.add_options("Sub Menu", "Checkout the Website (hyperoot.live)", open_website)

response = mm.show_menu()
response()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
