import datetime
class liability:
    def __init__(self, name, amount, due_date):
        self.name = name
        self.amount = amount
        self.due_date = due_date
    
    def __str__(self):
        return f"Liability(name='{self.name}', amount={self.amount}, due_date='{self.due_date}')"

    def is_due(self):
        """判断负债是否已到期"""
        today = datetime.date.today()
        due_date = datetime.datetime.strptime(self.due_date, "%Y-%m-%d").date()
        return today > due_date
#在上面的代码中，我们添加了一个名为 is_due 的方法，用于判断负债是否已到期。该方法使用 Python 的 datetime 模块来比较当前日期和负债的到期日期，并返回布尔值。





