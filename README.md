# **Documentação da Função Lambda**
## Descrição da Funcionalidade
A função Lambda **'GetCurrentDateTime'** busca a data e a hora atual no momento em que é acionada. Ela retorna a data e a hora no formato "YYYY-MM-DD HH:MM:SS".

## Saída Esperada
Ela processa a solicitação e retorna a data e a hora atual como saída.

- Entrada: N/A
- Saída:
  - **'statusCode'**: O código de status HTTP da resposta (200 para sucesso)
  - **'body'**: A data e a hora atual no formato "YYYY-MM-DD HH:MM:SS"

Exemplo de resposta:

```
{
  "statusCode": 200,
  "body": "2023-06-05 12:34:56"
}
```

## Dependências Externas
A função Lambda não possui dependências externas além dos serviços nativos da AWS.

## Instruções para Execução
1. Acesse o console da AWS (https://aws.amazon.com) e faça login na sua conta.
2. Navegue até o serviço AWS Lambda.
3. Selecione a função Lambda GetCurrentDateTime.
4. Verifique se as configurações e os gatilhos da função estão corretamente configurados.
5. Para testar a função, clique no botão "Teste" na parte superior da página.
6. Selecione ou crie um evento de teste.
7. Clique em "Testar" para executar a função Lambda.
8. Verifique a resposta retornada para garantir que a data e a hora atual estejam corretas.

## Testes e Depuração
Para testar a função Lambda adequadamente, siga as instruções de execução fornecidas acima. Certifique-se de verificar a resposta retornada para garantir que a data e a hora estejam corretas.

Para depurar a função Lambda, você pode usar os recursos de log do AWS Lambda. Os logs fornecerão informações detalhadas sobre a execução da função, incluindo mensagens de erro, registros de eventos e quaisquer outras saídas de registro adicionais que você tenha incluído no código.
