# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 1:31 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : compile_123bus.py
# @Software: PyCharm

import os
import pathlib

import py_dss_interface

script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("feeders", "123Bus", "IEEE123Master.dss")


def compile_123bus():
    dss = py_dss_interface.DSS()
    dss.text(f"compile [{dss_file}]")
    dss.text(f"New EnergyMeter.Feeder Line.L115 1")
    dss.text(f"Buscoords Buscoords.dat")

    return dss


