# Guia de Configuração e Teste da Aplicação Flask com Tavern

Siga os passos abaixo para configurar e testar a aplicação Flask utilizando Tavern para testes de API.

## 1. Ativar o Ambiente Virtual

Crie e ative um ambiente virtual para isolar as dependências do projeto.

```bash
python3 -m venv meu_ambiente_virtual
source meu_ambiente_virtual/bin/activate
```

## 2. Instalar as Dependências

Instale o Flask e o Tavern usando o pip.

```bash
pip install Flask
pip install tavern
```

## 3. Rodar o Servidor Usando Flask

Configure a variável de ambiente `FLASK_APP` para apontar para o seu arquivo `server.py` e inicie o servidor Flask.

```bash
export FLASK_APP=server.py
flask run
```

O servidor estará em execução e acessível pelo navegador.

## 4. Rodar os Testes com Tavern

Abra outro terminal para executar os testes enquanto o servidor está em execução.

```bash
py.test test_fruta_api.tavern.yaml -v
```

Certifique-se de que o arquivo `test_minimal.tavern.yaml` esteja configurado corretamente para testar as rotas da sua API.

---

Se precisar de mais informações, consulte a documentação do [Flask](https://flask.palletsprojects.com/en/latest/) e do [Tavern](https://tavern.readthedocs.io/en/latest/).

Assim, o guia está completo com todos os passos necessários para configurar e testar sua aplicação Flask.
