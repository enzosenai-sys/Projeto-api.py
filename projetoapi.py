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

    # Filtragem ao vivo
    if search_query:
        filtered_chars = [c for c in characters if search_query.lower() in c["name"].lower()]
        if filtered_chars:
            selected_name = st.selectbox("Resultados:", [c["name"] for c in filtered_chars])
            selected_char = next(c for c in filtered_chars if c["name"] == selected_name)
        else:
            st.warning("Nenhum personagem encontrado.")
            selected_char = None
    else:
        # Select padrão quando não há busca
        selected_name = st.selectbox(
            "Escolha um personagem:",
            sorted(char_dict.keys()),
            index=sorted(char_dict.keys()).index(st.session_state.get("selected_name", sorted(char_dict.keys())[0]))
        )
        selected_char = char_dict[selected_name]

    # Botão "Surpreenda-me"
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

# Separador visual
st.divider()

# Exibição dos dados do personagem
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

    # Dados brutos em expansor
    with st.expander("📦 Ver dados brutos (JSON)"):
        st.json(selected_char)
