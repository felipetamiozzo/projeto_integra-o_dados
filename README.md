
# Projeto de Padronização de Dados

## 📜 Visão Geral do Projeto

Este projeto, desenvolvido como parte de um desafio prático, tem o objetivo de resolver um problema real do **`'nome confidencial'`**: a inconsistência e a falta de padronização nos dados de clientes e serviços.

Nosso trabalho consistiu em unificar múltiplas bases de dados (oriundas das abas `Operacoes`, `Departamento_Pessoal`, `Profissional_Ponta`, e `Recrutamento_Selecao`) de um **único arquivo Excel**. A solução foi construída em Python, aplicando técnicas de **padronização de dados** e **fuzzy matching** para criar uma base de dados única e padronizada.

O resultado final é uma base de dados limpa e pronta para análises, permitindo ao `'nome confidencial'` gerar relatórios de desempenho por cliente de forma mais eficiente e automatizada.

## ⚙️ Ferramentas e Metodologia

  * **Linguagem:** Python
  * **Bibliotecas Principais:**
      * `pandas`: Para a manipulação e análise dos dados.
      * `fuzzywuzzy` e `python-levenshtein`: Para o **fuzzy matching** e a busca de nomes de clientes similares.
      * `openpyxl`: Para ler e escrever arquivos no formato Excel (`.xlsx`).
  * **Controle de Versão:** Git
  * **Metodologia:** O projeto seguiu uma abordagem estruturada, focando em:
    1.  **Entendimento dos dados** e das regras de negócio.
    2.  **Desenvolvimento de um script robusto** que lida com diferentes tipos de dados e inconsistências.
    3.  **Padronização e unificação** de todas as bases em um único arquivo de saída.

## 📂 Estrutura do Repositório

Organizei o projeto em uma estrutura lógica para facilitar a navegação e a colaboração. As bases de dados originais e processadas estão fora do repositório público por questões de confidencialidade.

```
├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo de documentação
├── /data/              # **Pasta local para os dados confidenciais**
│   ├── raw/            # A base de dados original (.xlsx)
│   └── processed/      # A base de dados unificada final (.xlsx)
├── /src/               # Código-fonte
│   └── processar_dados.py  # Script Python com todo o fluxo de padronização
└── /venv/              # Ambiente virtual do Python (fora do GitHub)
```

**Nota:** O arquivo original `Base de Dados Clientes.xlsx` deve ser colocado na pasta `data/raw/` para que o script funcione.

## 🚀 Como Executar o Projeto

Para replicar meu ambiente e executar o código, siga estas instruções:

1.  **Clone este repositório:**

    ```bash
    git clone https://github.com/felipetamiozzo/projeto_integra-o_dados
    cd projeto_integra-o_dados
    ```

2.  **Crie e Ative o Ambiente Virtual:**

    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa o ambiente (Windows - Git Bash)
    source venv/Scripts/activate
    ```

3.  **Adicione os Dados Brutos:**

      * Coloque o arquivo `Base de Dados Clientes.xlsx` na pasta `data/raw/`.

4.  **Instale as Dependências:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute o Código:**

      * Use o terminal com o ambiente virtual ativado:

    <!-- end list -->

    ```bash
    python src/processar_dados.py
    ```

## 📈 Conclusão e Próximos Passos

A solução desenvolvida resultou em uma base de dados robusta e confiável. Com essa nova estrutura, a equipe financeira do `'nome confidencial'` pode agora gerar relatórios com maior precisão e agilidade.

Acredito que os próximos passos podem incluir a criação de um painel de BI (Business Intelligence) interativo e a automação do processo de atualização dos dados em uma plataforma de nuvem.

-----

**Autor:** [Felipe Tamiozzo Silveira]