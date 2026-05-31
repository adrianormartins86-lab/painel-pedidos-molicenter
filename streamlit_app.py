import streamlit as st
import base64
import os

# Configuração da página para layout amplo (wide)
st.set_page_config(
    page_title="Gestão Pedidos - Molicenter",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Função para converter imagem local para Base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

# Tenta carregar a imagem do passarinho salva na raiz do GitHub
logo_base64 = get_base64_image("passaro_logo.png")
foto_embalagens_base64 = get_base64_image("Embalagens.jpg")
foto_materiaprima_base64 = get_base64_image("materiaprima.jpg")

# Estilização CSS customizada
st.markdown("""
    <style>
    /* Reset e Background Escuro */
    .stApp, .main, .reportview-container {
        background-color: #121212 !important;
        color: #ffffff !important;
    }
    
    /* Banner Principal - Ajustado para o Azul Original */
    .banner-container {
        background: linear-gradient(90deg, #0093E9 0%, #0077b6 100%);
        padding: 12px 20px;
        border-radius: 8px;
        margin-bottom: 25px;
        color: white;
        display: flex;
        align-items: center;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.5);
        border: 1px solid #0093E9;
    }
    .banner-logo {
        height: 42px;
        width: auto;
        object-fit: contain;
        margin-right: 15px;
    }
    .banner-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
    }
    
    /* Cards de Pedidos */
    .card-pedido {
        background-color: #1e1e1e;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
        margin-bottom: 20px;
        border: 1px solid #2d2d2d;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-pedido:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 18px rgba(0, 0, 0, 0.6);
        border-color: #0093E9;
    }
    .card-img {
        width: 100%;
        height: 130px;
        object-fit: cover;
        border-radius: 6px;
        margin-bottom: 12px;
        background-color: #2d2d2d;
        opacity: 0.9;
    }
    
    /* Botão de Título Comercial */
    .btn-titulo {
        background-color: #ffffff;
        color: #121212 !important;
        font-weight: bold;
        padding: 7px 10px;
        border-radius: 4px;
        text-decoration: none;
        display: inline-block;
        margin-bottom: 8px;
        font-size: 13.5px;
        width: 100%;
        transition: background-color 0.2s;
    }
    .btn-titulo:hover {
        background-color: #e0e0e0;
    }
    
    /* Horários e Informações */
    .texto-horario {
        font-size: 11.5px;
        color: #cccccc;
        font-weight: 500;
        line-height: 1.4;
    }
    
    /* Tarja de Sugestões - Ajustada para o Azul Original */
    .section-title-box {
        background-color: #0093E9;
        color: white;
        padding: 8px 15px;
        font-weight: bold;
        border-radius: 6px;
        margin-bottom: 15px;
        font-size: 15px;
        text-align: center;
        border: 1px solid #0082ce;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
    }
    
    .divider-line {
        border-top: 2px solid #2d2d2d;
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Geração do Top Banner
if logo_base64:
    header_html = f"""
        <div class="banner-container">
            <img src="data:image/png;base64,{logo_base64}" class="banner-logo" alt="Logo Molicenter">
            <div class="banner-title">Gestão Pedidos - Molicenter</div>
        </div>
    """
else:
    header_html = """
        <div class="banner-container">
            <span style="font-size: 28px; margin-right: 12px;">🛒</span>
            <div class="banner-title">Gestão Pedidos - Molicenter</div>
        </div>
    """

st.markdown(header_html, unsafe_allow_html=True)

# --- LINKS DAS PLANILHAS CONFIGURADOS ---
LINKS_PEDIDOS = {
    "folhagem": "https://docs.google.com/spreadsheets/d/1y1mCjctvQTwqvxhk67uYnSX4vs_SROAAa7-kZAz07jg/edit?gid=0#gid=0",
    "flv_normal": "https://docs.google.com/spreadsheets/d/1MROR0Tl__10OI--8-VqZdT5e1il64XSdwW3-xR23Cu8/edit?usp=drive_link",
    "flv_ofertas": "https://docs.google.com/spreadsheets/d/1Ic_iNC34IQTUwZhN0qdf6bsTM-EjwshVnNlwjdnI8mI/edit?usp=drive_link",
    "acougue_adriano": "https://docs.google.com/spreadsheets/d/19e0N0FWVdrKtWMG-UroqwPpVKQOqgJ524bBAOuEcyBY/edit?gid=0#gid=0",
    "acougue_pioneiro": "https://docs.google.com/spreadsheets/d/1bBB75w4lshM9Xg70VCuJAzLASpYrp35zYDp8y2vB3Fc/edit?usp=drive_link",
    "pecas_acougue": "https://docs.google.com/spreadsheets/d/19e0N0FWVdrKtWMG-UroqwPpVKQOqgJ524bBAOuEcyBY/edit?gid=0#gid=0",
    "embalagens": "https://docs.google.com/spreadsheets/d/1x2QjCgvjpBl5-QZAqZCNay7aoUvgohjJoAQFdGn4cfE/edit?gid=0#gid=0",
    "materia_prima": "https://docs.google.com/spreadsheets/d/1WDZBbT1J-aSjGNXFfy9HbhKAmAhU5zquqRHYJUXpR0o/edit?gid=0#gid=0",
    "padaria": "https://docs.google.com/spreadsheets/d/14nfvS6jRIJFdTgPpYDxUZNThLSBM4zASFXl_XnOLJOI/edit?gid=0#gid=0",
    "sugestao_hortifruti": "https://1drv.ms/x/s!Aub4upL5X9DiiMQk_TNnm9D1_s7p6A?e=dQbAKD",
    "sugestao_acougue": "https://1drv.ms/x/c/e2d05ff992baf8e6/IQDm-LqS-V_QIIDiA3ICAAAAAf91damk1P4zL0WOZQMb5ys?e=AhVL9h",
}

# --- LINHA 1 DE CARDS ---
row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

with row1_col1:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1574316071802-0d684efa7bf5?w=400" class="card-img" alt="Folhagem">
            <a href="{LINKS_PEDIDOS['folhagem']}" target="_blank" class="btn-titulo">Folhagem</a>
            <div class="texto-horario">Seg a Sáb até 12:00hrs</div>
        </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400" class="card-img" alt="FLV Normal">
            <a href="{LINKS_PEDIDOS['flv_normal']}" target="_blank" class="btn-titulo">FLV Normal</a>
            <div class="texto-horario">
                Terças-feira até 17:00hrs<br>Quintas-feira até 14:00hrs
            </div>
            <div style="margin-top: 10px;">
                <a href="{LINKS_PEDIDOS['flv_ofertas']}" target="_blank" class="btn-titulo">FLV Ofertas</a>
                <div class="texto-horario">Quintas-feira até 14:00hrs</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Açougue Adriano">
            <a href="{LINKS_PEDIDOS['acougue_adriano']}" target="_blank" class="btn-titulo">Açougue Adriano</a>
            <div class="texto-horario">
                Quartas-feira até 15:00hrs<br>Sábado até 15:00hrs
            </div>
        </div>
    """, unsafe_allow_html=True)

with row1_col4:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Açougue Pioneiro">
            <a href="{LINKS_PEDIDOS['acougue_pioneiro']}" target="_blank" class="btn-titulo">Pioneiro + BF + Paraná</a>
            <div class="texto-horario">Seg a Sex até 11:00hrs</div>
        </div>
    """, unsafe_allow_html=True)


# --- LINHA 2 DE CARDS ---
row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

with row2_col1:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Peças Açougue">
            <a href="{LINKS_PEDIDOS['pecas_acougue']}" target="_blank" class="btn-titulo">Peças Açougue</a>
            <div class="texto-horario">
                Seg / Qua e Sex - Arapongas até as 15:00h<br>
                Ter / Qui e Sáb - Maringá até as 15:00h
            </div>
        </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="data:image/jpeg;base64,{foto_embalagens_base64}" class="card-img" alt="Embalagens">
            <a href="{LINKS_PEDIDOS['embalagens']}" target="_blank" class="btn-titulo">Embalagens</a>
            <div class="texto-horario">Sexta-feira até as 17:30hrs</div>
        </div>
    """, unsafe_allow_html=True)

with row2_col3:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="data:image/jpeg;base64,{foto_materiaprima_base64}" class="card-img" alt="Matéria Prima">
            <a href="{LINKS_PEDIDOS['materia_prima']}" target="_blank" class="btn-titulo">Matéria Prima</a>
            <div class="texto-horario">Até Sábado</div>
        </div>
    """, unsafe_allow_html=True)

with row2_col4:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400" class="card-img" alt="Padaria e Confeitaria">
            <a href="{LINKS_PEDIDOS['padaria']}" target="_blank" class="btn-titulo">Padaria e Confeitaria</a>
            <div class="texto-horario">Sábado</div>
        </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)


# --- LINHA 3: SEÇÃO DE SUGESTÕES CENTRALIZADA ---
col_left, col_center, col_right = st.columns([0.5, 3, 0.5])

with col_center:
    st.markdown('<div class="section-title-box">Sugestão de Pedidos</div>', unsafe_allow_html=True)
    sub_col1, sub_col2 = st.columns(2)
    
    with sub_col1:
        st.markdown(f"""
            <div class="card-pedido">
                <img src="https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400" class="card-img" alt="Hortifruti">
                <a href="{LINKS_PEDIDOS['sugestao_hortifruti']}" target="_blank" class="btn-titulo" style="background-color: #ffffff; color: white !important;">Hortifruti</a>
            </div>
        """, unsafe_allow_html=True)
        
    with sub_col2:
        st.markdown(f"""
            <div class="card-pedido">
                <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Açougue">
                <a href="{LINKS_PEDIDOS['sugestao_acougue']}" target="_blank" class="btn-titulo" style="background-color: #ffffff; color: white !important;">Açougue</a>
            </div>
        """, unsafe_allow_html=True)

# Rodapé informativo
st.markdown("""
    <div style="text-align: center; margin-top: 40px; color: #ffffff; font-size: 11px;">
        Molicenter Supermercados © 2026 - Painel Web de Pedidos Centralizados
    </div>
""", unsafe_allow_html=True)
