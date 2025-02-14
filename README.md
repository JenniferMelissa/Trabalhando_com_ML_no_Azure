<h1 align="center"> Trabalhando com Machine Learning automatizado no Azure Machine Learning  </h1><br>

##  :bulb: Primeiro passo do projeto:

Criação de Gerador de arquivo csv de consumo diário de energia em linguagem Python.
##  :bulb: Segundo passo do projeto:

1. Entre no portal do Azure usando https://portal.azure.comsuas credenciais da Microsoft.<br>
2. Selecione + Criar um recurso, pesquise por Machine Learning e crie um novo recurso do Azure Machine Learning com as seguintes configurações:
  - Assinatura : sua assinatura do Azure .
  - Grupo de recursos : crie ou selecione um grupo de recursos.
  - Nome : Insira um nome exclusivo para seu espaço de trabalho.
  - Região : Leste dos EUA.
  - Conta de armazenamento : observe a nova conta de armazenamento padrão que será criada para seu espaço de trabalho.
  - Cofre de chaves : observe o novo cofre de chaves padrão que será criado para seu espaço de trabalho.
  - Insights do aplicativo : observe o novo recurso padrão de insights do aplicativo que será criado para seu espaço de trabalho.
  - Registro de contêiner : Nenhum (um será criado automaticamente na primeira vez que você implantar um modelo em um contêiner .

3. Selecione Review + create e, em seguida, selecione Create .<br>
4. Aguarde a criação do seu workspace (pode levar alguns minutos) e, em seguida, vá para o recurso implantado.
</ol>

## Estúdio de lançamento 

No seu recurso de espaço de trabalho do Azure Machine Learning, selecione Iniciar estúdio (ou abra uma nova guia do navegador e 
navegue até https://ml.azure.com e entre no estúdio do Azure Machine Learning usando sua conta da Microsoft). 
  
## Azure Machine Learning Studio 
Você deve ver seu workspace recém-criado. Caso contrário, selecione All workspaces no menu à esquerda e, em seguida, 
selecione o workspace que você acabou de criar.


No Azure Machine Learning Studio , visualize a página ML automatizado (em Criação).
Crie um novo trabalho de ML automatizado com as seguintes configurações, usando Avançar conforme necessário para avançar pela interface do usuário:

- Nome do trabalho : O campo Nome do trabalho já deve estar preenchido previamente com um nome exclusivo. Mantenha-o como está.
- Novo nome do experimento :consumo_energia_diario
- Descrição : Aprendizado de máquina automatizado para previsão  doonsumo diário de energia elétrica
- Tags : nenhuma

## Tipo de tarefa e dados :

- Selecione o tipo de tarefa : Regressão
- Selecionar conjunto de dados : Crie um novo conjunto de dados com as seguintes configurações:

### Tipo de dados :

- Nome :consumo_energia_diario
- Descrição : Consumo diário de energia ao longo de um ano,
- Tipo : Tabular

### Fonte de dados : 

- Selecione De arquivos locais

- Tipo de armazenamento de dados : Azure Blob Storage
- Carregue caminho ou pasta: Escolhi o local do arquivo criado através do script em python.

### Configurações:
- Formato de Arquivos:  Delimitado
- Delimitador: Vírgula
- Codificação: UTF - 8
- Cabeçalho de colunas: Somente o primeiro arquivo tem cabeçalho
- Ignorar linhas: Nenhum
  
Avance até terminar as abas e clique em Criar.
Selecione seu dado agora já criado e avance.

### Configurações de Tarefas :

- Tipo de tarefa : Regressão
- Conjunto de dados : consumo_energia_diario
- Coluna de destino : energy_consumption(decimal) (inteiro)

### Configurações adicionais : 

- Métrica primária : NormalizedRootMeanSquaredError
- Explique o melhor modelo : Não selecionado
- Habilitar empilhamento de conjunto : Não selecionado
- Usar todos os modelos suportados : Não selecionado.
- Modelos permitidos : Selecione apenas RandomForest e LightGBM

### Validar e testar :
- Tipo de validação : Divisão de validação de trem
- Porcentagem de dados de validação : 10
- Conjunto de dados de teste : Nenhum

### Limites : Expandir esta seção
- Máximo de ensaios :3
- Máximo de ensaios simultâneos :3
- Máximo de nós :3
- Limite de pontuação métrica : 0.085( para que se um modelo atingir uma pontuação métrica de erro quadrático médio normalizado de 0,085 ou menos, o trabalho termine. )
- Tempo limite do experimento :15
- Tempo limite de iteração :15
- Habilitar rescisão antecipada : Selecionado

## Computação
- Selecione o tipo de computação : Sem servidor
- Tipo de máquina virtual : CPU
- Camada de máquina virtual : Dedicada
- Tamanho da máquina virtual : Standard_D4s_v3 
- Número de instâncias : 1
* Se sua assinatura restringir os tamanhos de VM disponíveis para você, escolha qualquer tamanho disponível.

5 Envie o trabalho de treinamento. Ele inicia automaticamente.</li>

6. Implantar e testar o modelo


## :pushpin:  Ponto de Extremidade em Tempo Real 

Na Guia Modelo Para o melhor modelo treinado pelo seu trabalho de aprendizado de máquina automatizado, selecione Implantar e use a opção Ponto de extremidade em tempo real para implantar o modelo com as seguintes configurações:
- Selecione o modelo criado: consumo_de_energia_2 (o melhor treinado)
- Nome do Projeto Atual: laboratorioai900
- Contagem de instâncias : 3
- Máquina virtual : Standard_D2as_v4

- Ponto de Extremidade : Novo
- Nome do ponto de extremidade : laboratorioai900-whsmt
- Nome da implantação : consumoenergiad2-1
- Inferência de coleta de dados : Desativado
- Modelo de pacote : Desativado


1. Aguarde o início da implantação - isso pode levar alguns segundos. O status de Implantação para o endpoint predict-rentals será indicado na parte principal da página como Running .
2. Aguarde até que o status Deploy mude para Succeeded . Isso pode levar de 5 a 10 minutos.
3. Teste o serviço implantado

Agora você pode testar seu serviço implantado.

## :pushpin: Azure Machine Learning Studio

1. Selecione Endpoints e abra o endpoint em tempo real predict-rentals .

2. Na página do endpoint em tempo real do predict-rentals , visualize a guia Teste .

3. No painel Dados de entrada para testar o ponto de extremidade , foi substituido o JSON do modelo pelos seguintes dados de entrada:

{
  "input_data": {
    "columns": [
      "day",
      "mnth",
      "year",
      "season",
      "holiday",
      "weekday",
      "workingday",
      "weathersit",
      "temp",
      "hum",
      "windspeed",
      "energy_consumption"
    ],
    "index": [0],
    "data": [[15, 6, 2024, 3, 0, 5, 1, 1, 0.75, 0.55, 0.20, 1250.5]]
  }
}

4. Clique no botão Testar.
 
5. resultado:

[
  1494.2610477358962
]

## Esse resultado representa o consumo médio de energia para cada estação do ano.

