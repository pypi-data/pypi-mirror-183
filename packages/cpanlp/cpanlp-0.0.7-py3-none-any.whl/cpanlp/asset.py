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