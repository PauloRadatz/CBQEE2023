# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 1:41 PM
# @Author  : Paulo Radatz

# @File    : Parte1-2-b.py
# @Software: PyCharm

from compile_123bus import compile_123bus

dss = compile_123bus()

dss.text("batchedit capacitor..* enabled=No")

dss.text("solve")

dss.text("plot profile")

kw_losses = dss.circuit_losses()[0] / 1000.0
print(f"Losses in kW = {round(kw_losses, 2)}")
