import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(500, 2000, 1000)


def test_transfer_and_interest_workflow():
    from_balance, to_balance = transfer(8000, 1000, 3000)
    final_balance = calculate_interest(to_balance, 10, 1)
    assert round(final_balance, 2) == 4400.00


def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(5000, 2000, -200)
