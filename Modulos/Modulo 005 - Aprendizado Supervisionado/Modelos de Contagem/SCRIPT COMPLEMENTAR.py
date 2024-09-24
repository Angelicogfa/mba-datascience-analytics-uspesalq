# Modo direto de estimação do modelo binomial negativo:
    
modelo_bneg_direto = sm.NegativeBinomial.from_formula('violations ~ staff + post + corruption',
                                                      data=df_corruption).fit()

modelo_bneg_direto.summary()

#%%
# Teste de razão de verossimilhança
-2*(-2071.79 - (-567.401))

#%%
# Cálculo manual do fit do 'modelo_bneg' antes da vigência da lei

modelo_bneg.params

np.exp(1.946890 - 4.274634*0 + 0.040018*23 + 0.452654*0.5)

#%%
# Modo direto de estimação do modelo binomial negativo 2:
    
modelo_bneg_direto2 = sm.NegativeBinomial.from_formula('violations ~ staff + post + corruption',
                                                      data=df_corruption2).fit()

modelo_bneg_direto2.summary()


#%%
modelo_zip.params

# Cálculo manual do fit do 'modelo_zip' antes da vigência da lei
# igual à lousinha

(1 - (1/(1 + np.exp(-(-1.611649 - 0.952315*0.5)))))*\
    (np.exp(2.488877 + 0.020020*23 + 0.093722*0.5 - 4.287916*0))

#%%
modelo_zinb.params

# Cálculo manual do fit do 'modelo_zinb' antes da vigência da lei

(1 - (1/(1 + np.exp(-(-17.985682 - 8.110426*0.5)))))*\
    (np.exp(2.032397 + 0.041076*23 + 0.181459*0.5 - 4.263797*0))

#%%
# Comparação com modelos estimados por OLS

modelo_linear = sm.OLS.from_formula('violations ~ staff + post + corruption',
                                    df_corruption).fit()

modelo_linear.summary()
modelo_linear.llf

# Teste de Shapiro-Francia nos resíduos do 'modelo_linear'
from statstests.tests import shapiro_francia

shapiro_francia(modelo_linear.resid)

# Transformação de Box-Cox na variável 'violations'
from scipy.stats import boxcox

yast, lmbda = boxcox(df_corruption['violations'])

df_corruption['violations'].describe()

df_corruption['violations1'] = df_corruption['violations'] + 0.001

df_corruption['violations1'].describe()

yast, lmbda = boxcox(df_corruption['violations1'])

df_corruption['bc_violations'] = yast

df_corruption

# Estimar o novo modelo OLS com a trasnformação de Box-Cox

modelo_bc = sm.OLS.from_formula('bc_violations ~ staff + post + corruption',
                                    df_corruption).fit()

modelo_bc.summary()
modelo_bc.llf

shapiro_francia(modelo_bc.resid)

# In[FINAL]: Gráfico para a comparação dos LogLiks dos modelos Poisson,
#binomial negativo, ZIP, ZINB, OLS e OLS com Box-Cox

# Definição do dataframe com os modelos e respectivos LogLiks
df_llf = pd.DataFrame({'modelo':['Poisson','ZIP','BNeg','ZINB',
                                 'OLS Linear','OLS Box-Cox'],
                      'loglik':[modelo_poisson.llf,
                                modelo_zip.llf,
                                modelo_bneg.llf,
                                modelo_zinb.llf,
                                modelo_linear.llf,
                                modelo_bc.llf]})
df_llf

# Plotagem propriamente dita
fig, ax = plt.subplots(figsize=(15,10))

c = ['indigo', 'deeppink', 'darkgoldenrod', 'darkorange',
     'darkgreen','limegreen']

ax1 = ax.barh(df_llf.modelo,df_llf.loglik, color = c)
ax.bar_label(ax1, label_type='center', color='white', fontsize=30)
ax.set_ylabel("Modelo Proposto", fontsize=20)
ax.set_xlabel("LogLik", fontsize=20)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=20)
plt.show()
