# Documents Analysis AzureAI

Este projeto foi desenvolvido com o objetivo de criar uma aplicação utilizando **Streamlit** e os serviços do **Microsoft Azure**. O sistema realiza upload de imagens para o **Azure Blob Storage**, utiliza **Azure Document Intelligence** para analisar informações de cartões de crédito, e exibe os resultados na interface. Foi desenvolvido seguindo os princípios **SOLID** e **Clean Code**, ideal para aprender boas práticas e criar soluções escaláveis.

## Sumário
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Como Executar](#como-executar)
- [Testes](#testes)
- [Exemplo de Uso](#exemplo-de-uso)
- [Licença](#licença)

## Funcionalidades

- Upload de arquivos de imagem (**.png**, **.jpg**, **.jpeg**) para o **Azure Blob Storage**
- Análise de informações de cartões de crédito utilizando o **Azure Document Intelligence**
- Exibição de resultados com validação (cartão válido ou inválido)
- Interface interativa utilizando **Streamlit**

## Tecnologias Utilizadas

- **Linguagem**: Python 3.10+
- **Frameworks/Bibliotecas**:
  - Streamlit - Interface Web
  - Azure Storage Blob - Armazenamento de Arquivos
  - Azure Document Intelligence - Análise de Documentos
  - Python-dotenv - Configuração de Ambiente
- **Testes**: pytest

## Estrutura do Projeto

```
src/
├── app.py                        # Arquivo principal da aplicação
├── services/                     # Serviços que interagem com o Azure
│   ├── blob_service.py          # Serviço para upload no Blob Storage
│   └── credit_card_service.py   # Serviço para análise de cartões de crédito
├── utils/
│   └── config.py                # Configurações do projeto (variáveis de ambiente)
└── requirements.txt             # Dependências do projeto

tests/
├── test_blob_service.py         # Testes unitários para o serviço de blob
└── test_credit_card_service.py  # Testes unitários para o serviço de cartões de crédito
```

## Configuração do Ambiente

1. **Pré-requisitos**:
   - Python 3.10 ou superior
   - Conta no Microsoft Azure
   - Instale as dependências do projeto:
     ```bash
     pip install -r requirements.txt
     ```

2. **Configuração do Azure**:
   - Crie um **Blob Storage** e configure o nome do container
   - Habilite o **Azure Document Intelligence** e gere uma chave de acesso

3. **Configuração do Arquivo `.env`**:
   No diretório `src/`, crie um arquivo `.env` e configure as variáveis abaixo:
   ```
   ENDPOINT=<SEU_ENDPOINT_DO_AZURE_DOCUMENT_INTELLIGENCE>
   KEY=<SUA_CHAVE_DE_ACESSO>
   AZURE_STORAGE_CONNECTION=<CONNECTION_STRING_BLOB_STORAGE>
   CONTAINER_NAME=<NOME_DO_CONTAINER>
   ```

## Como Executar

1. Navegue até o diretório do projeto:
   ```bash
   cd src
   ```

2. Execute a aplicação Streamlit:
   ```bash
   streamlit run app.py
   ```

3. Abra o navegador e acesse o endereço:
   ```
   http://localhost:8501
   ```

## Testes

1. Instale o **pytest** (caso ainda não esteja instalado):
   ```bash
   pip install pytest
   ```

2. Navegue até o diretório raiz do projeto

3. Execute os testes:
   ```bash
   pytest tests/
   ```

4. O pytest gerará um relatório indicando os resultados

## Exemplo de Uso

1. Faça o upload de uma imagem contendo informações de cartão de crédito
2. O sistema realiza o upload para o Azure Blob Storage
3. As informações do cartão são analisadas com o **Azure Document Intelligence**
4. Os resultados são exibidos, indicando:
   - Nome do Titular
   - Banco Emissor
   - Data de Validade
   - Validade do Cartão

## 📧 Contato

Criado com ❤️ por **Paulo Nascimento**. Dúvidas ou sugestões? Entre em contato: **paulo.abreu@aluno.ufabc.edu.br**