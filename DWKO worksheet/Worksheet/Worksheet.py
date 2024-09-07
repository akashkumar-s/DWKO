
class MainMotor:
    def __init__(self, regime):
        self.regime = regime
        self.specs = self.get_motor_specs()

    def get_motor_specs(self):
        orders = {
            "DSAH": [(140, 600), (180, 750)], 
            "SAH": [(200, 1400), (250, 1600)], 
            "HAH": [(260, 1600), (300, 1800)],
            "FAH": [(340, 4500), (370, 4600)]  
        }
        if self.regime in orders:
            return orders[self.regime]
        else:
            raise ValueError(f"Unknown regime: {self.regime}")

    def interpolate(self, target_rpm):
        rpms = sorted([spec[0] for spec in self.specs])
        if target_rpm in rpms:
            for spec in self.specs:
                if spec[0] == target_rpm:
                    return spec[1]
        
        for i in range(len(rpms) - 1):
            if rpms[i] <= target_rpm <= rpms[i + 1]:
                rpm0, current0 = self.specs[i]
                rpm1, current1 = self.specs[i + 1]
                
                current = current0 + (current1 - current0) * (target_rpm - rpm0) / (rpm1 - rpm0)
                
                return current
        
        raise ValueError(f"RPM {target_rpm} is out of interpolation range.")

    def arm_current(self, rpm):
        return self.interpolate(rpm)

class EcoMotor:
    def __init__(self, regime):
        self.regime = regime
        self.current_drawn, self.rpm = self.get_motor_specs()

    def get_motor_specs(self):
        orders = {
            "DSAH": [150, 80],
            "SAH": [250, 100],
            "HAH": [350, 125],
            "FAH": [650, 150]
        }
        if self.regime in orders:
            return orders[self.regime]
        else:
            raise ValueError(f"Unknown regime: {self.regime}")

    def arm_current(self):
        return self.current_drawn

    def motor_rpm(self):
        return self.rpm


class machine:
    def __init__(self, name, starting_current, running_current):
        self.name = name
        self.starting_current = starting_current
        self.running_current = running_current
        self.active = True

    def get_current(self, regime):
        if self.active:
            print(self.name)
            return self.running_current if regime == 'running' else self.running_current
            
        return 0


class compartments:
    def __init__(self, name):
        self.name = name
        self.machines = []
        self.initialize_machines()

    def initialize_machines(self):
        if self.name == "F/E":
            self.machines.append(machine("Battery Blower no 1", 10.6, 2.8))
            self.machines.append(machine("Battery Blower no 2", 10.3, 2.9))
            self.machines.append(machine("Compartment Blower", 19.5, 5.3))
            self.machines.append(machine("Sonar Blower", 10, 2.5))
            self.machines.append(machine("WC Blower", 24, 7.5))
            self.machines.append(machine("1B1", 5, 2.4))
            self.machines.append(machine("BO 25", 22, 6.2))
        
        elif self.name == "C/R":
            self.machines.append(machine("40/15 DM water pump", 40, 14.5))
            self.machines.append(machine("5/17 Panel Cooling Pump", 9.5, 2.7))
            self.machines.append(machine("40/15 C/W pump", 45, 21))
            self.machines.append(machine("Ref Plant", 70, 22))
            self.machines.append(machine("1B1", 5, 2.03))
            self.machines.append(machine("1-2-3 Blower no 1", 22.5, 5.5))
            self.machines.append(machine("1-2-3 Blower no 2", 23.2, 6.0))
            self.machines.append(machine("Sonar Blower", 9.4, 3.2))
            self.machines.append(machine("WT and Gyro Blower", 22, 6.5))
            self.machines.append(machine("127V 50Hz Alt no 1", 310, 20))
            self.machines.append(machine("220V 400Hz Alt no 2", 370, 25))
            self.machines.append(machine("2P1", 203, 20))
            self.machines.append(machine("6MBX2", 348, 60))
            self.machines.append(machine("40/15 S/W pump", 45, 19))
            self.machines.append(machine("Aux Cooling SN 23 no 1", 46, 21.5))
            self.machines.append(machine("Aux Cooling SN 23 no 2", 47.6, 22))
            self.machines.append(machine("Appassionate 5/17 pump no 1", 9.5, 3.6))
            self.machines.append(machine("Appassionate 5/17 pump no 2", 10, 3.9))
            self.machines.append(machine("Hydraulic pump no 1", 165, 33))
            self.machines.append(machine("Hydraulic pump no 2", 150, 30))
            self.machines.append(machine("15MBOO no 1", 9.5, 2.02))
            self.machines.append(machine("15MBOO no 1", 9, 2.01))
            self.machines.append(machine("Condencer cooling pump", 45, 21))
            self.machines.append(machine("20 TR", 140, 55))
            self.machines.append(machine("Provision room blower", 16, 1.5))
            
        elif self.name == "Third":
            self.machines.append(machine("Galley Supply blower", 11.5, 4.01))
            self.machines.append(machine("Galley air purifier blower", 21, 5))
            self.machines.append(machine("1B1", 5, 2.3))
            self.machines.append(machine("Galley Blower", 9.1, 2.02))
            self.machines.append(machine("Provision room blower", 4.5, 1.9))
            self.machines.append(machine("Battery Blower no 1", 10.5, 3))
            self.machines.append(machine("Battery Blower no 2", 10.2, 2.9))
            self.machines.append(machine("Compartment Blower", 10.5, 5.1))
            
        elif self.name == "E/R":
            self.machines.append(machine("Standard Blower", 19.7, 7))
            self.machines.append(machine("Supply Blower", 150, 60))
            self.machines.append(machine("Exhaust Blower", 150, 65))
            self.machines.append(machine("Sulzer Compressor Motor", 450, 200))
            self.machines.append(machine("1B1", 13, 5))
            self.machines.append(machine("10MBOO", 5, 2.01))
            self.machines.append(machine("35MBOO(P)", 8, 2.7))
            self.machines.append(machine("35MBOO(S)", 8, 2.8))
            self.machines.append(machine("DG Blower(P)", 193, 43))
            self.machines.append(machine("DG Blower(S)", 165, 39))
            self.machines.append(machine("Lube Oil Pump 1", 45, 18))
            self.machines.append(machine("Lube Oil Pump 2", 41, 13))
            self.machines.append(machine("Shaft Cooling Pump 1", 25, 19))
            self.machines.append(machine("Shaft Cooling Pump 2", 26, 15))
            self.machines.append(machine("Shaft Cooling Pump 3", 25, 7))
            self.machines.append(machine("Emergency Fresh water pump", 24, 9))
        
        elif self.name == "M/R":
            self.machines.append(machine("127V 50Hz Alt no 1", 305, 18))
            self.machines.append(machine("220V 400Hz Alt no 2", 350, 22))
            self.machines.append(machine("1B1", 5, 2.7))
            self.machines.append(machine("MM Blower Fwd", 260, 90))
            self.machines.append(machine("MM Blower Aft", 260, 90))
            self.machines.append(machine("35MBOO(P)", 7.3, 2.5))
            self.machines.append(machine("35MBOO(S)", 7.5, 2.6))
            self.machines.append(machine("Sulzer Compressor Motor", 480, 180))
            self.machines.append(machine("Lube Oil Pump 3", 38, 16))
            self.machines.append(machine("Lube Oil Pump 4", 39, 16.9))
            self.machines.append(machine("ECO Shaft Cooling Pump 5/17", 12, 4))
            self.machines.append(machine("Aux Cooling SN 23 no 3", 45, 22))
            self.machines.append(machine("Aux Cooling SN 23 no 5", 47, 21))
            self.machines.append(machine("40/15 C/W pump", 40, 15))
            self.machines.append(machine("47 TR", 45, 22))
            self.machines.append(machine("Compartment Blower", 10, 4.5))
            self.machines.append(machine("Compartment Air Purifier", 7.2, 2.3))
        
        elif self.name == "A/E":
            self.machines.append(machine("2P1", 200, 21))
            self.machines.append(machine("1B1", 5, 2.3))
            self.machines.append(machine("Hydraulic pump no 1", 165, 33))
            self.machines.append(machine("Hydraulic pump no 2", 150, 30))
            self.machines.append(machine("Reserve Motor(P)", 750, 350))
            self.machines.append(machine("Reserve Motor(S)", 750, 360))
            self.machines.append(machine("Reserve Motor blower(P)", 15.6, 6.3))
            self.machines.append(machine("Reserve Motor blower(S)", 18.4, 6.7))
            self.machines.append(machine("Compartment Blower", 13, 7.6))
            self.machines.append(machine("Compartment Air Purifier", 6.2, 2.8))
            self.machines.append(machine("10MBOO", 5, 2.01))


    def set_machine_exclusions(self, excluded_machines):
        for machine in self.machines:
            if machine.name in excluded_machines:
                machine.active = False
            else:
                machine.active = True
            print(f"Machine {machine.name} active status: {machine.active}")
    
    def get_total_current(self, regime='running'):
        total_current = sum(machine.get_current(regime) for machine in self.machines)
        print(f"Total current for compartment {self.name}: {total_current} A")
        return total_current

import numpy as np
class BatteryPerformance:
    def __init__(self):
        self.performance_data = {
            1: (8300, 1.76, 1.60, 8300),
            2: (5800, 1.78, 1.60, 11600),
            3: (4443, 1.85, 1.58, 13330),
            5: (3004, 1.91, 1.60, 15020),
            10: (1630, 1.93, 1.70, 16300),
            20: (923.5, 1.95, 1.75, 18470),
            50: (408, 1.96, 1.70, 20200),
            100: (204, 1.97, 1.70, 20400)
        }
        self.usage_limit = 0.50  # Only 50% usage before recharging

    def interpolate_capacity(self, discharge_current):
        # Extract data into arrays for interpolation
        discharge_rates = np.array(sorted(self.performance_data.keys()))
        discharge_currents = np.array([self.performance_data[rate][0] for rate in discharge_rates])
        capacities = np.array([self.performance_data[rate][3] for rate in discharge_rates])
        
        # Interpolate between discharge currents and capacities
        capacity = np.interp(discharge_current, discharge_currents, capacities)
        return capacity * self.usage_limit  # Apply 50% usage limit
    
    def get_battery_duration(self, current_draw):
        capacity = self.interpolate_capacity(current_draw)
        duration = capacity / current_draw  # hours the battery can last
        return duration

class boat:
    def __init__(self, main_motor_regime):
        self.compartments = [
            compartments("F/E"),
            compartments("C/R"),
            compartments("Third"),
            compartments("E/R"),
            compartments("M/R"),
            compartments("A/E")
        ]
        self.battery_performance = BatteryPerformance()  # Integrate battery performance
        self.main_motor = MainMotor(main_motor_regime)  # Initialize with the appropriate regime

    def set_regime(self, regime):
        if regime == "Snorting":
            # Set all machines running except for the ones that shouldn't be running in F/E
            self.compartments[0].set_machine_exclusions(["1B1"])
            self.compartments[1].set_machine_exclusions(["1B1","2P1","6MBX2","Aux Cooling SN 23 no 1","Appassionate 5/17 pump no 1"])
            self.compartments[2].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[3].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[4].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[5].set_machine_exclusions(["Reserve Motor(P)"])
        elif regime == "Consuming":
            self.compartments[0].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[1].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[2].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[3].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[4].set_machine_exclusions(["Reserve Motor(P)"])
            self.compartments[5].set_machine_exclusions(["Reserve Motor(P)"])
        else:
            for compartment in self.compartments:
                compartment.set_machine_status([])

    def get_total_current(self, regime='running'):
        return sum(compartment.get_total_current(regime) for compartment in self.compartments)

    def calculate_battery_duration(self, current_draw):
        return self.battery_performance.get_battery_duration(current_draw)
    
    def calculate_required_speed(self, distance, battery_life_hours):
        # Speed = Distance / Time
        required_speed = distance / battery_life_hours
        return required_speed
    
    def calculate_speed_over_ground(self):
        # Get RPM from MainMotor
        motor_rpm = self.main_motor.specs[0][0]  # Assuming you want RPM of the first specification
        # Calculate speed in knots
        speed = (motor_rpm / 50) - 0.5
        return speed

    # # Example usage
    # main_motor_regime = "DSAH"  # Example regime
    # my_boat = boat(main_motor_regime)
    # my_boat.set_regime("Snorting")  # Set a specific regime
    # total_current_draw = my_boat.get_total_current()
    #
    # # Calculate battery life based on the total current draw with 50% usage limitation
    # battery_life_hours = my_boat.calculate_battery_duration(total_current_draw)
    #
    # # Calculate speed over ground using motor RPM
    # speed_over_ground = my_boat.calculate_speed_over_ground()
    #
    # print(f"Total current draw: {total_current_draw} A")
    # print(f"Battery will last for: {battery_life_hours:.2f} hours (50% usage limit)")
    # print(f"Speed over ground: {speed_over_ground:.2f} knots based on motor RPM of {my_boat.main_motor.specs[0][0]}")
    # # Example usage
main_motor_regime = "DSAH"  # Example regime
my_boat = boat(main_motor_regime)
my_boat.set_regime("Snorting")  # Set a specific regime

# Print compartment and machine details
for compartment in my_boat.compartments:
    print(f"\nCompartment: {compartment.name}")
    for machine in compartment.machines:
        print(f"Machine: {machine.name}, Starting Current: {machine.starting_current}, Running Current: {machine.running_current}, Active: {machine.active}")

# Calculate and print total current for each compartment
for compartment in my_boat.compartments:
    total_current = compartment.get_total_current()
    print(f"Total current for {compartment.name}: {total_current} A")

# Calculate total current draw and battery life
total_current_draw = my_boat.get_total_current()
battery_life_hours = my_boat.calculate_battery_duration(total_current_draw)

# Calculate speed over ground using motor RPM
speed_over_ground = my_boat.calculate_speed_over_ground()

print(f"\nTotal current draw: {total_current_draw} A")
print(f"Battery will last for: {battery_life_hours:.2f} hours (50% usage limit)")
print(f"Speed over ground: {speed_over_ground:.2f} knots based on motor RPM of {my_boat.main_motor.specs[0][0]}")
