**Dados fornecidos:**

- **Nome do arquivo CSV**: miro_dados_limpos_desde_janeiro.csv
- **Colunas do dataset**:

  - 'Nome do anúncio'
  - 'Alcance'
  - 'Impressões'
  - 'Frequência'
  - 'Valor usado (BRL)'
  - 'Configuração de atribuição'
  - 'Tipo de resultado'
  - 'Resultados'
  - 'Custo por resultado'
  - 'CPM (custo por 1.000 impressões)'
  - 'CTR (todos)'
  - 'Classificação de qualidade'
  - 'Classificação da taxa de engajamento'
  - 'Conversas por mensagem iniciadas'
  - 'Custo por conversa por mensagem iniciada'
  - 'CPC (custo por clique no link)'
  - 'Cliques (todos)'
  - 'Engajamento com a Página'
  - 'Reproduções de 25% do vídeo'
  - 'Reproduções de 50% do vídeo'
  - 'Reproduções de 75% do vídeo'
  - 'Reproduções de 95% do vídeo'
  - 'Reproduções de 100% do vídeo'
  - 'Início dos relatórios'
  - 'Término dos relatórios'
  - 'Data de criação'

**Informações adicionais sobre métricas:**

- **Alcance**: Número de contas únicas que viram seus anúncios pelo menos uma vez. Esta métrica é estimada e pode ser afetada por lance, orçamento e público-alvo.

- **Impressões**: Número de vezes que seus anúncios foram exibidos na tela. Contabiliza cada vez que um anúncio aparece na tela pela primeira vez.

- **Frequência**: Média de vezes que seu anúncio foi visualizado pela mesma conta. Calculada dividindo impressões por alcance.

- **Resultados**: Número de vezes que seu anúncio atingiu um resultado, com base no objetivo e nas configurações selecionadas. Pode incluir modelagem estatística para contabilizar alguns resultados.

- **CTR (todos)**: Porcentagem de impressões que resultaram em um clique (todos) em relação ao número total de impressões. Calculada como cliques (todos) divididos por impressões.

- **Engajamento com a Página**: Número de ações realizadas em sua Página do Facebook ou perfil do Instagram atribuídas aos seus anúncios. Inclui seguidores, curtidas, check-ins, reações a publicações e cliques em links.

**Objetivos da análise:**

1. **Avaliar o desempenho dos anúncios**: Utilizar as métricas fornecidas para entender quais anúncios estão performando bem ou mal.
2. **Justificar o desempenho**: Identificar fatores que contribuem para o sucesso ou falha dos anúncios, analisando correlações entre métricas.
3. **Decisão sobre reativação ou criação de novos criativos**: Baseado na análise, determinar se é viável reativar anúncios pausados ou se é melhor desenvolver novos criativos.
4. **Foco para novos criativos**: Se novos criativos forem necessários, identificar quais áreas ou métricas devem ser priorizadas para melhorar o desempenho (por exemplo, aumentar o CTR, melhorar o engajamento, etc.).

**Requisitos para o código em Python:**

- **Importação de bibliotecas**: Utilizar bibliotecas como pandas, numpy, matplotlib, seaborn, etc.
- **Leitura e pré-processamento dos dados**:
  - Carregar o arquivo CSV.
  - Tratar valores ausentes ou inconsistentes.
  - Converter tipos de dados quando necessário.
- **Análise exploratória de dados (EDA)**:
  - Estatísticas descritivas das métricas principais.
  - Visualizações gráficas (histogramas, boxplots, scatter plots) para entender a distribuição e relações entre as métricas.
- **Análise de correlação**:
  - Calcular a matriz de correlação entre as métricas.
  - Identificar métricas que têm forte correlação com o desempenho dos anúncios.
- **Insights e conclusões**:
  - Interpretar os resultados da análise.
  - Fornecer recomendações baseadas nos dados.
- **Documentação**:
  - Comentar o código para explicar cada etapa.
  - Incluir títulos e rótulos nos gráficos.
  - Apresentar um resumo final com os principais achados.

**Considerações adicionais:**

- **Focar na qualidade dos dados**: Garantir que os dados utilizados são confiáveis para evitar conclusões errôneas.
- **Interpretar métricas corretamente**: Utilizar as definições fornecidas para entender o que cada métrica representa e como influencia o desempenho.
- **Pensar estrategicamente**: Além da análise técnica, considerar aspectos de marketing e comportamento do usuário que podem afetar os resultados.