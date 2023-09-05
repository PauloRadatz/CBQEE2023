# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 3:19 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Parte1-3-b.py
# @Software: PyCharm

from compile_123bus import compile_123bus

dss = compile_123bus()

dss.text("batchedit regcontrol..* enabled=No")

dss.text(f"batchedit load..* daily=default")
dss.text("New Monitor.power element=Line.L115 terminal=1 mode=1 ppolar=NO")
dss.text("New Monitor.v_95 element=LINE.L94 terminal=2 mode=0")

dss.text("set mode=daily")
dss.text("solve")

dss.text("Plot monitor object=v_95 channels=(1 3 5 ) base=[2401.7 2401.7 2401.7]")
