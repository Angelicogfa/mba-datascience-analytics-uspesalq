# HLM3 com Medidas Repetidas:

# ICCs (intraclasses correlations):
    
icc_escola = 180.222 / (180.222 + 325.798 + 41.6494)
icc_escola

icc_estudante = 325.798 / (180.222 + 325.798 + 41.6494)
icc_estudante

icc_temporal = 1 - icc_escola - icc_estudante
icc_temporal

#%%
modelo_completo_final_hlm3.fit()

# Fitted Completo:
40.032 + 5.168*1 + 14.702*0 + 1.179*2 -0.652*0*1 -0.057*2*1 \
    -8.671594 + 0.319517*1 -2.182141 -0.118656*1