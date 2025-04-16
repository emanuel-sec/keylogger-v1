# Keylogger Educacional em Python

## Descrição
Este é um projeto educacional de um **keylogger simples** desenvolvido em Python. O objetivo é estudar e entender como capturar entradas de teclado, obter informações do sistema e realizar capturas de tela automaticamente. Este projeto é **exclusivamente para fins educacionais e foi executado localmente**.

### Funcionalidades
- **Captura de teclas**: Registra todas as teclas pressionadas no teclado.
- **Informações do sistema**: Obtém informações como o nome de usuário, hostname, IP local e detalhes do sistema operacional.
- **Captura de tela**: Tira screenshots automaticamente a cada intervalo de tempo configurado (default: 60 segundos).
  
## Tecnologias utilizadas
- Python 3.x
- Bibliotecas: `pynput`, `Pillow`, `threading`, `datetime`
- Sistema Operacional: Windows/Linux (funciona em ambos)

## Como rodar o projeto
1. Clone este repositório ou baixe o arquivo `.zip` do projeto.
2. Instale as dependências necessárias:
   ```bash
   pip install pynput pillow
