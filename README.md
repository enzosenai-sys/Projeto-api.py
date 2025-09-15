📁 Estrutura Final do Projeto
📦 disney-api-explorer
├── app.py               ← Código principal da aplicação
├── requirements.txt     ← Dependências
└── README.md            ← Documentação

✅ app.py
import streamlit as st
import requests
import random

API_URL = "https://api.disneyapi.dev/character"

# Configuração da página
st.set_page_config(page_title="Disney API Explorer", page_icon="🧭", layout="wide")

# Título principal
st.markdown("# 🧭 Disney API Explorer")
st.markdown("Explore personagens do universo Disney com um clique!")

# Requisição de dados
response = requests.get(f"{API_URL}?page=1&pageSize=500")
data = response.json()
characters = data["data"]

# Dicionário para facilitar busca por nome
char_dict = {c["name"]: c for c in characters}

# Busca por nome
with st.sidebar:
    st.markdown("### 🔍 Buscar personagem")
    search_query = st.text_input("Digite parte do nome:")

    if search_query:
        filtered_chars = [c for c in characters if search_query.lower() in c["name"].lower()]
        if filtered_chars:
            selected_name = st.selectbox("Resultados:", [c["name"] for c in filtered_chars])
            selected_char = next(c for c in filtered_chars if c["name"] == selected_name)
        else:
            st.warning("Nenhum personagem encontrado.")
            selected_char = None
    else:
        selected_name = st.selectbox(
            "Escolha um personagem:",
            sorted(char_dict.keys()),
            index=sorted(char_dict.keys()).index(st.session_state.get("selected_name", sorted(char_dict.keys())[0]))
        )
        selected_char = char_dict[selected_name]

    if st.button("🎲 Surpreenda-me!"):
        selected_char = random.choice(characters)
        st.session_state["selected_name"] = selected_char["name"]
        st.rerun()

    st.divider()
    st.markdown("### 📊 Estatísticas")
    total = len(characters)
    films_count = sum(1 for c in characters if c["films"])
    tv_count = sum(1 for c in characters if c["tvShows"])
    st.write("👤 Total de personagens:", total)
    st.write("🎬 Em filmes:", films_count)
    st.write("📺 Em séries:", tv_count)
    st.divider()
    st.markdown("[🌍 API da Disney](https://disneyapi.dev/)")

st.divider()

if selected_char:
    st.subheader(f"🎭 {selected_char['name']}")

    col1, col2 = st.columns([1, 2])

    with col1:
        if selected_char.get("imageUrl"):
            st.image(selected_char["imageUrl"], width=250)
        else:
            st.info("Imagem não disponível.")

    with col2:
        st.markdown("#### 🎞️ Aparições")
        st.write("**Filmes:**", ", ".join(selected_char.get("films", []) or ["Nenhum"]))
        st.write("**Séries de TV:**", ", ".join(selected_char.get("tvShows", []) or ["Nenhuma"]))
        st.write("**Curtas:**", ", ".join(selected_char.get("shortFilms", []) or ["Nenhum"]))
        st.write("**Parques:**", ", ".join(selected_char.get("parkAttractions", []) or ["Nenhum"]))

        st.markdown("#### 🧑‍🤝‍🧑 Relações")
        st.write("**Aliados:**", ", ".join(selected_char.get("allies", []) or ["Nenhum"]))
        st.write("**Inimigos:**", ", ".join(selected_char.get("enemies", []) or ["Nenhum"]))

    with st.expander("📦 Ver dados brutos (JSON)"):
        st.json(selected_char)

📄 requirements.txt
streamlit>=1.25.0
requests

📘 README.md
# 🧭 Disney API Explorer

Um aplicativo interativo feito com [Streamlit](https://streamlit.io/) que permite explorar personagens do universo Disney usando a API pública [DisneyAPI.dev](https://disneyapi.dev/).

---

## 🚀 Funcionalidades

- 🔍 **Busca por nome** de personagens Disney
- 🎲 **Personagem aleatório** ("Surpreenda-me!")
- 📊 **Estatísticas gerais** (total de personagens, aparições em filmes/séries)
- 📷 **Imagem do personagem**, se disponível
- 🎞️ Lista de **filmes, séries, curtas e atrações**
- 🧑‍🤝‍🧑 **Relações**: aliados e inimigos
- 📦 Visualização de **dados brutos (JSON)**

---

## 🛠️ Tecnologias utilizadas

- Python 3.9+
- Streamlit
- Requests
- [DisneyAPI.dev](https://disneyapi.dev)

---

## ▶️ Como executar localmente

1. **Clone este repositório**:

```bash
git clone https://github.com/seu-usuario/disney-api-explorer.git
cd disney-api-explorer


Crie um ambiente virtual (opcional):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Instale as dependências:

pip install -r requirements.txt


Execute o app:

streamlit run app.py

🌐 Fonte de dados

Este projeto utiliza a API gratuita:
🔗 https://disneyapi.dev

Nota: A API não é oficial da Disney. Use apenas para fins educacionais ou protótipos.

📂 Estrutura do Projeto
📦 disney-api-explorer
├── app.py               # Aplicação principal em Streamlit
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto

🤝 Contribuições

Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar PRs.

📄 Licença

Este projeto está licenciado sob a MIT License.
Veja o arquivo LICENSE
 para mais detalhes.

✨ Autor

Feito com ❤️ por Seu Nome


---

Se quiser, posso empacotar tudo isso num `.zip` para você baixar ou ajudar a publicar no GitHub ou no **Streamlit Community Cloud**.

Deseja isso?
