# -*- coding: utf-8 -*-
import pybamm
import matplotlib.pyplot as plt
	
# simulate US06 drive cycle (duration 600 seconds)
model=pybamm.lithium_ion.DFN()

chemistry = pybamm.parameter_sets.SMP2020test
parameter_values = pybamm.ParameterValues(chemistry=chemistry)

sim =  pybamm.Simulation(model,parameter_values=parameter_values,solver=pybamm.CasadiSolver())

sim.solve([0,3600])
time = sim.solution["Time [s]"].entries
capacity = sim.solution["Discharge capacity [A.h]"]
current = sim.solution["Current [A]"]
voltage = sim.solution["Terminal voltage [V]"]
c1=capacity(time) 
c2=voltage(time)
c3=current(time)
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.plot(time,c2)
plt.show() 
 

    
    