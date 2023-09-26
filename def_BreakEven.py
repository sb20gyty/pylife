# Breakeven analysis 
# 1. Selling as scrap
# 2. Ingot production 
# Comparison of ingot production cost with different machines

import matplotlib.pyplot as plt

# Calculation of total loss if we sell the scrap parts 

def calculate_total_loss(weight_scrap_parts, cost_raw_material_per_ton, cost_selling_scrap_per_ton):
    total_raw_material_cost = cost_raw_material_per_ton * weight_scrap_parts
    total_selling_scrap_cost = cost_selling_scrap_per_ton * weight_scrap_parts
    total_loss = total_raw_material_cost - total_selling_scrap_cost
    return total_loss, total_raw_material_cost, total_selling_scrap_cost


# Cost of melting scrap parts in furnace

# From internet, 1 cubic metre natural gas = 10.28 kWh 
# For melting 1 ton of aluminium, 100 cubic metres natural gas is used (info from melters)
# gas_used_per_ton = 100 #(cubic metres)
# 100 cubic metres natural gas = 1028 kWh 

def calculate_total_cost_melting(weight_scrap_parts,cost_electricity, gas_price,melting_capacity_furnace_per_hour): 
    Energy_consumption_furnace = 600 * weight_scrap_parts; #(kWh/T)
    cost_operating_furnace = cost_electricity * Energy_consumption_furnace ;
    Cost_natural_gas = gas_price * 1028 * weight_scrap_parts / 100; 
    Time_required_melting = weight_scrap_parts / melting_capacity_furnace_per_hour; 
    
    cost_labor_furnace = 50 * Time_required_melting ;
    total_cost_melting = cost_operating_furnace + Cost_natural_gas + cost_labor_furnace ;
    return total_cost_melting

# 1. Hindenlang Ingot casting machine
    # casting capacity = 600kg/hr  
    #Energy consumption = 5kWh
def calculate_variable_cost_hindenlang(weight_scrap_parts, cost_electricity, total_cost_melting):
    time_required_casting_machine_hindenlang = weight_scrap_parts / 0.6 ;
    energy_consumption_casting_machine_hindenlang = 5 * time_required_casting_machine_hindenlang ;
    cost_of_operating_casting_machine_hindenlang = cost_electricity * energy_consumption_casting_machine_hindenlang ;
    cost_labor_hindenlang = 50 *  time_required_casting_machine_hindenlang ;
    variable_cost_hindenlang = cost_of_operating_casting_machine_hindenlang + cost_labor_hindenlang + total_cost_melting ;
    return variable_cost_hindenlang,time_required_casting_machine_hindenlang

# 2. Hormesa Ingot Casting Machine, Madrid
    # casting capacity = 4 Tonnes/hr
    # Energy consumption = 5kWh ---not sure from quotation
def calculate_variable_cost_hormesa(weight_scrap_parts, cost_electricity,total_cost_melting):
    time_required_casting_machine_hormesa =  weight_scrap_parts / 4 ;
    energy_consumption_casting_machine_hormesa = 3 * time_required_casting_machine_hormesa ;
    cost_of_operating_casting_machine_hormesa = cost_electricity * energy_consumption_casting_machine_hormesa ;
    cost_labor_Hormesa = 50 * time_required_casting_machine_hormesa ;
    variable_cost_hormesa = cost_of_operating_casting_machine_hormesa + cost_labor_Hormesa + total_cost_melting ;
    return variable_cost_hormesa, time_required_casting_machine_hormesa

# 3. McIntyre Ingot Casting Machine, Nottingham, UK
    # casting capacity = 1000kg/hr
    # Energy consumption = 5kWh -----not sure
def calculate_variable_cost_McIntyre(weight_scrap_parts, cost_electricity, total_cost_melting):
    time_required_casting_machine_McIntyre = weight_scrap_parts / 1 ;
    energy_consumption_casting_machine_McIntyre = 5 * time_required_casting_machine_McIntyre
    cost_of_operating_casting_machine_McIntyre = cost_electricity * energy_consumption_casting_machine_McIntyre
    cost_labor_McIntyre = 50 * time_required_casting_machine_McIntyre
    variable_cost_McIntyre = cost_of_operating_casting_machine_McIntyre + cost_labor_McIntyre + total_cost_melting;
    return variable_cost_McIntyre, time_required_casting_machine_McIntyre

# Total cost of making ingots with Hindenlang ingot casting

def calculate_total_cost_making_ingots_hindenlang(cost_ingot_casting_machine_hindenlang, variable_cost_hindenlang):
    total_cost_making_ingots_hindenlang = cost_ingot_casting_machine_hindenlang + variable_cost_hindenlang
    return total_cost_making_ingots_hindenlang

# Total cost of making ingots with Hormesa ingot casting

def calculate_total_cost_making_ingots_hormesa(cost_ingot_casting_machine_hormesa, variable_cost_hormesa):
    total_cost_making_ingots_hormesa = cost_ingot_casting_machine_hormesa + variable_cost_hormesa
    return total_cost_making_ingots_hormesa

# Total cost of making ingots with McIntyre ingot casting

def calculate_total_cost_making_ingots_McIntyre(cost_ingot_casting_machine_McIntyre, variable_cost_McIntyre):
    total_cost_making_ingots_McIntyre = cost_ingot_casting_machine_McIntyre + variable_cost_McIntyre
    return total_cost_making_ingots_McIntyre

# Total cost of making ingots manually

# Casting capacity = 500 kg/ hr (28kg ingots)

def calculate_total_cost_making_ingots_manually(weight_scrap_parts, total_cost_melting):
    time_required_casting_manually = weight_scrap_parts / 0.5
    total_cost_making_ingots_manually = (50 * time_required_casting_manually) + total_cost_melting
    return total_cost_making_ingots_manually, time_required_casting_manually


def calculate_casting_times(time_required_casting_machine_hindenlang,time_required_casting_machine_hormesa,time_required_casting_machine_McIntyre, time_required_casting_manually):

    machines = ['Present','Hindenlang','Hormesa','McIntyre']
    exact_times = [time_required_casting_manually, time_required_casting_machine_hindenlang, time_required_casting_machine_hormesa, time_required_casting_machine_McIntyre]
    
    return machines, exact_times


# Given Data
weight_scrap_parts = float(input("Enter the weight of scrap parts (in Tonnes): "))
cost_raw_material_per_ton = 4400
cost_selling_scrap_per_ton = 1650
melting_capacity_furnace_per_hour = 1
cost_electricity = 0.8
gas_price = 8.8 #(cents/kWh)

# Cost of casting machines in €,fixed costs
cost_ingot_casting_machine_hindenlang = 140000
cost_ingot_casting_machine_hormesa = 80000  
cost_ingot_casting_machine_McIntyre = 75000 

# Other constants
annual_maintenance_cost = 0

# Calculate total loss if material sold as scrap
total_loss = calculate_total_loss(weight_scrap_parts, cost_raw_material_per_ton, cost_selling_scrap_per_ton)

# Calculate melting cost
total_cost_melting = calculate_total_cost_melting(weight_scrap_parts,cost_electricity,gas_price,melting_capacity_furnace_per_hour)

# Calculate variable costs and time required for casting
variable_cost_hindenlang, time_required_casting_machine_hindenlang = calculate_variable_cost_hindenlang(weight_scrap_parts, cost_electricity, total_cost_melting)
variable_cost_hormesa,time_required_casting_machine_hormesa = calculate_variable_cost_hormesa(weight_scrap_parts, cost_electricity, total_cost_melting)
variable_cost_McIntyre,time_required_casting_machine_McIntyre = calculate_variable_cost_McIntyre(weight_scrap_parts, cost_electricity, total_cost_melting)


# Calculate total cost of making ingots
total_cost_making_ingots_hindenlang = calculate_total_cost_making_ingots_hindenlang(cost_ingot_casting_machine_hindenlang, variable_cost_hindenlang)
total_cost_making_ingots_hormesa = calculate_total_cost_making_ingots_hormesa(cost_ingot_casting_machine_hormesa, variable_cost_hormesa)
total_cost_making_ingots_McIntyre = calculate_total_cost_making_ingots_McIntyre(cost_ingot_casting_machine_McIntyre, variable_cost_McIntyre)
total_cost_making_ingots_manually, time_required_casting_manually = calculate_total_cost_making_ingots_manually(weight_scrap_parts, total_cost_melting)

# cost of making ingots without melting scrap
# Using only leftover melt from melting and dosing furnace
cost_ingot_without_melting_hindenlang = total_cost_making_ingots_hindenlang - total_cost_melting
cost_ingot_without_melting_hormesa = total_cost_making_ingots_hormesa - total_cost_melting
cost_ingot_without_melting_McIntyre = total_cost_making_ingots_McIntyre - total_cost_melting
cost_ingot_without_melting_manually = total_cost_making_ingots_manually - total_cost_melting


# 3. Material costs 
total_loss, total_raw_material_cost, total_selling_scrap_cost = calculate_total_loss(weight_scrap_parts, cost_raw_material_per_ton, cost_selling_scrap_per_ton)

# Print the results

print("Total loss if material sold as scrap:", total_loss, "€")
print("Variable cost for making ingots with Hindenlang:", variable_cost_hindenlang, "€")
print("Variable cost for making ingots with Hormesa:", variable_cost_hormesa, "€")
print("Variable cost for making ingots with McIntyre:", variable_cost_McIntyre, "€")
print("Total cost of making ingots with Hindenlang:", total_cost_making_ingots_hindenlang, "€")
print("Total cost of making ingots with Hormesa:", total_cost_making_ingots_hormesa, "€")
print("Total cost of making ingots with McIntyre:", total_cost_making_ingots_McIntyre, "€")
print("Total cost of making ingots with current practice:", total_cost_making_ingots_manually, "€")
print("Total cost of melting scrap:", total_cost_melting, "€")


if total_loss > total_cost_making_ingots_hindenlang:
    print("Purchasing Hindelang ingot machine is worth it")

if total_loss > total_cost_making_ingots_hormesa:
    print("Purchasing Hormesa ingot machine is valuable for production of", weight_scrap_parts, "Tonnes of ingots")

if total_loss > total_cost_making_ingots_McIntyre:
    print("Purchasing McIntyre ingot machine is valuable for production of", weight_scrap_parts,"Tonnes of ingots")


# plotting


 
# 1. Time taken for casting using different machines


machines, exact_times = calculate_casting_times(time_required_casting_machine_hindenlang,time_required_casting_machine_hormesa,time_required_casting_machine_McIntyre, time_required_casting_manually)
times = [round(time,2) for time in exact_times]

# 2. Comparison of costs 
exact_costs = [total_cost_making_ingots_manually, total_cost_making_ingots_hindenlang, total_cost_making_ingots_hormesa, total_cost_making_ingots_McIntyre] 
costs = [round(cost,2) for cost in exact_costs]




# Grid of plots (2 row, 2 columns)

fig, axs = plt.subplots(2,2, figsize=(12,10))

# Plot 1: Bar chart for comparing time taken

bars1 = axs[0,0].bar(machines,times, color = ['magenta', 'orange', 'red', 'cyan'])
#axs[0,0].set_xlabel('Machines')
axs[0,0].set_ylabel('Casting time (hours)')
axs[0,0].set_title('Time taken by using different machines')

for bar in bars1:
    yval = bar.get_height()
    axs[0,0].text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval} hours',ha='center', va='bottom', fontsize=10)


# Plot 2 : Bar chart for comparing cost of making ingots

bars2 = axs[0,1].bar(machines,costs, color = ['magenta', 'orange', 'red', 'cyan'])
#axs[0,1].set_xlabel('Machines')
axs[0,1].set_ylabel('Cost of making ingots (€)')
axs[0,1].set_title('Total Cost of Making Ingots by Different Machines')

for bar in bars2:
    yval = bar.get_height()
    axs[0,1].text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval} €',ha='center', va='bottom', fontsize=10)


# Plot 3: Bar chart for comparing costs of making ingots without melting:

exact_cost_wo_melting = [cost_ingot_without_melting_manually, cost_ingot_without_melting_hindenlang, cost_ingot_without_melting_hormesa, cost_ingot_without_melting_McIntyre]

cost_ingot_without_melting = [round(cost,2) for cost in exact_cost_wo_melting]

bars3 = axs[1,0].bar(machines,cost_ingot_without_melting, color = ['magenta', 'orange', 'red', 'cyan'])
#axs[1,0].set_xlabel('Machines')
axs[1,0].set_ylabel('Cost of making ingots without melting scrap(€)')
axs[1,0].set_title('Total Cost of Making Ingots without melting scraps')

for bar in bars3:
    yval = bar.get_height()
    axs[1,0].text(bar.get_x() + bar.get_width()/2, yval + 0.2, f'{yval} €',ha='center', va='bottom', fontsize=10)

# Plot 4: Bar chart for cost of material at different stages

Material_stages = ['Raw material', 'Total loss', ' Scrap cost ']
material_costs = [total_raw_material_cost, total_loss, total_selling_scrap_cost]
bars4 = axs[1,1].bar(Material_stages,material_costs, color = ['magenta', 'orange', 'red', 'cyan'])
#axs[1,1].set_xlabel('Material Stage')
axs[1,1].set_ylabel('Cost of Material at different stages (€)')
axs[1,1].set_title('Comparison of material cost at different stages')


for i, v in enumerate(material_costs):
    axs[1, 1].text(i, v + 2, f'{v}€', ha='center', va='bottom')

# Show the plot

plt.tight_layout()
plt.show()
