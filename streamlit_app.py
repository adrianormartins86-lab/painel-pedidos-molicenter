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

# Estilização CSS customizada - Versão Compacta (Efeito Zoom 67%)
st.markdown("""
    <style>
    /* Reset e Background Escuro */
    .stApp, .main, .reportview-container {
        background-color: #121212 !important;
        color: #ffffff !important;
    }
    
    /* Banner Principal Mais Compacto */
    .banner-container {
        background: linear-gradient(90deg, #1e1e1e 0%, #2d2d2d 100%);
        padding: 10px 18px;
        border-radius: 6px;
        margin-bottom: 15px;
        color: white;
        display: flex;
        align-items: center;
        box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.4);
        border: 1px solid #3d3d3d;
    }
    .banner-logo {
        height: 35px; /* Altura ideal compacta */
        width: auto;
        object-fit: contain;
        margin-right: 12px;
    }
    .banner-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 20px; /* Reduzido de 26px para equilíbrio */
        font-weight: bold;
        color: #ffffff;
    }
    
    /* Cards de Pedidos Compactados */
    .card-pedido {
        background-color: #1e1e1e;
        border-radius: 8px;
        padding: 10px; /* Reduzido de 15px */
        text-align: center;
        box-shadow: 0 3px 8px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s, box-shadow 0.2s;
        margin-bottom: 15px;
        border: 1px solid #2d2d2d;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-pedido:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.5);
        border-color: #0093E9;
    }
    .card-img {
        width: 100%;
        height: 95px; /* Altura otimizada para o efeito de Zoom 67% */
        object-fit: cover;
        border-radius: 5px;
        margin-bottom: 8px;
        background-color: #2d2d2d;
        opacity: 0.85;
    }
    
    /* Botão/Label de Título Compacto */
    .btn-titulo {
        background-color: #ffffff;
        color: #121212 !important;
        font-weight: bold;
        padding: 5px 8px; /* Reduzido para ficar slim */
        border-radius: 4px;
        text-decoration: none;
        display: inline-block;
        margin-bottom: 6px;
        font-size: 12px; /* Fonte reduzida para não quebrar linha */
        width: 100%;
        transition: background-color 0.2s;
    }
    .btn-titulo:hover {
        background-color: #e0e0e0;
    }
    
    /* Horários e Informações Menores */
    .texto-horario {
        font-size: 10.5px;
        color: #cccccc;
        font-weight: 500;
        line-height: 1.3;
    }
    
    /* Seções Inferiores e Divisores Mais Finos */
    .section-title-box {
        background-color: #2d2d2d;
        color: white;
        padding: 5px 10px;
        font-weight: bold;
        border-radius: 4px;
        margin-bottom: 10px;
        font-size: 13px;
        text-align: center;
        border: 1px solid #3d3d3d;
    }
    
    .divider-line {
        border-top: 2px solid #3d3d3d;
        margin: 12px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Geração do Top Banner com Validação da Logo
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
            <span style="font-size: 24px; margin-right: 10px;">🛒</span>
            <div class="banner-title">Gestão Pedidos - Molicenter</div>
        </div>
    """

st.markdown(header_html, unsafe_allow_html=True)

# --- LINKS DAS PLANILHAS REAIS CONFIGURADOS ---
LINKS_PEDIDOS = {
    "folhagem": "https://docs.google.com/spreadsheets/d/1y1mCjctvQTwqvxhk67uYnSX4vs_SROAAa7-kZAz07jg/edit?gid=0#gid=0",
    "flv_normal": "https://docs.google.com/spreadsheets/d/1MROR0Tl__10OI--8-VqZdT5e1il64XSdwW3-xR23Cu8/edit?usp=drive_link",
    "flv_ofertas": "https://docs.google.com/spreadsheets/d/1Ic_iNC34IQTUwZhN0qdf6bsTM-EjwshVnNlwjdnI8mI/edit?usp=drive_link",
    "acougue": "https://docs.google.com/spreadsheets/d/11e0N0FWVdrKtWMG-UroqwPpVKQOqgJ524bBAOuEcyBY/edit?gid=0#gid=0",
    "acougue_pioneiro": "https://docs.google.com/spreadsheets/d/1bBB75w4lshM9Xg70VCuJAzLASpYrp35zYDp8y2vB3Fc/edit?usp=drive_link",
    "pecas_acougue": "https://docs.google.com/spreadsheets/d/19q1qxoLhddZo616gdJFYrj9f4t9TmRCvD3dYhThmUpY/edit?gid=0#gid=0",
    "embalagens": "https://docs.google.com/spreadsheets/d/1x2QjCgvjpBl5-QZAqZCNay7aoUvgohjJoAQFdGn4cfE/edit?gid=0#gid=0",
    "materia_prima": "https://docs.google.com/spreadsheets/d/1WDZBbT1J-aSjGNXFfy9HbhKAmAhU5zquqRHYJUXpR0o/edit?gid=0#gid=0",
    "padaria": "https://docs.google.com/spreadsheets/d/14nfvS6jRIJFdTgPpYDxUZNThLSBM4zASFXl_XnOLJOI/edit?gid=0#gid=0",
    "sugestao_hortifruti": "https://1drv.ms/x/s!Aub4upL5X9DiiMQk_TNnm9D1_s7p6A?e=dQbAKD",
    "sugestao_acougue": "https://1drv.ms/x/s!Aub4upL5X9Diido2H0sInF2k7EArQQ?e=WEfvJU",
}

# --- LINHA 1 DE CARDS ---
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400" class="card-img" alt="Folhagem">
            <a href="{LINKS_PEDIDOS['folhagem']}" target="_blank" class="btn-titulo">Folhagem</a>
            <div class="texto-horario">Seg a Sáb até 12:00hrs</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400" class="card-img" alt="FLV Normal">
            <a href="{LINKS_PEDIDOS['flv_normal']}" target="_blank" class="btn-titulo">FLV Normal</a>
            <div class="texto-horario">
                Ter até 17:00h | Qui até 14:00h
            </div>
            <div style="margin-top: 8px;">
                <a href="{LINKS_PEDIDOS['flv_ofertas']}" target="_blank" class="btn-titulo">FLV Ofertas</a>
                <div class="texto-horario">Qui até 14:00hrs</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1603048588665-791ca8aea617?w=400" class="card-img" alt="Açougue">
            <a href="{LINKS_PEDIDOS['acougue']}" target="_blank" class="btn-titulo">Açougue</a>
            <div class="texto-horario">
                Qua até 15:00hrs<br>
                Sáb até 15:00hrs
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?w=400" class="card-img" alt="Açougue Pioneiro">
            <a href="{LINKS_PEDIDOS['acougue_pioneiro']}" target="_blank" class="btn-titulo" style="font-size: 10.5px;">Açougue - Pioneiro</a>
            <div class="texto-horario">Seg a Sex até 11:00hrs</div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Peças Açougue">
            <a href="{LINKS_PEDIDOS['pecas_acougue']}" target="_blank" class="btn-titulo">Peças Açougue</a>
            <div class="texto-horario">
                Seg/Qua/Sex - Arapongas<br>
                Ter/Qui/Sáb - Maringá
            </div>
        </div>
    """, unsafe_allow_html=True)

# Linha divisória
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)

# --- LINHA 2 DE CARDS (Insumos e Sugestão de Pedidos) ---
col_inf1, col_inf2, col_inf3, col_space, col_inf4 = st.columns([1, 1, 1, 0.1, 1.9])

with col_inf1:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1530587191325-3db32d826c18?w=400" class="card-img" alt="Embalagens">
            <a href="{LINKS_PEDIDOS['embalagens']}" target="_blank" class="btn-titulo">Embalagens</a>
            <div class="texto-horario">Sexta-feira até as 17:30h</div>
        </div>
    """, unsafe_allow_html=True)

with col_inf2:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1574316071802-0d684efa7bf5?w=400" class="card-img" alt="Matéria Prima">
            <a href="{LINKS_PEDIDOS['materia_prima']}" target="_blank" class="btn-titulo">Matéria Prima</a>
            <div class="texto-horario">Até Sábado</div>
        </div>
    """, unsafe_allow_html=True)

with col_inf3:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400" class="card-img" alt="Padaria e Confeitaria">
            <a href="{LINKS_PEDIDOS['padaria']}" target="_blank" class="btn-titulo">Padaria</a>
            <div class="texto-horario">Sábado</div>
        </div>
    """, unsafe_allow_html=True)

# Espaço de separação mínimo
with col_space:
    st.write("")

# Coluna da Direita: Sugestão de Pedidos
with col_inf4:
    st.markdown('<div class="section-title-box">Sugestão de Pedidos</div>', unsafe_allow_html=True)
    sub_col1, sub_col2 = st.columns(2)
    
    with sub_col1:
        st.markdown(f"""
            <div class="card-pedido">
                <img src="https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400" class="card-img" alt="Hortifruti">
                <a href="{LINKS_PEDIDOS['sugestao_hortifruti']}" target="_blank" class="btn-titulo" style="background-color: #0093E9; color: white !important;">Hortifruti</a>
            </div>
        """, unsafe_allow_html=True)
        
    with sub_col2:
        st.markdown(f"""
            <div class="card-pedido">
                <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Açougue">
                <a href="{LINKS_PEDIDOS['sugestao_acougue']}" target="_blank" class="btn-titulo" style="background-color: #0093E9; color: white !important;">Açougue</a>
            </div>
        """, unsafe_allow_html=True)

# Rodapé informativo
st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: #444444; font-size: 11px;">
        Molicenter Supermercados © 2026 - Painel Web de Pedidos Centralizados
    </div>
""", unsafe_allow_html=True)
