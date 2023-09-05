# -*- coding: utf-8 -*-
# @Time    : 9/5/2023 3:29 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Parte4-1.py
# @Software: PyCharm

import os
import pathlib
import pandas as pd

from compile_123bus_h import compile_123bus_h

dss = compile_123bus_h()
dss.text("Solve")

dss.text("set harmonics=[3]")
dss.text("set mode=harmonic")
dss.text("solve")

dss.text("export monitor power")
dss.text("export monitor V_I")


script_path = os.path.dirname(os.path.abspath(__file__))
m_power = pathlib.Path(script_path).joinpath("feeders", "123Bus", "ieee123_Mon_power_1.csv")
m_v_i = pathlib.Path(script_path).joinpath("feeders", "123Bus", "ieee123_Mon_v_i_1.csv")


p_df = pd.read_csv(m_power, index_col=0)
v_df = pd.read_csv(m_v_i, index_col=0)

i_a_1 = v_df.loc[60, " I1"]
i_a_3 = v_df.loc[180, " I1"]
i_b_1 = v_df.loc[60, " I2"]
i_b_3 = v_df.loc[180, " I2"]
i_c_1 = v_df.loc[60, " I3"]
i_c_3 = v_df.loc[180, " I3"]

dhi_a_3 = 100.0 * i_a_3 / i_a_1
dhi_b_3 = 100.0 * i_b_3 / i_b_1
dhi_c_3 = 100.0 * i_c_3 / i_c_1

dhi_3 = max(dhi_a_3, dhi_b_3, dhi_c_3)

v_a_1 = v_df.loc[60, " V1"]
v_a_3 = v_df.loc[180, " V1"]
v_b_1 = v_df.loc[60, " V2"]
v_b_3 = v_df.loc[180, " V2"]
v_c_1 = v_df.loc[60, " V3"]
v_c_3 = v_df.loc[180, " V3"]

dhv_a_3 = 100.0 * v_a_3 / v_a_1
dhv_b_3 = 100.0 * v_b_3 / v_b_1
dhv_c_3 = 100.0 * v_c_3 / v_c_1

dhv_3 = max(dhv_a_3, dhv_b_3, dhv_c_3)

print(f"DHV3 = {round(dhv_3, 2)} % e DHI3 = {round(dhi_3, 2)}")
