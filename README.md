# api-calculadora-equacao-segundo-grau

Projeto que sobe um Container e, neste, uma API RESTful com o Swagger. A partir disso, resolve uma a equação de segundo grau digitada como entrada
## Getting Started

Para executar a aplicação, basta compilar o Docker e executar o mesmo com os seguintes comandos

```
docker-compose build
docker-compose up
```
A partir disso, acesse a URL: localhost:9000/docs e, na aba POST, digite os coeficientes a, b e c da equacao de segundo grau. Como resultado, será exibido a equação completa e a sua respectiva solução.

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Authors

* **Patrick Luiz** - *Initial work*
* **Julia de Souza dos Santos** - *Calculadora de Equacoes de Segundo Grau*

## Exemplo de template copiado de: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
