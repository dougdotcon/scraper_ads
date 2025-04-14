# Meta Ads Library Scraper

Uma aplicação para extrair e analisar dados da API da Meta Ads Library com interface gráfica amigável.

![Meta Ads Library Scraper](assets/icons/app_preview.png)

## Índice

- [Visão Geral](#visão-geral)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
  - [Configuração da API](#configuração-da-api)
  - [Pesquisa de Anúncios](#pesquisa-de-anúncios)
  - [Visualização de Resultados](#visualização-de-resultados)
  - [Exportação de Dados](#exportação-de-dados)
- [Parâmetros de Pesquisa](#parâmetros-de-pesquisa)
- [Solução de Problemas](#solução-de-problemas)
- [Perguntas Frequentes](#perguntas-frequentes)

## Visão Geral

O Meta Ads Library Scraper é uma ferramenta que permite extrair dados da API da Biblioteca de Anúncios da Meta (Facebook, Instagram, etc.) de forma simples e eficiente. Com esta aplicação, você pode:

- Pesquisar anúncios usando diversos critérios e filtros
- Visualizar os resultados em uma interface amigável
- Exportar os dados para Excel para análise posterior
- Configurar facilmente sua conexão com a API da Meta

## Requisitos

- Python 3.7 ou superior
- Conexão com a internet
- Token de acesso à API da Meta Ads Library
- Bibliotecas Python (instaladas automaticamente):
  - tkinter
  - requests
  - pandas
  - openpyxl
  - python-dotenv
  - Pillow

## Instalação

1. Clone ou baixe este repositório para seu computador
2. Abra um terminal ou prompt de comando na pasta do projeto
3. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

4. Execute a aplicação:

```bash
python main.py
```

## Como Usar

### Configuração da API

Antes de começar a usar a aplicação, você precisa configurar seu token de acesso à API da Meta Ads Library:

1. Ao iniciar a aplicação pela primeira vez, você será direcionado automaticamente para a aba "Configuration"
2. Siga os passos indicados na tela para obter um token de acesso:
   - Crie uma conta Meta for Developers
   - Crie um novo aplicativo
   - Gere um token de acesso com permissão `ads_read`
3. Cole o token no campo "Access Token"
4. Clique em "Save Token" para salvar
5. Clique em "Validate Token" para verificar se o token é válido

![Configuração da API](assets/icons/config_tab.png)

### Pesquisa de Anúncios

Após configurar seu token de API, você pode começar a pesquisar anúncios:

1. Vá para a aba "Search"
2. Preencha os campos de pesquisa conforme necessário:
   - **Search Terms**: Palavras-chave para buscar nos anúncios
   - **Ad Type**: Tipo de anúncio (político, habitação, emprego, etc.)
   - **Countries**: Países onde os anúncios foram exibidos (códigos de país separados por vírgula)
   - **Date Range**: Intervalo de datas para a pesquisa
   - **Platforms**: Plataformas onde os anúncios foram exibidos (Facebook, Instagram, etc.)
   - **Ad Status**: Status dos anúncios (ativos, inativos, todos)
3. Clique no botão "Search Ads" para iniciar a pesquisa

![Pesquisa de Anúncios](assets/icons/search_tab.png)

### Visualização de Resultados

Os resultados da pesquisa serão exibidos na área abaixo das abas:

1. A tabela mostra uma visão geral dos anúncios encontrados
2. Clique em um anúncio na tabela para ver detalhes adicionais no painel à direita
3. Use a barra de rolagem para navegar pelos resultados
4. Clique duas vezes em um anúncio ou use o botão "Open Ad in Browser" para ver o anúncio original no navegador

![Visualização de Resultados](assets/icons/results_view.png)

### Exportação de Dados

Você pode exportar os resultados da pesquisa para um arquivo Excel:

1. Após realizar uma pesquisa, clique no botão "Export to Excel"
2. Escolha um local e nome para salvar o arquivo
3. O arquivo Excel conterá várias abas:
   - **Ad Data**: Informações básicas sobre os anúncios
   - **Demographics**: Dados demográficos (se disponíveis)
   - **Search Parameters**: Parâmetros usados na pesquisa

## Parâmetros de Pesquisa

### Search Terms
Palavras-chave para buscar no conteúdo dos anúncios. Você pode usar termos simples ou frases.

### Ad Type
- **ALL**: Todos os tipos de anúncios
- **POLITICAL_AND_ISSUE_ADS**: Anúncios políticos ou sobre questões sociais
- **HOUSING_ADS**: Anúncios de habitação ou imóveis
- **EMPLOYMENT_ADS**: Anúncios de emprego
- **FINANCIAL_PRODUCTS_AND_SERVICES_ADS**: Anúncios de produtos financeiros

### Countries
Códigos de país ISO de duas letras, separados por vírgula (ex: US,BR,DE).

### Date Range
Intervalo de datas em que os anúncios foram veiculados, no formato YYYY-MM-DD.

### Platforms
- **Facebook**: Anúncios exibidos no Facebook
- **Instagram**: Anúncios exibidos no Instagram
- **Audience Network**: Anúncios exibidos na rede de parceiros da Meta
- **Messenger**: Anúncios exibidos no Messenger
- **WhatsApp**: Anúncios exibidos no WhatsApp

### Ad Status
- **ACTIVE**: Anúncios atualmente ativos
- **INACTIVE**: Anúncios que não estão mais ativos
- **ALL**: Todos os anúncios, independentemente do status

## Solução de Problemas

### Token Inválido
Se seu token for rejeitado, verifique se:
- O token não expirou (tokens geralmente expiram após algumas horas)
- Você tem as permissões corretas (ads_read)
- Você colou o token completo, sem espaços extras

### Nenhum Resultado Encontrado
Se sua pesquisa não retornar resultados, tente:
- Usar termos de pesquisa mais amplos
- Expandir o intervalo de datas
- Verificar se os códigos de país estão corretos
- Selecionar mais plataformas

### Aplicação Lenta
Se a aplicação estiver lenta, considere:
- Limitar sua pesquisa com filtros mais específicos
- Reduzir o intervalo de datas
- Verificar sua conexão com a internet

## Perguntas Frequentes

### Quantos anúncios posso extrair de uma vez?
A API da Meta tem limites de taxa. Por padrão, a aplicação tenta obter até 1000 anúncios por pesquisa, mas você pode ajustar esse valor nas configurações avançadas.

### Os dados são atualizados em tempo real?
Sim, a aplicação consulta diretamente a API da Meta, então os dados são os mais recentes disponíveis.

### Posso salvar minhas configurações de pesquisa?
Atualmente, apenas o token de API é salvo entre sessões. As configurações de pesquisa precisam ser inseridas novamente a cada vez.

### É possível automatizar pesquisas?
Esta versão da aplicação é focada na interface gráfica. Para automação, considere usar diretamente os módulos Python em scripts personalizados.

---

Desenvolvido com ❤️ para facilitar o acesso e análise de dados da Meta Ads Library.
