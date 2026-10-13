# Projeto 8 — Testes automatizados com Selenium

Automação dos principais passos do pedido de um táxi Comfort no Urban Routes, usando Python, Selenium, Pytest e Page Object Model (POM).

## Estrutura

- `main.py`: testes automatizados e configuração do navegador.
- `pages.py`: localizadores e ações da página Urban Routes.
- `data.py`: URL e dados usados nos testes.
- `helpers.py`: funções auxiliares fornecidas para o projeto.
- `requirements.txt`: versões de Selenium e Pytest.

## Cobertura

O conjunto enviado contém oito testes:

1. Definir os endereços de origem e destino.
2. Selecionar a tarifa Comfort.
3. Preencher o número de telefone.
4. Adicionar um cartão.
5. Escrever um comentário para o motorista.
6. Solicitar cobertor e lenços.
7. Pedir dois sorvetes.
8. Solicitar o táxi e verificar a janela de busca pelo carro.

## Configuração no macOS

Com o terminal aberto na pasta do projeto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install webdriver-manager
```

O `webdriver-manager` é usado pelo `main.py` para obter o ChromeDriver.

## Executar os testes

```bash
python -m pytest main.py -q
```

A execução concluída no PyCharm apresentou **8 passed**.

## Evidência

A captura da execução está em [`evidencias/execucao-8-testes-passaram.png`](evidencias/execucao-8-testes-passaram.png). O resultado final mostrado no terminal é `8 passed`.
