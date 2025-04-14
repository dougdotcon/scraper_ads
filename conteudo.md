
API da Biblioteca de Anúncios da Meta
API da Biblioteca de Anúncios
​

Douglas H.
API da Biblioteca de Anúncios
Aceder à API
Notas da versão
API da Biblioteca de Anúncios da Meta
A API da Biblioteca de Anúncios ajuda-te a fazer pesquisas personalizadas na Biblioteca de Anúncios relativas a:
Anúncios sobre questões sociais, eleições ou política que foram apresentados em qualquer lugar do mundo nos últimos 7 anos
Anúncios de qualquer tipo que foram apresentados na União Europeia durante o último ano
Para usar a API, será útil que tenhas alguns conhecimentos de programação. Para facilitar a tua pesquisa, pondera começar com o nosso Relatório da Biblioteca de Anúncios.
Para pesquisar todos os anúncios que estão a ser apresentados atualmente nas tecnologias da Meta, usa a Biblioteca de Anúncios.
A postos para começar?
Para obteres autorização para utilizar a API, precisas de uma conta do Facebook.
Passo 1: confirma a tua identidade e localização
Acede a Facebook.com/ID e conclui o processo de confirmação necessário para apresentar anúncios relacionados com questões sociais, eleições ou política. Pode demorar alguns dias a confirmar as informações que enviares.
Passo 2: cria uma conta da Meta para Programadores
Acede à conta da Meta para Programadores e seleciona "Começar". Como parte da criação da conta, vais ter de aceitar a Política da Plataforma.
Passo 3: adiciona uma app nova
Quando tiveres uma conta, volta a esta página e seleciona Aceder à API. Podes criar uma nova app na opção As minhas apps > Criar app.
Quando a tua app estiver pronta, podes começar a usar a API da Biblioteca de Anúncios
Podes saber mais sobre a criação de consultas e a utilização do ambiente da API Gráfica através da documentação Meta para Programadores
Se fores um programador de API experiente, poderás querer visitar a Repositório de Scripts de API da Biblioteca de Anúncios da Meta no Github, que inclui exemplos de código e uma interface de linha de comandos simples
O que podes pesquisar através da API
Todos os anúncios disponíveis devem incluir:
Identificação da biblioteca
Conteúdos criativos do anúncio (sujeitos aos nossos Termos de Serviço)
Nome da Página e Identificação da Página associados ao anúncio
Datas de apresentação de anúncios
Local onde o anúncio foi apresentado (Facebook, Instagram, etc.)
Anúncios sobre questões sociais, eleições ou políticas também devem incluir:
Montante total gasto (alcance)
Total de impressões recebidas (alcance)
Informações demográficas sobre o alcance dos anúncios, tais como a idade, o género e a localização (%)
Anúncios que foram apresentados na União Europeia também devem incluir:
Total de impressões que um anúncio recebeu na UE (estimativa)
Informações demográficas de definição do público-alvo e de alcance específicas para a UE (estimativa)
Informações sobre o beneficiário e a entidade pagadora
No caso de valores estimados, os dados demográficos agregados baseiam-se em diversos fatores, incluindo as informações de idade e de género que os utilizadores indicarem nos seus perfis do Facebook.
Exemplo de consulta e resposta
Para obter dados sobre anúncios relacionados com questões sociais, eleições ou política que contenham o termo "Califórnia" e que tenham alcançado um público nos Estados Unidos, podes inserir este termo:
curl -G \
-d "search_terms='california'" \
-d "ad_type=POLITICAL_AND_ISSUE_ADS" \
-d "ad_reached_countries=['US']" \
-d "access_token=<ACCESS_TOKEN>" \
"https://graph.facebook.com/<API_VERSION>/ads_archive"
O que devolveria uma resposta como esta:
{
  "data": [
    {
      "page_id": "123",
      "page_name": "123",
      "ad_snapshot_url": "https://www.facebook.com/ads/archive/render_ad/?id=123&amp;access_token=&lt;ACCESS_TOKEN&gt;"
    }
  ],
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MAZDZD"
    },
    "next": "https://graph.facebook.com/v3.1/ads_archive?access_token=&lt;ACCESS_TOKEN&gt;&amp;fields=page_id,page_name,ad_snapshot_url&amp;search_terms='california'&amp;ad_type=POLITICAL_AND_ISSUE_ADS&amp;ad_reached_countries=['US']&amp;limit=25&amp;after=MAZDZD"
  }
}
Parâmetros de pesquisa que podes utilizar para encontrar anúncios:
Tem em conta que alguns parâmetros apenas são válidos para determinados tipos de anúncios, tal como indicado na descrição de parâmetros.
Nome
Descrição
ad_active_status
enum {ACTIVE, ALL, INACTIVE}
Search for ads based on the status. Defaults to ACTIVE for all ads that are eligible for delivery. Set INACTIVE for ads ineligible for delivery, and ALL for both types.
ad_delivery_date_max
string
Search for ads delivered before the date (inclusive) you provide. The date format should be YYYY-mm-dd.
ad_delivery_date_min
string
Search for ads delivered after the date (inclusive) you provide. The date format should be YYYY-mm-dd.
ad_reached_countries
array<enum {ALL, BR, IN, GB, US, CA, AR, AU, AT, BE, CL, CN, CO, HR, DK, DO, EG, FI, FR, DE, GR, HK, ID, IE, IL, IT, JP, JO, KW, LB, MY, MX, NL, NZ, NG, NO, PK, PA, PE, PH, PL, RU, SA, RS, SG, ZA, KR, ES, SE, CH, TW, TH, TR, AE, VE, PT, LU, BG, CZ, SI, IS, SK, LT, TT, BD, LK, KE, HU, MA, CY, JM, EC, RO, BO, GT, CR, QA, SV, HN, NI, PY, UY, PR, BA, PS, TN, BH, VN, GH, MU, UA, MT, BS, MV, OM, MK, LV, EE, IQ, DZ, AL, NP, MO, ME, SN, GE, BN, UG, GP, BB, AZ, TZ, LY, MQ, CM, BW, ET, KZ, NA, MG, NC, MD, FJ, BY, JE, GU, YE, ZM, IM, HT, KH, AW, PF, AF, BM, GY, AM, MW, AG, RW, GG, GM, FO, LC, KY, BJ, AD, GD, VI, BZ, VC, MN, MZ, ML, AO, GF, UZ, DJ, BF, MC, TG, GL, GA, GI, CD, KG, PG, BT, KN, SZ, LS, LA, LI, MP, SR, SC, VG, TC, DM, MR, AX, SM, SL, NE, CG, AI, YT, CV, GN, TM, BI, TJ, VU, SB, ER, WS, AS, FK, GQ, TO, KM, PW, FM, CF, SO, MH, VA, TD, KI, ST, TV, NR, RE, LR, ZW, CI, MM, AN, AQ, BQ, BV, IO, CX, CC, CK, CW, TF, GW, HM, XK, MS, NU, NF, PN, BL, SH, MF, PM, SX, GS, SS, SJ, TL, TK, UM, WF, EH}>
Search ALL or by ISO country code to return ads that reached specific countries or locations. Note: Ads that did not reach any location in the EU will only return if they are about social issues, elections or politics.
Obrigatório
Este parâmetro é obrigatório.
ad_type
enum {ALL, EMPLOYMENT_ADS, FINANCIAL_PRODUCTS_AND_SERVICES_ADS, HOUSING_ADS, POLITICAL_AND_ISSUE_ADS}
Valor predefinido: "ALL"
Search by type of ad. You can use this to narrow your results to ads in special ad categories: FINANCIAL_PRODUCTS_AND_SERVICES_ADS returns ads related to financial products, services, or institutions. EMPLOYMENT_ADS returns ads related to job listings or employment opportunities. HOUSING_ADS returns housing or real estate ads. POLITICAL_AND_ISSUE_ADS returns ads about social issues, elections or politics. ALL returns ads on all topics.FINANCIAL_PRODUCTS_AND_SERVICES_ADS now replaces CREDIT_ADS. Continued usage of CREDIT_ADS will return FINANCIAL_PRODUCTS_AND_SERVICES_ADS data.
bylines
array<string>
Filter results for ads with a paid for by disclaimer byline, such as political ads that reference “immigration” paid for by “ACLU”. Provide a JSON array to search for a byline without a comma or one with a comma. For instance ?bylines=["byline, with a comma,","byline without a comma"] returns results with either text variation. You must list the complete byline. For example, 'Maria' would not return ads with the byline 'Maria C. Lee for America.' Available only for POLITICAL_AND_ISSUE_ADS
delivery_by_region
array<string>
View ads by the region (such as state or province) where Accounts Center accounts were based or located when an ad was displayed to them. You can provide a comma-separated list of regions. For instance ?delivery_by_region=['California', 'New York']. Available only for POLITICAL_AND_ISSUE_ADS
estimated_audience_size_max
int64
Search for ads with a maximum estimated audience size. Must be one of these range boundaries: 1000, 5000, 10000, 50000, 100000, 500000, 1000000. Leave empty for no maximum boundary. Available only for POLITICAL_AND_ISSUE_ADS
estimated_audience_size_min
int64
Search for ads with a minimum estimated audience size. Must be one of these range boundaries: 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000. Leave empty for no minimum boundary. Available only for POLITICAL_AND_ISSUE_ADS
languages
array<string>
Search for ads based on the language(s) contained in the ad. Language codes are based on the ISO 639-1 language codes and also includes ISO 639-3 language codes CMN and YUE.For instance ?languages=['es', 'en'].
media_type
enum {ALL, IMAGE, MEME, VIDEO, NONE}
Search for ads based on whether they contain a specific type of media, such as an image or video.
publisher_platforms
array<enum {FACEBOOK, INSTAGRAM, AUDIENCE_NETWORK, MESSENGER, WHATSAPP, OCULUS, THREADS}>
Search for ads based on whether they appear on a particular Meta technology, such as Instagram or Facebook. You can provide one technology or a comma-separated list of technologies.
search_page_ids
array<int64>
Search for archived ads based on specific Facebook Page IDs. You can provide up to ten IDs, separated by commas.
search_terms
string
Valor predefinido: ""
The terms to search for in your query. We treat a blank space as a logical AND and search for both terms and no other operators. The limit of your string is 100 characters or less. Use search_type to adjust the type of search to use.
search_type
enum {KEYWORD_UNORDERED, KEYWORD_EXACT_PHRASE}
Default value: KEYWORD_UNORDERED The type of search to use for the search_terms field. KEYWORD_UNORDERED will treat each word in search_terms individually, and return results that contain these words in any order. KEYWORD_EXACT_PHRASE will treat the words in search_terms as a single phrase, and only return results that match that exact phrase. To search for multiple phrases at once, separate groups of words in search_terms by commas. This will retrieve results that contain an exact match for every phrase.
unmask_removed_content
boolean
Valor predefinido: false
Specify whether you would like your results to reveal content that was removed for violating our standards.
Campos de dados que podes incluir nos teus resultados de pesquisa:
Tem em conta que alguns campos apenas apresentam dados para determinados tipos de anúncios e/ou locais de apresentação específicos, conforme indicado na descrição do campo.
Nome
Descrição
id
numeric string
The Library ID of the ad object.
ad_creation_time
string
The UTC date and time when someone created the ad. This is not the same time as when the ad ran. Includes date and time separated by T. Example: 2019-01-24T19:02:04+0000, where +0000 is the UTC offset.
ad_creative_bodies
list<string>
A list of the text which displays in each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique text. See Reference, Ad Creative.
ad_creative_link_captions
list<string>
A list of the captions which appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique text that appears in the link.
ad_creative_link_descriptions
list<string>
A list of text descriptions which appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique text describing the link.
ad_creative_link_titles
list<string>
A list of titles which appear in the call to action section for each unique ad card of the ad. Some ads run with multiple ad versions or carousel cards each with their own unique title text about the link.
ad_delivery_start_time
string
Date and time when an advertiser wants to start delivering an ad. Provided in UTC as in ad_creation_time.
Predefinição
Este campo é predefinido.
ad_delivery_stop_time
string
The time when an advertiser wants to stop delivery of their ad. If this is blank, the ad will run until the advertiser stops it or they spend their entire campaign budget. In UTC.
Predefinição
Este campo é predefinido.
ad_snapshot_url
string
String with URL link which displays the archived ad. This displays uncompressed images and videos from the ad. While you cannot currently download a batch of archived ads, you can download ad creative such as images and text for an individual ad. If you do so, it must be for analysis and you must comply with the data storage terms in our Terms of Service.
Predefinição
Este campo é predefinido.
age_country_gender_reach_breakdown
list<AgeCountryGenderReachBreakdown>
The demographic distribution of Accounts Center accounts in the EU reached by the ad. Available only for ads delivered to the EU and POLITICAL_AND_ISSUE_ADS delivered to Brazil
beneficiary_payers
list<BeneficiaryPayer>
The reported beneficiaries and payers for this ad. Available only for ads delivered to the EU
br_total_reach
int32
The estimated ad reach for Brazil. Available for POLITICAL_AND_ISSUE_ADS delivered to Brazil
bylines
string
A string containing the name of the person, company, or entity that provided funding for the ad. Provided by the purchaser of the ad. Available only for POLITICAL_AND_ISSUE_ADS
currency
string
The currency used to pay for the ad, as an ISO currency code. Available only for POLITICAL_AND_ISSUE_ADS
delivery_by_region
list<AudienceDistribution>
Regional distribution of Accounts Center accounts reached by the ad. Provided as a percentage and where regions are at a sub-country level. Available only for POLITICAL_AND_ISSUE_ADS
demographic_distribution
list<AudienceDistribution>
The demographic distribution of Accounts Center accounts reached by the ad. Provided as age ranges and gender. Age ranges: Can be one of 18-24, 25-34, 35-44, 45-54, 55-64, 65+. Gender: Can be the following strings: "Male", "Female", "Unknown". Available only for POLITICAL_AND_ISSUE_ADS
estimated_audience_size
InsightsRangeValue
Estimated Audience Size generally estimates how many Accounts Center accounts meet the targeting and ad placement criteria that advertisers select while creating an ad. Learn more. Available only for POLITICAL_AND_ISSUE_ADS
eu_total_reach
int32
The estimated combined ad reach for all locations inside the European Union. Available only for ads delivered to the EU
impressions
InsightsRangeValue
A string containing the number of times the ad created an impression. In ranges of: <1000, 1K-5K, 5K-10K, 10K-50K, 50K-100K, 100K-200K, 200K-500K, >1M. Available only for POLITICAL_AND_ISSUE_ADS
languages
list<string>
The list of languages contained within the ad. These are displayed in ISO 639-1 language codes.
page_id
numeric string
ID of the Facebook Page that ran the ad.
Predefinição
Este campo é predefinido.
page_name
string
Name of the Facebook Page which ran the ad.
publisher_platforms
list<enum>
A list of Meta technologies where the archived ad appeared, such as Facebook or Instagram.
spend
InsightsRangeValue
A string showing the amount of money spent running the ad, as specified in currency. This is reported in ranges: <100, 100-499, 500-999, 1K-5K, 5K-10K, 10K- 50K, 50K-100K, 100K-200K, 200K-500K, >1M. Available only for POLITICAL_AND_ISSUE_ADS
target_ages
list<numeric string>
The age ranges selected for ad targeting in the EU. The lowest age that can be returned is 13; the highest is 65+. Available only for ads delivered to the EU and POLITICAL_AND_ISSUE_ADS delivered to Brazil
target_gender
enum
The genders selected for ad targeting in the EU. Possible values: “Women”, “Men” or “All”. Available only for ads delivered to the EU and POLITICAL_AND_ISSUE_ADS delivered to Brazil
target_locations
list<TargetLocation>
The locations included or excluded for ad targeting in the EU. Available only for ads delivered to the EU and POLITICAL_AND_ISSUE_ADS delivered to Brazil
Perguntas frequentes
Onde é que a API está disponível?
Preciso de um token de acesso?
Como obtenho dados através da API Gráfica?
Como uso o Explorador da API Gráfica?
Onde posso encontrar documentação adicional para programadores?
Porque é que determinados campos e parâmetros só estão disponíveis para determinados tipos de anúncios?
O que significa o erro 1357045?
Foram fornecidos alguns identificadores individuais para anúncios individuais?
Como são determinadas as datas de início dos anúncios?
Qual é o número máximo de anúncios que uma pesquisa pode obter?
Como é que posso aprender mais sobre anúncios relacionados com assuntos sociais, eleições ou política?
Posso publicar um artigo ou resultados de investigação sobre a utilização da API?
Posso partilhar dados obtidos da API com outros investigadores ou jornalistas?
Tenho uma pergunta que não está aqui. Onde posso encontrar ajuda?
Estado do sistema
Acerca dos anúncios e da utilização de dadosPrivacidadeTermosCookies
Meta © 2025 | Português (Portugal)