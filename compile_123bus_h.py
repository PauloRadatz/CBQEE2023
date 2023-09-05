# -*- coding: utf-8 -*-
# @Time    : 10/1/2022 6:32 PM
# @Author  : Paulo Radatz

# @File    : compile_123bus_h.py
# @Software: PyCharm

import os
import pathlib

import py_dss_interface

script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")

def compile_123bus_h():
    dss = py_dss_interface.DSS()
    dss.text(f"set DefaultBaseFrequency=60")
    dss.text(f"compile [{dss_file}]")


    dss.text(f"New EnergyMeter.Feeder Line.L115 1")
    dss.text(f"Buscoords Buscoords.dat")
    dss.text(f"set maxiteration=100")

    dss.text(f"New monitor.Power load.S48 mode=1 ppolar=no")
    dss.text(f"New monitor.V_I load.S48 mode=0")

    return dss