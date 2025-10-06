
## 🎯 Objetivo do Projeto

O principal objetivo deste projeto é automatizar a limpeza, padronização e unificação de múltiplas bases de dados de clientes, que originalmente se encontram em abas separadas dentro de um único arquivo Excel (`Base de Dados Clientes.xlsx`).

O script realiza dois processos de padronização principais:
1.  **Padronização de Clientes**: Utilizando uma base de referência (`Base_Referencia`), o script identifica e padroniza os nomes de clientes com base na similaridade de texto (Fuzzy Matching). Ao encontrar uma correspondência, atribui um `ID` único, a `Razão Social` e o `Grupo Econômico` corretos.
2.  **Padronização de Serviços**: Utilizando uma base de mapeamento (`Fases`), o script classifica e categoriza os serviços listados em cada registro.

Ao final, todos os dados tratados são consolidados em um único arquivo Excel, pronto para análise.

## ✨ Funcionalidades Principais

-   **Leitura de Múltiplas Abas**: Carrega e processa dinamicamente todas as abas de dados de um arquivo Excel.
-   **Limpeza de Dados**: Realiza a limpeza de nomes de clientes e serviços, convertendo para maiúsculas e removendo caracteres especiais.
-   **Fuzzy Matching para Clientes**: Utiliza a biblioteca `fuzzywuzzy` para encontrar a correspondência mais provável de nomes de clientes, mesmo que não sejam idênticos.
-   **Mapeamento de Categorias**: Converte descrições de serviços em categorias padronizadas.
-   **Unificação de Dados**: Consolida todos os dados processados em um único DataFrame e o salva como um novo arquivo Excel.
-   **Tratamento de Erros**: Inclui tratamento básico de exceções para erros como arquivo não encontrado.

## 📁 Estrutura do Projeto

Para que o script funcione corretamente, os arquivos e pastas devem seguir a estrutura abaixo:

```
PROJETO/
│
├── Data/Data
│   ├── Raw/
│   │   └── Base de Dados Clientes.xlsx  <
│   └── Processed/
│       └── base_unificada_clientes.xlsx  
│
├── src/
│   └── analise_limpeza.py                
│
└── README.md 
└── requirements.txt
                       
```

## 🛠️ Pré-requisitos

Antes de executar, certifique-se de que você tem o Python 3.7+ instalado. Você também precisará instalar as bibliotecas listadas abaixo.

-   `pandas`
-   `openpyxl` (necessário para o pandas ler e escrever arquivos `.xlsx`)
-   `fuzzywuzzy`
-   `python-levenshtein` (opcional, mas acelera muito a `fuzzywuzzy`)

## ⚙️ Instalação e Configuração

1.  **Clone este repositório** (ou simplesmente crie a estrutura de pastas acima).

2.  **Crie um ambiente virtual** (recomendado para isolar as dependências do projeto):
    ```bash
    python -m venv .venv
    ```

3.  **Ative o ambiente virtual:**
    -   No Windows:
        ```bash
        .\.venv\Scripts\activate
        ```
    -   No macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

4.  **Instale as bibliotecas necessárias:**
    ```bash
    pip install pandas openpyxl fuzzywuzzy python-levenshtein
    ```

## 🚀 Como Usar

1.  **Prepare o arquivo de entrada**:
    -   Coloque seu arquivo Excel na pasta `Data/Raw/` e certifique-se de que ele se chama `Base de Dados Clientes.xlsx`.
    -   O arquivo deve conter as abas de controle `Base_Referencia` e `Fases`, além das abas com os dados dos clientes.
    -   As abas de dados devem conter as colunas `Nome do Cliente` e `Fase 2`.

2.  **Execute o script**:
    -   Abra o terminal (com o ambiente virtual ativado) e navegue até a pasta raiz do projeto.
    -   Execute o comando:
      ```bash
      python src/seu_script.py
      ```

3.  **Verifique a saída**:
    -   O terminal exibirá o progresso do processamento de cada aba.
    -   Ao final, o arquivo `base_padronizada_final.xlsx` será criado na pasta `Data/Processed/`.

## 🧠 Detalhes do Processamento

### Padronização de Clientes
A função `padronizar_clientes` compara o nome de cada cliente (após limpeza) com a lista de `Razão Social` na `Base_Referencia`. Se a pontuação de similaridade (`fuzz.ratio`) for **igual ou superior a 85%**, o cliente é considerado uma correspondência e seus dados (`ID`, `Razão Social`, `Grupo Econômico`) são padronizados.

---