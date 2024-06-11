# Baccarat Live 

Este script automatiza o processo de login e acompanhamento de resultados de jogos de Baccarat ao vivo no site Blaze. Utilizando a biblioteca Playwright para automação de navegador, o script acessa a página de login, insere as credenciais de usuário, e navega para a área de jogos de Baccarat. Em seguida, ele monitora e coleta os resultados dos jogos em tempo real.

## Funcionalidades

- **Login Automático**: Realiza o login no site utilizando credenciais armazenadas em um arquivo JSON ou solicita as credenciais do usuário se o arquivo não existir.
- **Idioma pt-BR**: O site é sempre carregado em português do Brasil.
- **Rastreamento de Resultados**: Acompanha os resultados dos jogos de Baccarat ao vivo e os classifica de acordo com os critérios definidos (Empate Vermelho, Empate Azul, Vermelho, Azul).
- **Armazenamento de Resultados**: Mantém listas atualizadas dos resultados recentes para múltiplas mesas de Baccarat.

## Dependências

- `playwright`
- `beautifulsoup4`
- `requests`

## Como Usar

1. **Instale as dependências**:

    ```bash
    pip install playwright beautifulsoup4 requests
    ```

2. **Execute o script**:

    ```bash
    python versao_final.py
    ```

3. **Siga as instruções no terminal** para inserir suas credenciais caso necessário.

## Estrutura do Código

- **Função `run(playwright)`**: Principal função que configura o navegador, realiza login, navega para a página de jogos de Baccarat, e monitora os resultados.
- **Função `tempo()`**: Função auxiliar para pausas no script.
- **Função `main()`**: Inicia o Playwright e executa a função `run(playwright)`.

## Notas

- O script é configurado para rodar em um navegador visível (`headless=False`) para facilitar a depuração.
- Certifique-se de ter um arquivo `credenciais.json` com suas credenciais de login, ou insira-as quando solicitado.
- Para parar o script, pressione `Ctrl+C`.

## Exemplo de Arquivo `credenciais.json`

```json
{
  "email": "seu_email@example.com",
  "password": "sua_senha"
}
