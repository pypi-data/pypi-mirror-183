import numpy as np
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
