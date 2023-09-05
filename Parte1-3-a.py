# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 2:08 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Parte1-3-a.py
# @Software: PyCharm

from compile_123bus import compile_123bus

dss = compile_123bus()

dss.text("batchedit regcontrol..* enabled=No")

dss.text(f"batchedit load..* daily=default")
dss.text("New Monitor.power element=Line.L115 terminal=1 mode=1 ppolar=NO")

dss.text("set mode=daily")
dss.text("solve")

file = dss.text("Export monitors power")
dss.text("Plot monitor object=power channels=(1 3 5 )")
dss.text("Plot monitor object=power channels=(2 4 6 )")
