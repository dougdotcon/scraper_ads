# MetaAdsLibraryScraper

Uma ferramenta robusta baseada em Python, com interface gráfica, para extrair e analisar dados de publicidade da API da Meta Ads Library. Ela simplifica a recuperação de dados através de filtros de busca personalizáveis e permite a exportação para Excel para uma análise abrangente.

![Meta Ads Library Scraper](assets/icons/app_preview.png)

## Índice

- [Visão Geral](#visão-geral)
- [Recursos](#recursos)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Guia de Uso](#guia-de-uso)
  - [Configuração da API](#configuração-da-api)
  - [Pesquisa de Anúncios](#pesquisa-de-anúncios)
  - [Visualização e Exportação de Dados](#visualização-e-exportação-de-dados)
- [Parâmetros de Busca](#parâmetros-de-busca)
- [Solução de Problemas](#solução-de-problemas)
- [Perguntas Frequentes](#perguntas-frequentes)

## Visão Geral

O MetaAdsLibraryScraper é projetado para profissionais de marketing, pesquisadores e desenvolvedores que precisam interagir com a API da Meta Ads Library sem lidar com ferramentas complexas de linha de comando. Ele oferece uma forma simplificada e amigável de buscar criativos de anúncios, textos e metadados com base em critérios específicos.

## Recursos

- **GUI Intuitiva**: Construída com `tkinter` do Python para fácil navegação.
- **Filtragem Avançada**: Filtre anúncios por palavras-chave, país, intervalo de datas, plataformas e tipo de anúncio.
- **Exportação de Dados**: Salve os resultados diretamente em formato `.xlsx` (Excel) para análise posterior.
- **Gerenciamento de Token**: Salve e valide seu token de acesso à API da Meta de forma segura.
- **Monitoramento em Tempo Real**: Acompanhe o progresso da extração diretamente na interface.

## Pré-requisitos

- Python 3.7+
- Conexão com a internet
- Conta Meta for Developers (para token de acesso à API)
- Bibliotecas Python (instaladas automaticamente via `requirements.txt`):
  - `tkinter`
  - `requests`
  - `pandas`
  - `openpyxl`
  - `python-dotenv`
  - `Pillow`

## Instalação

1. **Clone o repositório:**
   bash
   git clone https://github.com/yourusername/scraper_ads.git
   cd scraper_ads
   

2. **Instale as dependências:**
   bash
   pip install -r requirements.txt
   

3. **Execute a aplicação:**
   bash
   python main.py
   

## Guia de Uso

### Configuração da API

Antes de buscar anúncios, você deve configurar seu token da API da Meta:

1. Ao iniciar o aplicativo, navegue para a aba **Configuration**.
2. Obtenha seu Token de Acesso no [Portal Meta for Developers](https://developers.facebook.com/).
   - Certifique-se de que o token tenha a permissão `ads_read`.
3. Cole o token no campo "Access Token".
4. Clique em **Save Token** para armazená-lo localmente.
5. Clique em **Validate Token** para verificar a conectividade.

### Pesquisa de Anúncios

1. Mude para a aba **Search**.
2. Insira seus critérios de busca:
   - **Search Terms**: Palavras-chave para buscar no texto do anúncio.
   - **Ad Type**: Categorias específicas (ex: Político, Habitação, Emprego).
   - **Countries**: Códigos de país separados por vírgula (ex: `US, BR, CA`).
   - **Date Range**: Data de início e fim do período de exibição do anúncio.
   - **Platforms**: Onde os anúncios apareceram (Facebook, Instagram, Audience Network).
   - **Ad Status**: Ativo, Inativo ou Todos.
3. Clique em **Search Ads** para iniciar a extração de dados.

### Visualização e Exportação de Dados

- Visualize os resultados na aba **Results**, onde os anúncios são listados com seus detalhes respectivos.
- Clique em uma entrada de anúncio específica para ver detalhes criativos (se disponíveis).
- Use o botão **Export to Excel** para salvar o conjunto completo de dados em uma planilha.

## Parâmetros de Busca

A ferramenta utiliza os endpoints oficiais da API da Meta Ads Library. Parâmetros-chave incluem:

- `search_terms`: String para correspondência de palavras-chave.
- `ad_reached_countries`: Lista de códigos de país ISO 3166-1 alpha-2.
- `ad_type`: Opções incluem `ALL`, `POLITICAL_AND_ISSUE_ADVERTISING`, `HOUSING`, `EMPLOYMENT`, `CREDIT`.
- `start_date` / `end_date`: Formato `YYYY-MM-DD`.
- `platforms`: Lista de plataformas como `FACEBOOK`, `INSTAGRAM`.

## Solução de Problemas

- **Erro "Token Invalid"**: Verifique se seu token não expirou e inclui a permissão `ads_read`.
- **Nenhum Resultado Encontrado**: Amplie seus termos de busca ou remova filtros de país. Note que a API pode não retornar dados para consultas muito específicas/com baixo volume.
- **App Crashes on Start**: Certifique-se de que `tkinter` está instalado (geralmente vem com o Python, mas pode exigir instalação separada no Linux: `sudo apt-get install python3-tk`).

## Perguntas Frequentes

**P: Esta ferramenta é gratuita?**
R: Sim, o software é open source. No entanto, o uso da API da Meta está sujeito aos [Termos da Plataforma](https://developers.facebook.com/terms) e políticas de uso de dados da Meta.

**P: Esta ferramenta faz scraping sem acesso à API?**
R: Não, esta ferramenta depende inteiramente da API oficial da Meta Ads Library. Você deve ter um token de acesso válido.

**P: Posso baixar as imagens reais dos anúncios?**
R: A API fornece links para ativos de mídia. A ferramenta permite exportar esses links, mas o download em massa de imagens pode exigir configurações específicas ou ferramentas adicionais devido aos limites de taxa da API.