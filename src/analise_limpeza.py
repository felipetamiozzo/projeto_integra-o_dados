
# ### Objetivo do Projeto
# O principal objetivo deste projeto foi automatizar a padronização de múltiplas bases de dados de clientes, que estavam em abas diferentes dentro de um único arquivo Excel. O processo de limpeza e unificação foi focado em dois aspectos principais:
# 
# •	Padronização de Clientes: Utilizando uma base de referência (Base_Referencia), o script identifica e padroniza os nomes de clientes, atribuindo um ID único, a Razão Social e o Grupo Econômico corretos.
# 
# 


#Bibliotecas
import pandas as pd
import os
import re
from fuzzywuzzy import fuzz

# %%
#Caminho para a pasta de dados brutos
caminho_dados_brutos = 'Data/Data/Raw/'
nome_arquivo = 'Base de Dados Clientes.xlsx'
caminho_completo = os.path.join(caminho_dados_brutos, nome_arquivo)

# %%
#Função para padronizar os clientes
# Esta função faz a busca por similaridade (fuzzy matching)
def padronizar_clientes(df, df_referencia):
    """
    Usa Fuzzy Matching para encontrar a correspondência mais próxima
    dos nomes de clientes na base de referência e adiciona colunas padronizadas.
    """
    
    df['ID_Padronizado'] = None
    df['Razao_Social_Padronizada'] = None
    df['Grupo_Economico_Padronizado'] = None
    
    # Itera sobre cada linha do DataFrame principal (df)
    for index, row in df.iterrows():
        nome_cliente_tratado = row['Nome_Cliente_Tratado']
        melhor_match = None
        melhor_score = 0
        
        # Procura o melhor match na base de referência
        for ref_nome in df_referencia['Razão Social']:
            score = fuzz.ratio(nome_cliente_tratado, ref_nome)
            if score > melhor_score:
                melhor_score = score
                melhor_match = ref_nome
        
        # Se a similaridade for alta (>= 85), padroniza
        if melhor_score >= 85:
            match_info = df_referencia[df_referencia['Razão Social'] == melhor_match].iloc[0]
            df.at[index, 'ID_Padronizado'] = match_info['ID']
            df.at[index, 'Razao_Social_Padronizada'] = match_info['Razão Social']
            df.at[index, 'Grupo_Economico_Padronizado'] = match_info['Empresa / Grupo Economico']
    
    print("   -> Padronização de clientes concluída.")

# %%
#Pocesso principal
try:
    # Carrega as bases de referência do arquivo Excel
    excel_file = pd.ExcelFile(caminho_completo)
    df_referencia = excel_file.parse('Base_Referencia')
    df_fases = excel_file.parse('Fases', header=None)
    
    # Prepara a base de referência para a busca
    df_referencia['Razão Social'] = df_referencia['Razão Social'].astype(str).str.upper().str.strip()
    df_referencia['Empresa / Grupo Economico'] = df_referencia['Empresa / Grupo Economico'].astype(str).str.strip()

    # Cria o dicionário para mapear serviços
    mapeamento_servicos = {}
    for _, row in df_fases.iterrows():
        if pd.notna(row[1]): 
            categoria = str(row[0])
            servico = str(row[1])
            mapeamento_servicos[servico.upper().strip()] = categoria.strip()

    # Lista para armazenar todos os DataFrames processados
    todos_os_dfs = []

    # Itera sobre cada aba no arquivo Excel
    for nome_aba in excel_file.sheet_names:
        if nome_aba not in ['Base_Referencia', 'Fases']:
            print(f"\nProcessando a base: {nome_aba}")

            # Carrega a base de dados
            df = excel_file.parse(nome_aba)
            
            # Adiciona a coluna de origem
            df['Base_Origem'] = nome_aba

            # Verifica e renomeia a coluna de clientes
            if 'Nome do Cliente' in df.columns:
                df = df.rename(columns={'Nome do Cliente': 'Nome_Cliente_Bruto'})
            else:
                print(f"Aviso: Coluna 'Nome do Cliente' não encontrada na aba '{nome_aba}'. Pulando.")
                todos_os_dfs.append(df)
                continue

            # Inicia o tratamento de nomes de clientes
            df['Nome_Cliente_Bruto'] = df['Nome_Cliente_Bruto'].astype(str).str.upper().str.strip()
            df['Nome_Cliente_Tratado'] = df['Nome_Cliente_Bruto'].apply(
                lambda x: re.sub(r'[^\w\s]', '', x)
            )

            # Padroniza os serviços
            if 'Fase 2' in df.columns:
                df['Servico_Tratado'] = df['Fase 2'].astype(str).str.upper().str.strip()
                df['Categoria_Padronizada'] = df['Servico_Tratado'].map(mapeamento_servicos)
            
            # Chama a função de padronização de clientes
            padronizar_clientes(df, df_referencia)

            # Adiciona o DataFrame à lista
            todos_os_dfs.append(df)

    #FINALIZAÇÃO E SALVAMENTO
    if todos_os_dfs:
        # Concatena todos os DataFrames em um único
        df_unificado = pd.concat(todos_os_dfs, ignore_index=True)
        
        print("\n--- Processo de Unificação Concluído ---")
        print(f"Total de registros na base unificada: {len(df_unificado)}")
        print(f"Total de clientes únicos padronizados: {df_unificado['ID_Padronizado'].nunique()}")
        
        # Salva o resultado final com um novo nome para evitar conflitos de permissão
        caminho_salvar_excel = 'Data/Data/Processed/base_padronizada_final.xlsx'
        os.makedirs('Data/Data/Processed', exist_ok=True)
        df_unificado.to_excel(caminho_salvar_excel, index=False)
        
        print(f"Base de dados unificada salva em: {caminho_salvar_excel}")
    else:
        print("\nNenhum arquivo de dados de clientes foi encontrado ou processado.")

except FileNotFoundError:
    print(f"Erro: Verifique se o arquivo '{nome_arquivo}' está na pasta '{caminho_dados_brutos}'.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


