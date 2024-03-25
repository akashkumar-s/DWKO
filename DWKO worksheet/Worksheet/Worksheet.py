class main_motor:
    def __init__(self, regime):
        self.regime = regime
    
    def arm_current(self):
        self.arm_current
        orders={"DSAH":600,
                "SAH":1400,
                "HAH":1600,
                "FAH":4500}
        self.arm_current=orders.get(self.regime)
        print(self.arm_current)      


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

x=main_motor("DSAH")
x.arm_current;