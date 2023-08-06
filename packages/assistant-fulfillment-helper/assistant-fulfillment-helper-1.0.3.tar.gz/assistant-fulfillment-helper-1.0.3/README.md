# Assistant Fulfillment Helper
Esta biblioteta tem como objetivo facilitar a criação de *webhooks* para os nós de intenção da [Assistente TOTVS](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-carol-assistente/). Com poucas linhas de código, é possivel criar uma regra de negócio customizada em sua propria estrutura de servidor.

## Pré-requisitos:
- [>= Python 3.7](https://www.python.org/downloads/)

## Por onde começar?
Crie um projeto novo e instale o módulo usando PyPI:

```sh
pip install assistant-fulfillment-helper
```

Importe e instancie a classe ``FulfillmentHelper`` para poder definir sua própria regra de negócio. 

```python
fh = FulfillmentHelper()
fh.start() # Inicia um servidor local
```

O código acima irá instanciar o módulo e servirá um Webhook pronto para receber as requisições dos seus nós de intenção da Assistente. Para checar se está tudo certo, abra seu navegador e acesse http://127.0.0.1:5052 (endereço padrão).

O endereço (path) raíz possui dois roteamentos:
- ``GET``: Trás uma mensagem de sucesso com ``http response 200``, e pode ser utilizada como *health check*.
- ``POST``: Iniciará o processamento das [intenções definidas](#definindo-uma-intenção) na sua aplicação. É a chamada que o WebHook espera receber da Assistente.

## Definindo uma Intenção
Para definir uma intenção, basta chamar o método ``registerIntent()`` da classe instanciada ``FulfillmentHelper()``. Por exemplo:

```python
fh = FulfillmentHelper()

fh.registerIntent(
    callback = my_method,
    webhook_token = '{token do webhook aqui}',
    node_name = '{nome do nó de intenção}'
)

fh.start()
```

### registerIntent()
O método ``registerIntent()`` definirá o callback pra cada intenção em uma lista de intenções. Será efetuado uma chamada para o método declarado como callback toda a vez que o Webhook receber uma chamada vinda de um nó da Assistente.
É possível registrar quantos callback de intenções forem necessários, mas apenas um callback é permitido para cada nó.

**Parâmetros:**
| Parâmetro | Obrigatório? | Tipo | Descrição | 
|-----------|--------------|------|-----------|
| ``callback`` | Sim | ``Function`` | Método que será invocado quando o Webhook receber uma chamada desse nó |
| ``webhook_token`` | Sim | ``Str`` | Token disponibilizado pela Assistente na configuração do Nó de Intenção |
| ``node_name`` | Sim | ``Str`` | Nome do Nó de Intenção cadastrado na Assistente |

## Criando um callback
Na chamada do callback, será passado uma variável do tipo ``Dict`` com alguns argumentos que poderão ser utilizados na regra de negócio como quiser. 
Exemplo de um método para callback de um Nó de Intenção:
```python
def my_method(params):
    session = params.get('sessionId')
    message = f"Olá Usuário, nosso id de sessão é: {session}"
    
    return FulfillmentHelperResponse(
        message = message
    )
```

Os parametros passados na chamada do callback são:

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| intent_name | ``Str`` | Nome do nó sendo processado |
| parameters | ``Dict`` | Todos os parametros desse contexto de conversa |
| sessionLog | ``List`` | Lista de ID de sessões até esse ponto da conversa |
| namedQueries | ``Dict`` | Resultados da Named Query (se houver) |
| query | ``Str`` | Query executada (se houver) |
| language | ``Str`` | Idioma da conversa |
| carolOrganization | ``Str`` | Nome da Organização |
| carolEnvironment | ``Str`` | Nome do Ambiente |
| carolOrganizationId | ``Str`` | Id da Organização |
| carolEnvironmentId | ``Str`` | Id do Ambiente |
| sessionId | ``Str`` | Id da sessão da conversa atual |
| isProduction | ``Bool`` | Informa se a convesa está acontecendo em Produção ou Desenvolvimento |
| channelName | ``Str`` | Nome do canal por onde a mensagem chegou |

### Retorno do Callback 
O metodo de callback deve retornar uma classe do tipo ``FulfillmentHelperResponse``, como no [exemplo acima](#iniciando-um-servidor-local). Essa classe possui os seguintes atributos para retorno:

| Parâmetro | Obrigatório? | Tipo | Descrição | 
|-----------|--------------|------|-----------|
| ``message`` | Sim | ``Str`` | Mensagem que será retornada na conversa |
| ``short_message`` | Não | ``Str`` | Mensagem curta de retorno |
| ``jump_to`` | Não | ``Str`` | Nome do nó para o qual a conversa será direcionada |
| ``options`` | Não | ``List[Str]`` | Lista de opções pré-definidas que aparecerão como botões na resposta |
| ``logout`` | Não | ``Bool`` | Destrói a sessão de usuário na conversa ``(default: False)`` |
| ``parameters`` | Não | ``Dict`` | Parametros que serão adicionados no contexto da conversa |

Exemplo de uso:
```python
def callback_boas_vindas(params):
    message = f"Olá, o que deseja fazer agora?"
    
    return FulfillmentHelperResponse(
        message = message,
        short_message = "Boas vindas",
        jump_to = "Pedidos",
        options = [
            "Criar Pedido", 
            "Consultar Pedido"
            "Cancelar Pedido"
        ],
        logout = False,
        parameters = { 'onboarding' : True }
    )
```

## Iniciando um servidor local
O método ``start()`` é responsavel por iniciar um servidor local e deixar pronto para receber requisições como um Webhook. O servidor local pode ser configurado passando algumas propriedades no momento da chamada. Por exemplo:

```python
fh = FulfillmentHelper()

fh.start(
    debug = True
)
```

As configurações customizáveis para o servidor local são:

| Parâmetro | Obrigatório? | Tipo | Default | Descrição | 
|-----------|--------------|------|---------|-----------|
| ``debug`` | Não | ``Bool`` | ``False`` | O Debug ativo habilita verbosidade e reinicia o servidor em cada alteração de código |
| ``host`` | Não | ``Str`` | ``0.0.0.0`` | Nome ou IP do host local |
| ``port`` | Não | ``Int`` | ``5052`` | Porta do host local |


## Exceções 
Os possíveis erros são tratados pelas exceções do módulo. Aqui está a lista das exceções existentes:


| Exceção | Problema | 
|-----------|--------|
| ``DuplicatedIntentNodeException()`` |  Foi tentado adicionar dois métodos de callback para o mesmo Nó de Intenção |
| ``IntentEmptyParamException()`` | Foi tentado registrar um callback de Intenção com algum parâmetro obrigatório vazio |
| ``IntentMissingParamException()`` | Foi tentado registrar um callback de Intenção com algum parâmetro faltando |
| ``IntentInvalidCallbackException()`` | O método passado como Callback não pode ser invocado (*is not callable*) |
| ``IntentResponseInstanceException()`` | O Callback invocado não retornou a classe de resposta esperada (``FulfillmentHelperResponse()``) |
| ``IntentCallbackNotFoundException()`` | O WebHook recebeu uma chamada para um Nó de Intenção indefinido |
| ``InvalidWebhookTokenException()`` | O WebHook token utilizado na chamada é diferente do token informado no registro do nó |

## Executando em ambiente de DEV:
> Dica: Ao invocar o metodo ``start()``, [habilite o Debug](#iniciando-um-servidor-local) para um desenvolvimento mais rápido.

Ao iniciar o webhook local, será necessario disponibilizar a aplicação para fora da sua rede. Para isso recomendamos a utilização de algum software de proxy local, como, por exemplo, o [ngrok](https://ngrok.com/download). Após instalação, execute o comando abaixo em seu terminal para obter a URL pública da sua aplicação. Essa URL poderá ser adicionada como WebHook nas configurações dos seus nós na Assistente para um teste local.

```sh
ngrok http http://127.0.0.1:5052 
```
> NOTA: Informe o host e porta definida na inicialiazação do servidor WebHook.

## Licença
MIT (LICENSE)