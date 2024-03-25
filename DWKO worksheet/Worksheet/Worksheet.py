class main_motor:
    def __init__(self, regime):
        self.regime = regime
    
    def arm_current(self):
        orders={"DSAH": [600, 150],
                "SAH": [1400, 200],
                "HAH": [1600, 260],
                "FAH": [4500, 360]}
        self.arm_current = orders.get(self.regime)[1]
        return self.arm_current

class Eco_motor:
    pass

class Present_status:
    pass

class battries:
    pass

class charging_plan:
    pass

class major_machineries:
    pass

x = main_motor("DSAH")
print(x.arm_current())  # Corrected: calling arm_current() method
