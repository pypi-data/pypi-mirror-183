# Financial Pie

Improved version of Fi-Pye.

# Table of Contents
* [About the project](#About)
* [Getting started](#getting-started)
* [Using readers](#usage)
  * [Api docs](#api-developer-docs)
  * [Instantiating readers](#instantiation)


# About
Financial Pie is built to obtain stock-related data from various API's.
Currently, this package supports calls to Financial Modeling Prep and 
Nasdaq API endpoints, but more will be added over time.

# Getting started
Clone this repo and use pip to locally install the package

```commandline
pip install .
```

# Usage

After pip installing the package, you can start obtaining data by importing
a certain reader (Either FMP or Nasdaq) and then instantiating it with your
api_key. If you don't have any API key already, you can check out their
dev docs below.

## API developer docs

Data providers
- Financial Modeling Prep (FMP): https://site.financialmodelingprep.com/developer/docs/
- Nasdaq Data Link: https://data.nasdaq.com/tools/api


## Instantiation
To instantiate a reader, import the reader containing the endpoint methods
you wish to get data from. For example if I wanted to get data from
Financial Modeling Prep endpoints pertaining to Analysts, I can do the
following:

```python
from financial_pie.Fmp.analysts import Analysts

analysts = Analysts(api_key="abc123")

# Now you can get data from Analysts methods like so.
aapl_upgrades_n_downgrades = analysts.upgrades_and_downgrades(symbol="AAPL")
```

If you would like to import multiple readers and maintain the same requests
Session object amongst them all, you can pass the first session object to the other
readers during their instantiation. This can be done with the following:

```python
from financial_pie.Fmp.senators import Senators
from financial_pie.Fmp.fundamentals import Fundamentals

SYMBOL: str = "MSFT"

senators = Senators(api_key="abc123")
fundamentals = Fundamentals(api_key="abc123", session=senators.session)

# Persist 'SYMBOL' across multiple calls.
senator_trades = senators.senate_trading(symbol=SYMBOL)
quarterly_cash_flows = fundamentals.cash_flow(symbol=SYMBOL, period="quarter", limit=15)
```