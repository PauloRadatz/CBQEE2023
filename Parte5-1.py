# -*- coding: utf-8 -*-
# @Time    : 9/5/2023 3:36 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Parte5-1.py
# @Software: PyCharm

import numpy as np
from compile_123bus import compile_123bus

dss = compile_123bus()
dss.text("batchedit regcontrol..* enabled=No")
dss.text("Solve")

dss.circuit.set_active_bus("95")

volts_seq_95 = dss.bus.cplx_sequence_voltages
v0 = abs(volts_seq_95[0] + 1j * volts_seq_95[1])
v1 = abs(volts_seq_95[2] + 1j * volts_seq_95[3])
v2 = abs(volts_seq_95[4] + 1j * volts_seq_95[5])

FD = v2 / v1 * 100

volts_95 = dss.bus.voltages

vab = abs((volts_95[0] - volts_95[2]) + 1j * (volts_95[1] - volts_95[3]))
vbc = abs((volts_95[2] - volts_95[4]) + 1j * (volts_95[3] - volts_95[5]))
vca = abs((volts_95[4] - volts_95[0]) + 1j * (volts_95[5] - volts_95[1]))

beta = (vab ** 4 + vbc ** 4 + vca ** 4) / (vab ** 2 + vbc ** 2 + vca ** 2) ** 2

FD_cigre = 100 * np.sqrt((1 - np.sqrt(3 - 6 * beta)) / (1 + np.sqrt(3 - 6 * beta)))


print(f"FD ANEEL = {round(FD, 2)} %\nFD Cigre = {round(FD_cigre, 2)} %")