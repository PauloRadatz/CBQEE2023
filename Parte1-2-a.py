# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 1:32 PM
# @Author  : Paulo Radatz

# @File    : 1.py
# @Software: PyCharm

from compile_123bus import compile_123bus

dss = compile_123bus()
dss.text("solve")

dss.text("plot profile")

kw_losses = dss.circuit_losses()[0] / 1000.0
print(f"Losses in kW = {round(kw_losses, 2)}")
