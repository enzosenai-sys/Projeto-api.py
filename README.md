# Disney API Explorer 🧭

Explore personagens do universo Disney de forma simples e interativa utilizando a API pública da Disney! Com um clique, você pode visualizar personagens, suas aparições em filmes, séries, parques e muito mais.

## Funcionalidades 🚀

- **Busca por Personagens**: Digite o nome de um personagem para filtrá-los facilmente.
- **Surpreenda-me**: Clique para ser surpreendido com um personagem aleatório.
- **Estatísticas**: Veja estatísticas sobre o total de personagens, filmes e séries.
- **Detalhes do Personagem**: Exiba informações detalhadas como filmes, séries, aliados, inimigos e muito mais.
- **Interface Interativa**: Interface simples e agradável com Streamlit.

## Como Usar 📋

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/disney-api-explorer.git
    cd diseny-api-explorer
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o aplicativo:
    ```bash
    streamlit run app.py
    ```

4. Abra seu navegador e acesse [http://localhost:8501](http://localhost:8501) para começar a explorar os personagens da Disney!

## Tecnologias 🛠️

- **Streamlit**: Framework para criação de aplicativos interativos em Python.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **API Disney**: API pública que fornece dados sobre personagens, filmes, séries e muito mais no universo Disney.

## Visão Geral do Código 💻

### Estrutura do Código

1. **Configuração da Página**: 
    - Usamos o `st.set_page_config` para definir o título e layout da página.

2. **Requisição de Dados**: 
    - Através da API pública da Disney (`https://api.disneyapi.dev/character`), obtemos os dados dos personagens e os armazenamos.

3. **Busca por Personagem**: 
    - O usuário pode buscar por nome de personagem usando o `st.text_input` e um filtro dinâmico é aplicado.

4. **Surpreenda-me**: 
    - Um botão que ao ser pressionado escolhe um personagem aleatoriamente para exibição.

5. **Exibição dos Personagens**: 
    - Informações detalhadas sobre o personagem selecionado, como filmes, séries, aliados, inimigos e muito mais.

6. **Estatísticas**: 
    - Exibimos informações como o total de personagens, quantos estão em filmes e séries de TV.

### Exibição dos Dados

A informação do personagem inclui:
- **Imagem** (se disponível)
- **Filmes, séries, curtas e parques**
- **Aliados e inimigos**
- **Dados em formato JSON**

## Exemplo de Interface 🌐

Ao executar o aplicativo, a interface permite que você:
- Busque personagens diretamente pela caixa de busca.
- Veja personagens em detalhes, com imagens e informações sobre suas aparições em filmes, séries e parques.
- Explore dados brutos em formato JSON.

## Imagens 🌟

![Exemplo de Interface](https://link-para-sua-imagem.com/exemplo.jpg)

## Contribuindo 🤝

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades. Basta fazer um fork do repositório e enviar um pull request!

## Licença 📄

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.



