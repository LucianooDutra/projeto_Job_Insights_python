# Projeto Job Insights!

## Sobre o projeto:

O Job Insights é um site sobre análises a partir de um conjunto de dados sobre empregos.

Suas implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). também foi escrito alguns testes para a implementação de uma análise de dados. Por fim, como bônus, foi escrito uma rota e view para um recurso novo usando Flask!

  Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

 - O site é responsavel por:

 - Fazer a busca por empregos utilizando alguns filtros como por Tipo de emprego, indústria, salário anual;
 - Decidir como mostrar a quantidade de resultados;
 - Ao clicar no job, mostra detalhes sobre a vaga de emprego;

# Técnologias utilizadas:

 - Python;
 - Flask;
 - Flake8;
 - Pytest;

# Habilidades trabalhadas:

 - terminal interativo do Python;
 - estruturas condicionais e de repetição;
 - funções built-in do Python;
 - tratamento de exceções;
 - manipulação de arquivos;
 - funções;
 - testes com Pytest;
 - escrever módulos e importá-los em outros códigos;

## Instalando as dependências

<details>

  ```json
    # Clone o repositório:
    git clone git@github.com:LucianooDutra/projeto_Job_Insights_python.git
    
    # Entre no diretório:
    cd projeto_Job_Insights_python
    
    # Crie o ambiente virtual para o projeto:
    python3 -m venv .venv && source .venv/bin/activate
    
    # Instale as dependências:
    python3 -m pip install -r dev-requirements.txt
  ```

</details>

## Rodando o front-end

<details>
 <summary><strong>Front-End</strong></summary><br />

- Para rodar o front-end basta executar o comando abaixo a partir da raiz do projeto:

  ```json
    flask run
  ```

- Acesse o site gerado pelo Flask em http://localhost:5000

</details>


## Executando os testes

<details>
 <summary><strong>Testes</strong></summary><br />

 Foi utilizado o Pytest para a realização dos testes;

- Para rodar todos os testes:

Para executar todos os testes digite o seguinte comando no terminal a partir da raiz do projeto:

  ```json
    python3 -m pytest
  ```

</details>

