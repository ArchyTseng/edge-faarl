import pytest
from src.data_fetch import fetch_stock_data

def test_fetch_stock_data():
    """
    Test stock data fetching.
    """
    data = fetch_stock_data("AAPL", "2022-01-01", "2022-01-31")
    assert not data.empty, "Data should not be empty"
    assert data.index.name == "Date", "Index should be named 'Date'"
    assert 'Close' in data.columns, "Data should have a 'Close' column"
    assert 'Volume' in data.columns, "Data should have a 'Volume' column"
    assert 'Open' in data.columns, "Data should have an 'Open' column"
    assert 'High' in data.columns, "Data should have a 'High' column"
    assert 'Low' in data.columns, "Data should have a 'Low' column"



