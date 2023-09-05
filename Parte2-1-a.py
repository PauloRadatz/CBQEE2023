# -*- coding: utf-8 -*-
# @Time    : 9/16/2022 4:00 PM
# @Author  : Paulo Radatz

# @File    : Parte2-1-a.py
# @Software: PyCharm

from compile_123bus import compile_123bus

# Duração Relativa da Transgressão de Tensão Precária – DRP, e a Duração Relativa da Transgressão de Tensão Crítica – DRC,
number = 1008

v_pre_max = 1.05
v_cri_max = 1.1
v_pre_min = 0.95
v_cri_min = 0.9

dss = compile_123bus()

dss.text("batchedit regcontrol..* enabled=No")

dss.text(f"batchedit load..* daily=default")
dss.text("New Monitor.power element=Line.L115 terminal=1 mode=1 ppolar=NO")
dss.text("New Monitor.v_95 element=LINE.L94 terminal=2 mode=0")
dss.text("New Monitor.v_95_rec element=LINE.L94 terminal=2 mode=0 vipolar=no")

dss.text("set mode=daily")
dss.text("set stepsize=10m")
dss.text(f"set number={number}") # 10min x 1008 = 7 dias
dss.text("solve")

dss.text("Export monitors v_95")
dss.text("Plot monitor object=v_95 channels=(1 3 5 ) base=[2401.7 2401.7 2401.7]")

dss.monitors.name = "v_95_rec"

va_real = dss.monitors.channel(1)
va_imag = dss.monitors.channel(2)
vb_real = dss.monitors.channel(3)
vb_imag = dss.monitors.channel(4)
vc_real = dss.monitors.channel(5)
vc_imag = dss.monitors.channel(6)

nlp = 0
nlc = 0
for i in range(number):
    vab = abs((va_real[i] - vb_real[i]) + 1j * (va_imag[i] - vb_imag[i])) / 4160.0
    vbc = abs((vb_real[i] - vc_real[i]) + 1j * (vb_imag[i] - vc_imag[i])) / 4160.0
    vca = abs((vc_real[i] - va_real[i]) + 1j * (vc_imag[i] - va_imag[i])) / 4160.0

    v_min = min(vab, vbc, vca)
    v_max = max(vab, vbc, vca)

    if v_cri_min < v_min < v_pre_min or v_pre_max < v_max < v_cri_max:
        nlp = nlp + 1
    elif v_min < v_cri_min or v_max > v_cri_max:
        nlc = nlc + 1


DRP = nlp / number * 100
DRC = nlc / number * 100

print(f"DRP = {round(DRP, 2)} %")
print(f"DRC = {round(DRC, 2)} %")