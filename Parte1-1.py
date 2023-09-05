# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 12:26 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Y.py
# @Software: PyCharm

from compile_123bus import compile_123bus

dss = compile_123bus()

dss.text("ClearBusMarkers")
dss.text(f"set markcapacitor=yes")
dss.text(f"set markregulators=yes")
dss.text("plot circuit Power max=2000 n n C1=$00FF0000")