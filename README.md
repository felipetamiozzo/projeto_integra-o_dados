
# Projeto de Integração e Análise de Dados 

## 📜 Visão Geral do Projeto

Este projeto, desenvolvido como parte de um desafio prático, tem o objetivo de resolver um problema real da **confidencial**: a inconsistência e a falta de padronização nos dados de clientes.

Meu trabalho consistiu em unificar múltiplas bases de dados (`Operacoes`, `Departamento_Pessoal`, `Profissional_Ponta`, e `Recrutamento_Selecao`) utilizando uma base de referência (`Base_Referencia`). A solução foi construída em Python, aplicando técnicas de tratamento de dados (`Data Wrangling`) e **clusterização** para criar uma base de dados única e padronizada.

O resultado final é uma base de dados limpa e pronta para análises financeiras, permitindo à BeeCorp gerar relatórios de desempenho por cliente de forma mais eficiente e automatizada.

## ⚙️ Ferramentas e Metodologia

  * **Linguagem:** Python
  * **Bibliotecas Principais:**
      * `pandas`: Para a manipulação e análise dos dados.
      * `fuzzywuzzy` e `python-levenshtein`: Para a clusterização e busca de nomes de clientes similares.
      * `jupyter`: Para a prototipagem e exploração do código.
  * **Controle de Versão:** Git
  * **Metodologia:** O projeto seguiu as etapas do modelo **CRISP-DM**, garantindo um fluxo de trabalho estruturado, desde o entendimento do negócio até a implantação da solução.

## 📂 Estrutura do Repositório

Organizei o projeto em uma estrutura lógica para facilitar a navegação e a colaboração. As bases de dados originais e processadas estão fora do repositório público por questões de **confidencialidade**.

```
├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo de documentação
├── /data/              # **Pasta local para os dados confidenciais**
│   ├── raw/            # As bases de dados originais (fora do GitHub)
│   └── processed/      # A base de dados unificada final (fora do GitHub)
├── /docs/              # Documentos e relatórios do projeto
├── /src/               # Código-fonte
│   ├── analise_limpeza.ipynb # Notebook Jupyter com o processo de ETL e clusterização
│   └── main.py         # Script Python final, após o refinamento do notebook
└── /venv/              # Ambiente virtual do Python (fora do GitHub)
```

## 🚀 Como Executar o Projeto

Para replicar meu ambiente e executar o código, siga estas instruções:

1.  **Clone este repositório:**

    ```bash
    git clone https://github.com/felipetamiozzo/projeto_integra-o_dados
    cd seu-repositorio
    ```

2.  **Crie e Ative o Ambiente Virtual:**

    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa o ambiente (Windows - Git Bash)
    source venv/Scripts/activate

    # Ativa o ambiente (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Adicione os Dados Brutos:**

      * Solicite as bases de dados originais (`.csv`) e coloque-as na pasta `data/raw/`.

4.  **Instale as Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute o Código:**

      * Abra o notebook `src/analise_limpeza.ipynb` no VS Code e execute as células para ver o processo passo a passo.
      * Para rodar o script final, use o terminal com o ambiente virtual ativado:
        ```bash
        python src/main.py
        ```

## 📈 Conclusão e Próximos Passos

A solução desenvolvida resultou em uma base de dados robusta e confiável. Com essa nova estrutura, a equipe financeira da BeeCorp pode agora gerar relatórios de DRE com maior precisão e agilidade.

Acredito que os próximos passos podem incluir a criação de um painel de BI (Business Intelligence) interativo e a automação do processo de atualização dos dados em uma plataforma de nuvem.

-----

**Autor:** [Felipe Tamiozzo Silveira]