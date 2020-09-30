# Laboratório de Experimentação de Software

![java-vs-python](https://user-images.githubusercontent.com/34322384/94696600-9984af80-030d-11eb-8976-a2eaae081d3c.png)

**Aluno**: Lucas Branco Laborne Tavares  
**Professor**: Humberto Torres Marques Neto

## Introdução

O objetivo deste laboratório é analisar a qualidade de repositórios desenvolvidos na linguagem Python comparando-os com repositórios desenvolvidos na linguagem Java sob a perspectiva de características levantadas através de ferramentas como Radon, CodeFactor ou SonarQube.

## Metodologia

1. Escolher a ferramenta de análise estática de código Java e Python.  
Sugere-se avaliar o conteúdo do repositório  
https://github.com/analysis-tools-dev/static-analysis  

2. Com o objetivo de analisar repositórios relevantes, escritos nas linguagens estudadas (Python e Java), coletaremos, ou seja, faremos o clone, dos top-100 repositórios Python e dos top-100 repositórios Java mais populares do GitHub, para calcular cada uma das métricas definidas a seguir.  

3. Produzir um relatório comparando os repositórios mais populares das linguagens Python e Java de acordo com as métricas definidas.

## Questões de pesquisa
1. Quais as características dos top-100 repositórios Java mais populares?
2. Quais as características dos top-100 repositórios Python mais populares?
3. Repositórios Java e Python populares possuem características de "boa qualidade" semelhantes?
4. A popularidade influencia nas características dos repositórios Java e Python?

## Métricas
Utilizaremos como fatores de qualidade métricas associadas à quatro dimensões:  
**Popularidade**: Número de estrelas, número de watchers, número de forks dos repositórios coletados  
**Tamanho**: Linhas de código (LOC e SLOC) e linhas de comentários  
**Atividade**: Número de releases, frequência de publicação de releases (número de releases / dias)  
**Maturidade**: Idade (em anos) de cada repositório coletado  

## Relatório Final
Apresente uma extensão do comparativo dos repositórios Java e Python considerando as métricas:  
i. Complexidade ciclomática  
ii. Índice de manutenibilidade  
iii. Halstead  
Veja como referência como é feito pela ferramenta "radon" em https://radon.readthedocs.io/en/latest/intro.html

## Instruções
1. (Opcional) [Crie um ambiente virtual](https://docs.python.org/3/library/venv.html)  
2. Instale as dependências:  
```pip install -r requirements.txt```  
3. Execute o script para gerar os arquivos .csv:  
```python farmer.py```
4. Execute o script para analisar os dados e gerar o relatorio:  
```python relatorio.py```
