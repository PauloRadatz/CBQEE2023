# -*- coding: utf-8 -*-
# @Time    : 9/5/2023 3:32 PM
# @Author  : Paulo Radatz
# @Email   : pradatz@epri.com
# @File    : Parte4-2.py
# @Software: PyCharm

import os
import pathlib
import pandas as pd
import numpy as np

from compile_123bus_h import compile_123bus_h

dss = compile_123bus_h()
dss.text("Solve")

dss.text("set mode=harmonic")
dss.text("solve")

dss.text("export monitor power")
dss.text("export monitor V_I")


script_path = os.path.dirname(os.path.abspath(__file__))
m_power = pathlib.Path(script_path).joinpath("feeders", "123Bus", "ieee123_Mon_power_1.csv")
m_v_i = pathlib.Path(script_path).joinpath("feeders", "123Bus", "ieee123_Mon_v_i_1.csv")


p_df = pd.read_csv(m_power, index_col=0)
v_df = pd.read_csv(m_v_i, index_col=0)

v_df_h = v_df.drop(60)
sum_vn_a_2 = (v_df_h[" V1"] ** 2).sum()
sum_vn_b_2 = (v_df_h[" V2"] ** 2).sum()
sum_vn_c_2 = (v_df_h[" V3"] ** 2).sum()

dhv_a_t = 100 * np.sqrt(sum_vn_a_2 / v_df.loc[60, " V1"] ** 2)
dhv_b_t = 100 * np.sqrt(sum_vn_b_2 / v_df.loc[60, " V2"] ** 2)
dhv_c_t = 100 * np.sqrt(sum_vn_c_2 / v_df.loc[60, " V3"] ** 2)

dhv_t = max(dhv_a_t, dhv_b_t, dhv_c_t)

print(f"DHVt = {round(dhv_t, 2)} %")