O modelo Zero Inflated Poisson e Zero Inflated Negative BenomialP não possuem uma função step wise, então o parametro `exig_infl` necessita ser obtido utilizando teste de força ou rodando um step_wise com um modelo logit na qual a caracteristica que identifica a relação poderá ser utilizada como variavel exogena

Poisson

$exp^(a + B_1 * X_1 + B_2 * X_2 + B_n + X_n)$