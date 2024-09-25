# Calculo

z > 1.96 (95% de confiança ~5% Nível de significância)
v0j -> intercepto
v1j -> inclinação


## Modelo Nulo


## Modelo  com interceptos e inclinações aleatorias

intercepto -> gama_00
beta_i -> gama_01

## Modelo final com interceptos e inclunações aleatórias


y_pred = g_00 + g_01 * B_01 + g_10 * B_02 + g_11 * B_03 * B_01
y_pred_final = y_pred + v0j + v1j * B_01

## HLM 3

### Modelo nulo - Constructo do Modelo Nulo Multinível

Para um modelo nulo, a equação é simplificada para capturar apenas a variabilidade aleatória entre os grupos:

$$
\text{desempenho}_{ij} = \beta_0 + u_{0j} + v_{0ij} + \epsilon_{ij}
$$

Onde:

- $\text{desempenho}_{ij}$ é o resultado observado para o estudante $i$ na escola $j$.
- $\beta_0$ é o intercepto fixo global médio do modelo, representando a média geral dos desempenhos sem levar em conta outros preditores.
- $u_{0j}$ é o efeito aleatório do intercepto para a escola $j$, capturando a variação do desempenho entre as escolas.
- $v_{0ij}$ é o efeito aleatório do intercepto para o estudante $i$ dentro da escola $j$, capturando a variação adicional entre estudantes dentro das mesmas escolas.
- $\epsilon_{ij}$ é o termo de erro residual, capturando a variabilidade não explicada pelo modelo.

Este modelo nulo é útil para calcular a Intra-Class Correlation (ICC), que quantifica a proporção da variabilidade total que é atribuível aos agrupamentos de nível mais alto (neste caso, as escolas).

### Cálculo da Correlação Intra-Classe (ICC) para um Modelo Nulo

A ICC (Intraclass Correlation Coefficient) permite avaliar a proporção da variabilidade total dos dados que é atribuível aos diferentes níveis de agrupamento, como escolas, em um modelo multinível nulo.

### Fórmula da ICC

Para um modelo com dois níveis de agrupamento, como escolas (nível 2) e estudantes (nível 1), a ICC é calculada usando a seguinte fórmula:

$\text{ICC} = \frac{\sigma^2_{\text{entre-escolas}}}{\sigma^2_{\text{entre-escolas}} + \sigma^2_{\text{dentro-dos-estudantes}}}$

### Componentes da Fórmula

- $\sigma^2_{\text{entre-escolas}}$ representa a variância entre grupos de nível superior (escolas), o componente de variância $u_{0j}$.
- $\sigma^2_{\text{dentro-dos-estudantes}}$ é a variância residual dentro do mesmo grupo de nível inferior (estudantes na mesma escola), o componente de variância $\epsilon_{ij}$.

### Interpretação da ICC

- **ICC próximo a 1**: Indica que a maior parte da variância total no desempenho é devida a diferenças entre as escolas.
- **ICC próximo a 0**: Sugere que a variância total é principalmente devida a diferenças dentro das escolas, ou seja, entre estudantes da mesma escola.

A ICC ajuda a decidir se um modelo multinível é apropriado, demonstrando quanto da variação total dos dados é explicável pelo agrupamento em níveis mais elevados, como as escolas neste caso específico.


## Modelo Multinível

O modelo pode ser representado pela seguinte equação:

$$
\text{desempenho}_{ij} = (\beta_0 + u_{0j} + v_{0ij}) + (\beta_1 + u_{1j} + v_{1ij}) \times \text{mes}_{ij} + \beta_2 \times \text{ativ\_sim}_{ij} + \beta_3 \times \text{texp}_j + \beta_4 \times (\text{ativ\_sim}_{ij} \times \text{mes}_{ij}) + \beta_5 \times (\text{texp}_j \times \text{mes}_{ij}) + \epsilon_{ij}
$$

Onde:

- $\text{desempenho}_{ij}$ é o resultado para o estudante $i$ na escola $j$.
- $\beta_0$ é o intercepto fixo do modelo.
- $\beta_1$ a $\beta_5$ são os coeficientes de regressão para os efeitos fixos.
- $u_{0j}$ e $u_{1j}$ são os efeitos aleatórios associados à escola $j$ para o intercepto e a inclinação de $\text{mes}$, respectivamente.
- $v_{0ij}$ e $v_{1ij}$ são os efeitos aleatórios associados ao estudante $i$ dentro da escola $j$ para o intercepto e a inclinação de $\text{mes}$, respectivamente.
- $\epsilon_{ij}$ é o termo de erro residual.
- $\text{mes}_{ij}$, $\text{ativ\_sim}_{ij}$, e $\text{texp}_j$ são as variáveis preditoras para estudante $i$ na escola $j$.

## Fórmula de Predição do Modelo Multinível

A previsão do desempenho $\hat{y}_{ij}$ para um estudante $i$ na escola $j$ pode ser expressa pela seguinte fórmula:

$$
\hat{y}_{ij} = \beta_0 + \beta_1 \cdot \text{mes}_{ij} + \beta_2 \cdot \text{ativ\_sim}_{ij} + \beta_3 \cdot \text{texp}_j + \beta_4 \cdot ( \text{ativ\_sim}_{ij} \cdot \text{mes}_{ij} ) + \beta_5 \cdot ( \text{texp}_j \cdot \text{mes}_{ij} )
$$

Além dos efeitos fixos, incluem-se os efeitos aleatórios:

$$
+ u_{0j} + v_{0ij} + (u_{1j} + v_{1ij}) \cdot \text{mes}_{ij}
$$


Onde:

- $\hat{y}_{ij}$ é a predição para o estudante $i$ na escola $j$.
- $\beta_0$ a $\beta_5$ são os coeficientes fixos estimados pelo modelo.
- $u_{0j}$ e $v_{0ij}$ são os efeitos aleatórios no intercepto para a escola $j$ e o estudante $i$, respectivamente.
- $u_{1j}$ e $v_{1ij}$ são os efeitos aleatórios na inclinação de $\text{mes}$ para a escola $j$ e o estudante $i$, respectivamente.
- $\text{mes}_{ij}$, $\text{ativ\_sim}_{ij}$, e $\text{texp}_j$ são as variáveis preditoras, onde $\text{mes}_{ij}$ interage com os coeficientes aleatórios.

Esta fórmula combina os efeitos fixos e aleatórios para gerar uma predição de $\text{desempenho}$ específico para cada combinação de escola e estudante com suas respectivas características e interações temporais.