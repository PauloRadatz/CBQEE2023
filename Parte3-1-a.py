# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 5:08 PM
# @Author  : Paulo Radatz

# @File    : Parte3-1-a.py
# @Software: PyCharm

from compile_123bus import compile_123bus

dss = compile_123bus()

dss.text("batchedit regcontrol..* enabled=No")
dss.text("batchedit load..* enabled=No")

dss.text("new fault.3_pf_95 phases=3 bus1=95")

dss.text("solve")

dss.text("plot profile")

dss.circuit.set_active_bus("8")
v_8_min = min(dss.bus.vmag_angle_pu[0:6:2])
v_8_max = max(dss.bus.vmag_angle_pu[0:6:2])
dss.circuit.set_active_bus("57")
v_57_min = min(dss.bus.vmag_angle_pu[0:6:2])
v_57_max = max(dss.bus.vmag_angle_pu[0:6:2])

print("Sag")
print(f"Mag VTCD 8 = {round(v_8_min, 2)} Vpu")
print(f"Mag VTCD 57 = {round(v_57_min, 2)} Vpu")

print("Swell")
print(f"Mag VTCD 8 = {round(v_8_max, 2)} Vpu")
print(f"Mag VTCD 57 = {round(v_57_max, 2)} Vpu")
