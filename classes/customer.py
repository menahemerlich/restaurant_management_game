
class Customer:
    def __init__(self, name: str, satisfaction: int = 50):
        self.name = name
        self.satisfaction = satisfaction

    def increase_satisfaction(self, amount: int):
        if 0 < (self.satisfaction + amount) <= 100:
            self.satisfaction += amount
        else:
            print("Out of range.")

    def decrease_satisfaction(self, amount: int):
        if 0 < (self.satisfaction - amount) <= 100:
            self.satisfaction -= amount
        else:
            print("Out of range.")

    def is_happy(self):
        if self.satisfaction > 70:
            return True
        return False

    def get_info(self):
        return f"name: {self.name}, satisfaction: {self.satisfaction}"

    



