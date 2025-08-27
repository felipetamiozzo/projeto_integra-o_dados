# Projeto de Integração de Dados - BeeCorp

## Visão Geral do Projeto
Este projeto tem como objetivo unificar e padronizar as bases de dados de clientes da BeeCorp, que atualmente estão dispersas e com nomenclaturas inconsistentes. A solução permitirá análises financeiras mais precisas e a geração de relatórios de DRE (Demonstração do Resultado do Exercício) de forma mais ágil.

## Estrutura do Projeto

├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── requirements.txt    # Dependências do projeto (bibliotecas Python)
├── README.md           # Visão geral e instruções do projeto
├── /data               # Pasta para dados confidenciais (IGNORADA PELO GIT)
│   ├── raw             # Dados brutos da empresa
│   └── processed       # Dados tratados e unificados
├── /docs               # Documentos e relatórios
├── /src                # Código-fonte
└── /venv               # Ambiente virtual

## Como Começar (para novos membros do grupo)

1.  **Clone o Repositório:**
    Abra o terminal e clone este repositório para sua máquina local:
    `git clone <URL do seu repositório>`

2.  **Crie e Ative o Ambiente Virtual:**
    Navegue até a pasta do projeto e crie o ambiente virtual:
    `python -m venv venv`

    Ative o ambiente:
    * **Windows (PowerShell):** `.\venv\Scripts\activate`
    * **Windows (Git Bash):** `source venv/Scripts/activate`
    * **macOS/Linux:** `source venv/bin/activate`

3.  **Adicione os Dados Brutos:**
    Peça os dados à pessoa responsável. Os arquivos `.csv` (recebidos da BeeCorp) devem ser colocados na pasta `data/raw`.

4.  **Instale as Dependências:**
    Com o ambiente virtual ativado, instale todas as bibliotecas necessárias:
    `pip install -r requirements.txt`

## Fluxo de Trabalho e Contribuição
-   Utilize a metodologia **CRISP-DM** para guiar o desenvolvimento.
-   Antes de começar a trabalhar, crie uma **branch** específica para a sua tarefa: `git checkout -b nome-da-sua-branch`.
-   Após finalizar sua parte, faça o `commit` das mudanças e envie para o repositório: `git push origin nome-da-sua-branch`.
-   Abra um **Pull Request (PR)** para que seu código seja revisado e, depois, integrado à `main branch`.
