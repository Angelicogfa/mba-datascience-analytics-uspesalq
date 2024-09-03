## Modelo Determinístico

**Definição**: Um modelo determinístico é aquele em que os resultados são completamente determinados pelas condições iniciais e pelos parâmetros do modelo. Não há variabilidade ou incerteza nos resultados. Os erros são obtidos a posteriori.
> Características:
* **Previsibilidade**: Dado um conjunto de condições iniciais, o modelo sempre produzirá o mesmo resultado.
* **Exemplo**: A equação da trajetória de um projétil sob a influência da gravidade, sem considerar a resistência do ar, é um modelo determinístico.


## Modelos Estocásticos

**Definição**: Um modelo estocástico incorpora elementos de aleatoriedade e incerteza. Os resultados podem variar mesmo com as mesmas condições iniciais, devido à presença de variáveis aleatórias.
> Características:
* **Variabilidade**: Os resultados podem diferir em diferentes execuções do modelo, mesmo com as mesmas condições iniciais.
* **Exemplo**: A previsão do tempo é um modelo estocástico, pois incorpora a incerteza e a variabilidade inerentes aos sistemas climáticos.

## Calculo para box-cox

y_box_cox = (y ^ lambda - 1) / lambda

y_box_cox_i  = alpha + beta_i * X_i + u_i

y_hat_i = alpha + beta_i * X_i

y_norm = (y_hat * lambda - 1) ^ (1 / lambda)