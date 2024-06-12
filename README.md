# DioAdventureWorks
Este repositório inclui todos os arquivos necessários para a criação de uma aplicativo Streamlit.

## Análise de Vendas da Adventure Works: Dashboard Interativo com Streamlit 🚲

### Descrição do Projeto

Este projeto tem como objetivo analisar dados de vendas da empresa fictícia Adventure Works e apresentar insights valiosos por meio de um dashboard interativo construído com Streamlit. 

O dashboard permite explorar as vendas, a lucratividade, o desempenho por produto, a performance das lojas e o comportamento dos clientes. Com visualizações claras e filtros interativos, a ferramenta facilita a compreensão do negócio e auxilia na tomada de decisões estratégicas.

**Acesse o aplicativo online:** [[dioadventureworks.meuaplicativo](https://dioadventureworks.streamlit.app/)]

### Funcionalidades

- **Visualização da Receita e Lucro Mensal:** Gráficos de linhas que mostram a evolução das vendas e lucros ao longo dos meses.
- **Análise dos Produtos Mais Vendidos:** Gráfico de barras com o Top 10 produtos por receita, permitindo identificar os itens mais importantes para o negócio.
- **Detalhes do Desempenho de Cada Produto:** Tabela interativa com informações sobre receita, lucro e quantidade vendida por produto.
- **Comparativo de Receita entre Lojas:** Gráfico de pizza que destaca a contribuição de cada loja para a receita total.
- **Identificação dos Clientes Mais Relevantes:** Gráfico de barras verticais que mostra os 10 clientes com maior receita.
- **Filtros Interativos:**  Permite filtrar os dados por ano e por produto, tornando a análise mais granular e focada.

### Como Executar o Projeto

1. **Requisitos:** Python 3.7 ou superior instalado.
2. **Ambiente Virtual:**  Crie um ambiente virtual para isolar as dependências do projeto: `python -m venv .venv`
3. **Ativando o Ambiente:** `source .venv/bin/activate` (Linux/macOS) ou `.venv\Scripts\activate` (Windows)
4. **Instalando as Bibliotecas:** `pip install -r requirements.txt` (crie um arquivo `requirements.txt` com as bibliotecas: `pandas`, `streamlit`, `plotly`)
5. **Executando o Aplicativo:**  `streamlit run seu_script.py` (substitua `seu_script.py` pelo nome do seu arquivo Python)

### Desafios Encontrados

- **Escolha das Visualizações Mais Adequadas:**  Definir os tipos de gráficos mais eficientes para representar cada tipo de dado e insight.
- **Organização do Layout do Dashboard:**  Criar um layout intuitivo e visualmente agradável para o usuário.
- **Otimização do Desempenho:** Garantir que o aplicativo carregue e processe os dados de forma rápida e eficiente.

### Soluções Adotadas

- **Exploração de Diferentes Gráficos:**  Experimentamos diversos tipos de gráficos (barras, linhas, pizza, boxplot) e escolhemos os mais adequados para cada análise.
- **Uso de `st.columns()`:**  Utilizamos a função `st.columns()` do Streamlit para organizar o layout do dashboard de forma mais flexível e responsiva.
- **Filtros Interativos:** Implementamos filtros para permitir que o usuário personalize a análise e explore os dados em diferentes níveis de detalhe.

### Lições Aprendidas e Próximos Passos

- **Importância da Visualização de Dados:**  Um bom dashboard faz a diferença na comunicação de insights e na tomada de decisão.
- **Flexibilidade do Streamlit:** O Streamlit é uma ferramenta poderosa e fácil de usar para criar dashboards interativos.
- **Próximos Passos:** 
    - Adicionar mais funcionalidades ao dashboard, como análise de tendências e previsões de vendas.
    - Explorar outras bibliotecas de visualização, como o Seaborn e o Plotly, para criar gráficos mais avançados.

### Captura de Telas

**Tela Principal:**

![capturaTela001](https://github.com/enps2015/DioAdventureWorks/assets/84017071/bb9be90c-53f5-426c-8670-c6a515a4bd58)

![capturaTela002](https://github.com/enps2015/DioAdventureWorks/assets/84017071/98551077-6417-4aab-b6f4-8ca4d9fbe3d3)

![capturaTela003](https://github.com/enps2015/DioAdventureWorks/assets/84017071/d7c551ba-14da-472b-a991-244a3a77230e)

![capturaTela004](https://github.com/enps2015/DioAdventureWorks/assets/84017071/39daa91d-154c-4ae6-8010-f5747d23949a)

![capturaTela005](https://github.com/enps2015/DioAdventureWorks/assets/84017071/ed3fe239-4373-4ea8-9dcf-bc112d249b41)

https://github.com/enps2015/DioAdventureWorks/assets/84017071/27408f77-5b45-4840-abcc-9305243142d2



