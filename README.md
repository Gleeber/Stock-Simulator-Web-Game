# Stock Simulator Web App (name subject to change)

Interactive web app where users can simulate stock portfolios using real-world financial data.

## Development guide

*Note: These steps should work on Debian/Ubuntu systems. I'm not sure about
other operating systems.*

### Getting started

Make sure you have `pip` installed. On Debian systems, you can install the
`python3-pip` package.

Use `pip3` to install `virtualenv`, which is a tool for creating and managing
virtual environments:

```
pip3 install virtualenv
```

### Virtual environments

A virtual environment is an isolated Python environment that contains its own
versions of `python`, `pip`, and any third-party Python packages you choose to
install to it.

#### Creating the virtual environment

After cloning this project to your local development machine, open a terminal,
`cd` into the project directory, and run the following command:

```
virtualenv venv -p python3.6
```

This creates a new virtual environment located in a directory called `venv` and
ensures that the virtual environment uses Python 3.6.

Activate the virtual environment with:

```
source venv/bin/activate
```

You should see `(venv)` appear to the left of your shell prompt, indicating
that the virtual environment is active.

Now, if you run `python --version`, you should see some variant of `Python
3.6.x`. And if you run `which python`, you should see a path that ends with
`venv/bin/python`. This means that if you run the `python` command from within
the active virtual environment, it will use the virtual environment's Python
interpreter.

Additionally, if you run `pip --version`, you should see output that includes
`python 3.6`, and if you run `which pip`, you should see a path that ends with
`venv/bin/pip`. If you run the `pip` command from within the virtual
environment, it will use the virtual environment's version of `pip` and will
install, uninstall, and otherwise manage packages within the virtual
environment, rather than modifying your machine's global Python environment.

In order to exit the virtual environment, run `deactivate` from within the
active virtual environment.

TODO: alias