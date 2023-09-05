# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 5:22 PM
# @Author  : Paulo Radatz

# @File    : Parte3-2-a-1.py
# @Software: PyCharm

from compile_123bus import compile_123bus

v_1 = 0.1
v_2 = 0.5
v_3 = 0.95

dss = compile_123bus()

dss.text("batchedit regcontrol..* enabled=No")
dss.text("batchedit load..* enabled=No")

dss.text("new fault.3_ph_95 phases=3 bus1=95")

dss.text("solve")

bus_color_dict = dict()
for bus in dss.circuit.buses_names:
    dss.circuit.set_active_bus(bus)
    if len(dss.bus.nodes) >= 3 and dss.bus.x:
        v_min = min(dss.bus.vmag_angle_pu[0:6:2])

        if v_min < v_1:
            bus_color_dict[bus] = "black"
        elif v_min < v_2:
            bus_color_dict[bus] = "red"
        elif v_min < v_3:
            bus_color_dict[bus] = "yellow"
        else:
            bus_color_dict[bus] = "green"

for bus_name, color in bus_color_dict.items():
    dss.text(f"AddBusMarker Bus={bus_name} code=7 color={color} size=10")

dss.text("plot circuit Power max=2000 n n C1=$00FF0000")
