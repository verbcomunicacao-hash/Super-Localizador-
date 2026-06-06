import streamlit as st
import folium
from streamlit_folium import st_folium

# Configuração da Página
st.set_page_config(page_title="Scout Imobiliário Pro", page_icon="🛰️", layout="wide")

# CSS para Acessibilidade e Estilo
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 100px;
        font-size: 24px !important;
        border-radius: 20px;
        background-color: #6366f1;
        color: white;
    }
    .avatar-text {
        font-size: 20px;
        font-weight: bold;
        color: #1e293b;
        background-color: #f1f5f9;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicialização do Estado
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- CABEÇALHO ---
st.title("🛰️ Scout Imobiliário Pro")
st.subheader("Encontre os melhores terrenos com o Vovô Zé e a Bia!")

# --- JORNADA GUIADA ---
col1, col2 = st.columns([1, 3])

with col1:
    if st.session_state.step == 1:
        st.image("https://raw.githubusercontent.com/adapta-one/assets/main/vovo_ze.png", width=150) # Placeholder
        st.markdown('<div class="avatar-text">👴 Vovô Zé: "Olá! Onde você quer procurar um tesouro hoje?"</div>', unsafe_allow_html=True)
        location = st.text_input("Digite a cidade ou zona:", placeholder="Ex: Alcabideche, Cascais")
        if st.button("Próximo ➡️"):
            if location:
                st.session_state.location = location
                st.session_state.step = 2
                st.rerun()

    elif st.session_state.step == 2:
        st.image("https://raw.githubusercontent.com/adapta-one/assets/main/bia.png", width=150) # Placeholder
        st.markdown(f'<div class="avatar-text">👧 Bia: "Legal! Em {st.session_state.location} deve ter muita coisa. Qual o tamanho do castelo que vamos construir?"</div>', unsafe_allow_html=True)
        area = st.slider("Tamanho mínimo (m²):", 5000, 50000, 15000)
        if st.button("Buscar Tesouros! 💎"):
            st.session_state.area = area
            st.session_state.step = 3
            st.rerun()

with col2:
    if st.session_state.step == 3:
        st.success(f"💎 Encontramos 5 terrenos incríveis em {st.session_state.location}!")
        
        # Mapa Exemplo
        m = folium.Map(location=[38.7333, -9.4167], zoom_start=14)
        folium.Marker([38.7333, -9.4167], popup="Terreno A - 25.000m²", icon=folium.Icon(color='green')).add_to(m)
        st_folium(m, width=700, height=500)
        
        if st.button("🔄 Nova Busca"):
            st.session_state.step = 1
            st.rerun()
