class Asset:
      def __init__(self, name, age):
          self.name = name
          self.age = age
          self.owner = "bfsu"
      def makemoney(self):
          print(self.owner,"is making big money")