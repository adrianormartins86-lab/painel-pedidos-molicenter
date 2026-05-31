
import streamlit as st

# Configuração da página para layout amplo (wide)
st.set_page_config(
    page_title="Gestão Pedidos - Molicenter",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização CSS customizada para replicar o visual profissional e limpo
st.markdown("""
    <style>
    /* Reset e Background */
    .reportview-container, .main {
        background-color: #f8f9fa;
    }
    
    /* Banner Principal */
    .banner-container {
        background: linear-gradient(90deg, #0093E9 0%, #80D0C7 100%);
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 30px;
        color: white;
        display: flex;
        align-items: center;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }
    .banner-title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 28px;
        font-weight: bold;
        margin-left: 15px;
    }
    
    /* Grid e Cards de Pedidos */
    .card-pedido {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform 0.2s, box-shadow 0.2s;
        margin-bottom: 25px;
        border: 1px solid #eef2f5;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-pedido:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    .card-img {
        width: 100%;
        height: 140px;
        object-fit: cover;
        border-radius: 6px;
        margin-bottom: 15px;
        background-color: #f1f3f5;
    }
    
    /* Botão/Label de Título */
    .btn-titulo {
        background-color: #000000;
        color: #ffffff !important;
        font-weight: bold;
        padding: 8px 12px;
        border-radius: 4px;
        text-decoration: none;
        display: inline-block;
        margin-bottom: 10px;
        font-size: 14px;
        width: 100%;
        transition: background-color 0.2s;
    }
    .btn-titulo:hover {
        background-color: #212529;
    }
    
    /* Horários e Informações */
    .texto-horario {
        font-size: 12px;
        color: #495057;
        font-weight: 500;
        line-height: 1.4;
    }
    
    /* Seções Inferiores e Divisores */
    .section-title-box {
        background-color: #495057;
        color: white;
        padding: 8px 15px;
        font-weight: bold;
        border-radius: 4px;
        margin-bottom: 15px;
        font-size: 15px;
        text-align: center;
    }
    
    .divider-line {
        border-top: 3px solid #000000;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Top Banner (Header)
st.markdown("""
    <div class="banner-container">
        <span style="font-size: 32px;">🛒</span>
        <div class="banner-title">Gestão Pedidos - Molicenter</div>
    </div>
""", unsafe_allow_html=True)

# --- LINKS DAS PLANILHAS (Substitua pelos seus links reais do Google Sheets) ---
LINKS_PEDIDOS = {
    "folhagem": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "flv_normal": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "flv_ofertas": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "acougue": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "acougue_pioneiro": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "pecas_acougue": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "embalagens": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "materia_prima": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "padaria": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "sugestao_hortifruti": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
    "sugestao_acougue": "https://docs.google.com/spreadsheets/d/seu_id_aqui/edit",
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
                Terças-feira até 17:00hrs<br>
                Quintas-feira até 14:00hrs
            </div>
            <div style="margin-top: 15px;">
                <a href="{LINKS_PEDIDOS['flv_ofertas']}" target="_blank" class="btn-titulo">FLV Ofertas</a>
                <div class="texto-horario">Quintas-feira até 14:00hrs</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1603048588665-791ca8aea617?w=400" class="card-img" alt="Açougue">
            <a href="{LINKS_PEDIDOS['acougue']}" target="_blank" class="btn-titulo">Açougue</a>
            <div class="texto-horario">
                Quartas-feira até 15:00hrs<br>
                Sábado até 15:00hrs
            </div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1516467508483-a7212febe31a?w=400" class="card-img" alt="Açougue Pioneiro">
            <a href="{LINKS_PEDIDOS['acougue_pioneiro']}" target="_blank" class="btn-titulo" style="font-size: 12px;">Açougue - Pioneiro + Big Frango</a>
            <div class="texto-horario">Seg a Sex até 11:00hrs</div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Peças Açougue">
            <a href="{LINKS_PEDIDOS['pecas_acougue']}" target="_blank" class="btn-titulo">Peças Açougue</a>
            <div class="texto-horario">
                Seg / Qua e Sex - Arapongas até as 15:00hrs<br>
                Ter / Qui e Sáb - Maringá até as 15:00hrs
            </div>
        </div>
    """, unsafe_allow_html=True)


# Linha divisória preta idêntica ao layout original
st.markdown('<div class="divider-line"></div>', unsafe_allow_html=True)


# --- LINHA 2 DE CARDS (Insumos e Sugestão de Pedidos) ---
col_inf1, col_inf2, col_inf3, col_space, col_inf4 = st.columns([1, 1, 1, 0.2, 1.8])

with col_inf1:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1530587191325-3db32d826c18?w=400" class="card-img" alt="Embalagens">
            <a href="{LINKS_PEDIDOS['embalagens']}" target="_blank" class="btn-titulo">Embalagens</a>
        </div>
    """, unsafe_allow_html=True)

with col_inf2:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1574316071802-0d684efa7bf5?w=400" class="card-img" alt="Matéria Prima">
            <a href="{LINKS_PEDIDOS['materia_prima']}" target="_blank" class="btn-titulo">Matéria Prima</a>
        </div>
    """, unsafe_allow_html=True)

with col_inf3:
    st.markdown(f"""
        <div class="card-pedido">
            <img src="https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400" class="card-img" alt="Padaria e Confeitaria">
            <a href="{LINKS_PEDIDOS['padaria']}" target="_blank" class="btn-titulo">Padaria e Confeitaria</a>
        </div>
    """, unsafe_allow_html=True)

# Espaço vazio simulando o layout original
with col_space:
    st.write("")

# Coluna da Direita: Sugestão de Pedidos (Mais larga, contendo 2 sub-cards side-by-side)
with col_inf4:
    st.markdown('<div class="section-title-box">Sugestão de Pedidos</div>', unsafe_allow_html=True)
    sub_col1, sub_col2 = st.columns(2)
    
    with sub_col1:
        st.markdown(f"""
            <div class="card-pedido">
                <img src="https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400" class="card-img" alt="Hortifruti">
                <a href="{LINKS_PEDIDOS['sugestao_hortifruti']}" target="_blank" class="btn-titulo" style="background-color: #17a2b8;">Hortifruti</a>
            </div>
        """, unsafe_allow_html=True)
        
    with sub_col2:
        st.markdown(f"""
            <div class="card-pedido">
                <img src="https://images.unsplash.com/photo-1544025162-d76694265947?w=400" class="card-img" alt="Açougue">
                <a href="{LINKS_PEDIDOS['sugestao_acougue']}" target="_blank" class="btn-titulo" style="background-color: #17a2b8;">Açougue</a>
            </div>
        """, unsafe_allow_html=True)

# Rodapé informativo
st.markdown("""
    <div style="text-align: center; margin-top: 50px; color: #a0aec0; font-size: 12px;">
        Molicenter Supermercados © 2026 - Painel Web de Pedidos Centralizados
    </div>
""", unsafe_allow_html=True)
