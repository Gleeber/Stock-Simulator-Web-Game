# Stock Trading Simulator

## Project design

### General design

This project was initially designed to be an interactive web app wherein users
can search, buy, and sell any publicly traded stock. With the purpose being
simulation, users would be able to trade with imaginary funds and view their
portfolios performance in real time. Another proposed purpose would be for
historical simulation; users would be able to have their portfolio start at
some arbitrary date in the past, and users could buy, sell, and monitor
performance using historical financial data. Unfortunately, we were not able to
implement this feature of the project due to time constraints and technical
complexity. For financial data, we would utilize the [AlphaVantage
API](https://www.alphavantage.co/). To simplify implementation, this financial
data would simply be queried when necessary rather than stored in a database or
local storage. The project also utilizes Docker for containerization, to allow
for cross-platform hosting and dependency management.

The project's code is divided into primarily two components - the backend and
the frontend of the web page. The backend is a REST API server written in the
Flask framework for Python. This server essentially wraps the AlphaVantage API
to provide endpoints for the frontend to query information regarding the user's
portfolio, stock quotes, etc. This server also serves the relevant
HTML/JavaScript files to client browsers. The backend includes a Portfolio and
Stock class to represent the user's portfolio and all the contained stocks
respectively, which are then serialized into JSON objects and delivered by the
API. The Flask framework also provides a signed session-wide cookie, which is
used as storage for user data such as the portfolio and recent searches. The
frontend of the app is written in HTML and vanilla JavaScript, using the
Bootstrap library for cross-browser compatibility and correct cross-platform
DOM rendering. The website is mostly rendered client-side, as the served HTML
is mostly a skeleton with JavaScript that queries the backend for necessary
info such as user portfolio or financial data using HTTP requests and modifies
the HTML accordingly.

### User stories

User stories are available in GitHub-hosted kanban boards under
[projects](https://github.com/Gleeber/Stock-Simulator-Web-Game/projects).

### Classes

#### APICallLimitError

The type of exception raised when we detect that we've made too many calls to
the Alpha Vantage API and must wait for a timeout.

#### Portfolio

Represents a user's portfolio. Utilizes **composition** by storing a `list` of
`Stock` objects representing the shares in the portfolio. Also stores the
user's total amount of cash and provides operations such as buying and selling
stocks and calculating the total value of the portfolio.

#### Stock

Represents some amount of a particular stock. Maintains data items such as the
number of shares represented by the `Stock` object, as well as the stock's
ticker symbol, current price, and price history. Can be converted to and from
JSON.

## Development guide

*Note: These steps should work on Debian/Ubuntu systems. I'm not sure about
other operating systems.*

### Install tools

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

If you want to delete the virtual environment for some reason, simply delete
the `venv` directory, e.g. by running `rm -rf venv`.

#### Activating the virtual environment

Activate the virtual environment with:

```
source venv/bin/activate
```

You should see `(venv)` appear to the left of your shell prompt, indicating
that the virtual environment is active.

To deactivate the virtual environment, run `deactivate` or simply close your
terminal.

#### Checking python and pip

After activating the virtual environment for the first time, check that
`python` and `pip` are installed correctly.

If you run `python --version`, you should see some variant of `Python 3.6.x`.
And if you run `which python`, you should see a path that ends with
`venv/bin/python`. This means that if you run the `python` command from within
the active virtual environment, it will use the virtual environment's Python
interpreter.

Additionally, if you run `pip --version`, you should see output that includes
`python 3.6`, and if you run `which pip`, you should see a path that ends with
`venv/bin/pip`. If you run the `pip` command from within the virtual
environment, it will use the virtual environment's version of `pip` and will
install, uninstall, and otherwise manage packages within the virtual
environment, rather than modifying your machine's global Python environment.

#### Aliasing the activation command

You may want to alias the `source venv/bin/activate` command to something
shorter. For example, adding the following line to your shell's init file
(`~/.bashrc` if you're using `bash`) aliases the activation command to `va`:

```
alias va='source venv/bin/activate'
```

Reload `~/.bashrc` by running `source ~/.bashrc`, or simply start a new
terminal. Now you can simply run `va` from the project directory in order to
activate the virtual environment.

### Managing dependencies

**Warning:** Always make sure you've activated the virtual environment before
running `pip` commands, so that you do not accidentally modify your global
Python environment.

*Note: I'm still learning about `pip` and virtual environments. I do not claim
that these are the best practices for Python dependency management.*

#### Installing existing dependencies

After creating the virtual environment and activating it for the first time,
install the project dependencies specified in `requirements.txt`:

```
pip install -r requirements.txt
```

You should also run this command after pulling changes that add new
dependencies to `requirements.txt`.

#### Adding a dependency

In order to add a new dependency (where `PACKAGE` is the name of the Python
package you wish to add as a dependency, e.g. `Flask`):

1. Run `pip install PACKAGE` to install the package to the virtual
   environment.
2. Run `pip show PACKAGE` to show details about the package. There should be
   a `Version` line near the beginning of the output.
3. Add `PACKAGE>=VERSION` to `requirements.txt`, where `VERSION` is the package
   version specified by the `Version` line from the previous step.
4. Commit the changes to `requirements.txt`.

#### Removing a dependency

In order to remove a dependency that is no longer needed, run `pip uninstall
PACKAGE`, remove the package's line from `requirements.txt`, and commit the
changes to `requirements.txt`.

### Docker

As of 4/26/19, our web-app runs on Docker! After installing Docker
([Mac](https://www.docker.com/products/docker#/mac),
[Windows](https://www.docker.com/products/docker#/windows), or
[Linux](https://www.docker.com/products/docker#/linux)), run

```
docker build . -t stock-simulator 
```

and then

```
docker run -p 5000:5000 stock-simulator
```

Now, it should say somthing along the lines of "This app is running". If you
open a browser and go to 127.0.0.1:5000, you should see the wonderfully
feature-full Stock Simulator Web App in its full glory.
