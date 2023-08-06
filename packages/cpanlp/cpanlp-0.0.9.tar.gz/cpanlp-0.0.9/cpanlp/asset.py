import numpy as np
from typing import List, Tuple
from datetime import datetime, timedelta

class asset:
    def __init__(self, name: str, category: str, value: float):
        self.name = name
        self.category = category
        self.value = value
    
    def __repr__(self):
        return f"Asset({self.name}, {self.category}, {self.value})"
    
    def total_value(assets):
        """Calculates the total value of a list of assets."""
        total = 0
        for asset in assets:
            total += asset.value
        return total
    
    def generate_report(assets):
        """Generates a report with information about a list of assets."""
        report = "ASSET REPORT\n"
        for i in assets:
            report += f"{i.name} ({i.category}): ${i.value}\n"
        report += f"Total value: ${asset.total_value(assets)}"
        return report
    def makemoney(self):
        print(self.name,"is making big money")
        return np.array([6, 7, 8])
class bankdeposit(asset):
    def __init__(self, name: str, category: str, value: float, interest_rate: float):
        super().__init__(name, category, value)
        self.interest_rate = interest_rate

    def get_interest_earned(self, start_date: str, end_date: str) -> float:
        return (end_date - start_date).days * self.interest_rate * self.value
class realestate(asset):
    def __init__(self, name, category, value, address):
        super().__init__(name, category, value)
        self.address = address
    
    def __str__(self):
        return f"RealEstate(name='{self.name}', value={self.value}, address='{self.address}')"
class stock(asset):
    def __init__(self, name, category, value, symbol, market):
        super().__init__(name, category, value)
        self.symbol = symbol
        self.market = market
    
    def __str__(self):
        return f"Stock(name='{self.name}', value={self.value}, symbol='{self.symbol}', market='{self.market}')"
class assetdepreciation:
    def __init__(self, cost, salvage_value, life):
        self.cost = cost
        self.salvage_value = salvage_value
        self.life = life

    def straight_line_depreciation(self):
        annual_depreciation = (self.cost - self.salvage_value) / self.life
        return annual_depreciation
class assetamortization(assetdepreciation):
    def __init__(self, cost, salvage_value, life, rate):
        super().__init__(cost, salvage_value, life)
        self.rate = rate

    def get_amortization_schedule(self):
        schedule = []
        annual_depreciation = self.straight_line_depreciation()
        for year in range(1, self.life + 1):
            amortization = self.cost * self.rate
            depreciation = annual_depreciation
            self.cost -= (amortization + depreciation)
            schedule.append((year, amortization, depreciation))
        return schedule
class assetbubble:
    def is_asset_bubble(self, price: float) -> bool:
        return price > 100
class transaction:
    def __init__(self, item: str, cost: float, quantity: int):
        self.item = item
        self.cost = cost
        self.quantity = quantity

class costaccounting:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction: transaction):
        self.transactions.append(transaction)

    def get_cost(self, item: str) -> float:
        cost = 0
        for transaction in self.transactions:
            if transaction.item == item:
                cost += transaction.cost * transaction.quantity
        return cost
class investment:
    def __init__(self, date: str, value: float):
        self.date = date
        self.value = value

class equityinvestmentaccounting:
    def __init__(self):
        self.investments = []

    def add_investment(self, investment: investment):
        self.investments.append(investment)

    def get_value(self, date: str) -> float:
        value = 0
        for investment in self.investments:
            if investment.date <= date:
                value += investment.value
        return value

    def get_return(self, start_date: str, end_date: str) -> float:
        start_value = self.get_value(start_date)
        end_value = self.get_value(end_date)
        return (end_value - start_value) / start_value
class financialasset:
    def __init__(self, name: str, value: float, date: str):
        self.name = name
        self.value = value
        self.date = date

class financialassetaccounting:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset: financialasset):
        self.assets.append(asset)

    def get_value(self, date: str) -> float:
        value = 0
class fairvaluefinancialasset(financialasset):
    def update_value(self, value: float):
        self.value = value