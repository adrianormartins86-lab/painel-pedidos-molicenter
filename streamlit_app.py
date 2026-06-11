import streamlit as st
import base64
import os

# ─────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Gestão Pedidos - Molicenter",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# UTILITÁRIOS
# ─────────────────────────────────────────────
def get_base64_image(image_path: str, fallback_path: str = "") -> str:
    """Converte imagem local para Base64. Tenta fallback se o principal não existir."""
    for path in [image_path, fallback_path]:
        if path and os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return ""

def img_tag(base64_str: str, mime: str, url_fallback: str, alt: str, css_class: str) -> str:
    """Retorna tag <img> usando base64 local ou URL remota como fallback."""
    if base64_str:
        return f'<img src="data:{mime};base64,{base64_str}" class="{css_class}" alt="{alt}">'
    if url_fallback:
        return f'<img src="{url_fallback}" class="{css_class}" alt="{alt}">'
    return f'<div class="{css_class} img-placeholder">📦</div>'

# ─────────────────────────────────────────────
# IMAGENS LOCAIS
# ─────────────────────────────────────────────
logo_b64           = get_base64_image("passaro_logo.png")
embalagens_b64     = get_base64_image("Embalagens.jpg")
materiaprima_b64   = get_base64_image("materiaprima.jpg")
pioneiros_b64      = get_base64_image("Pioneiros.jpg")

# ─────────────────────────────────────────────
# DADOS DOS CARDS  ← único lugar para editar
# ─────────────────────────────────────────────
# Cada card é um dict:
#   title, link, schedule (lista de strings), img_b64, img_mime, img_url, sub_cards
# sub_cards: lista de dicts com title, link, schedule
CARDS_ROW1 = [
    {
        "title": "Folhagem",
        "link": "https://pedidos-folhagem.streamlit.app/",
        "schedule": ["Seg a Sáb até 12:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1574316071802-0d684efa7bf5?w=400",
        "sub_cards": []
    },
    {
        "title": "FLV Normal",
        "link": "https://pedidos-flv.streamlit.app/",
        "schedule": ["Terças-feira até 17:00hrs", "Quintas-feira até 14:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400",
        "sub_cards": [
            {
                "title": "FLV Ofertas",
                "link": "https://pedidos-flv-ofertas.streamlit.app/",
                "schedule": ["Quintas-feira até 14:00hrs"]
            },
            {
                "title": "FLV Oriental",
                "link": "https://pedido-oriental.streamlit.app/",
                "schedule": ["Quintas-feira até 14:00hrs"]
            },
        ]
    },
    {
        "title": "Açougue Adriano",
        "link": "https://acougue-total.streamlit.app/",
        "schedule": ["Quartas-feira até 15:00hrs", "Sábado até 15:00hrs"],
        "img_b64": "", "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400",
        "sub_cards": [
            {
                "title": "Peças Açougue",
                "link": "https://acougue-pecas.streamlit.app/",
                "schedule": [
                    "Seg / Qua / Sex — Arapongas até 15:00h",
                    "Ter / Qui / Sáb — Maringá até 15:00h"
                ]
            }
        ]
    },
    {
        "title": "Pioneiro + BF + Paraná",
        "link": "https://acougue-especiais.streamlit.app/",
        "schedule": ["Seg a Sex até 11:00hrs"],
        "img_b64": pioneiros_b64, "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1578916171728-46686eac8d58?w=400",
        "sub_cards": []
    },
]

CARDS_ROW2 = [
    {
        "title": "Embalagens",
        "link": "https://docs.google.com/spreadsheets/d/1x2QjCgvjpBl5-QZAqZCNay7aoUvgohjJoAQFdGn4cfE/edit?gid=0#gid=0",
        "schedule": ["Sexta-feira até as 17:30hrs"],
        "img_b64": embalagens_b64, "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=400",
        "sub_cards": []
    },
    {
        "title": "Matéria Prima",
        "link": "https://docs.google.com/spreadsheets/d/1WDZBbT1J-aSjGNXFfy9HbhKAmAhU5zquqRHYJUXpR0o/edit?gid=0#gid=0",
        "schedule": ["Até Sábado"],
        "img_b64": materiaprima_b64, "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1556909114-44e3e70034e2?w=400",
        "sub_cards": []
    },
    {
        "title": "Padaria e Confeitaria",
        "link": "https://docs.google.com/spreadsheets/d/14nfvS6jRIJFdTgPpYDxUZNThLSBM4zASFXl_XnOLJOI/edit?gid=0#gid=0",
        "schedule": ["Sábado"],
        "img_b64": "", "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=400",
        "sub_cards": []
    },
]

CARDS_SUGESTOES = [
    {
        "title": "Hortifruti",
        "link": "https://1drv.ms/x/s!Aub4upL5X9DiiMQk_TNnm9D1_s7p6A?e=dQbAKD",
        "schedule": [],
        "img_b64": "", "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1610348725531-843dff563e2c?w=400",
        "sub_cards": []
    },
    {
        "title": "Açougue",
        "link": "https://1drv.ms/x/c/e2d05ff992baf8e6/IQDm-LqS-V_QIIDiA3ICAAAAAf91damk1P4zL0WOZQMb5ys?e=AhVL9h",
        "schedule": [],
        "img_b64": "", "img_mime": "image/jpeg",
        "img_url": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400",
        "sub_cards": []
    },
]

# ─────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
/* ── Base ── */
.stApp, .main, .reportview-container {
    background-color: #0f0f0f !important;
    color: #ffffff !important;
}

/* ── Banner ── */
.banner-container {
    background: linear-gradient(90deg, #0B3C5D 0%, #07263b 100%);
    padding: 12px 20px;
    border-radius: 10px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 4px 16px rgba(0,0,0,.55);
    border: 1px solid #0e4a74;
}
.banner-logo {
    height: 42px;
    width: auto;
    object-fit: contain;
    flex-shrink: 0;
}
.banner-title {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #fff;
    white-space: nowrap;
}

/* ── Card ── */
.card-pedido {
    background-color: #1a1a1a;
    border-radius: 12px;
    padding: 14px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,.45);
    transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
    margin-bottom: 20px;
    border: 1px solid #2a2a2a;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.card-pedido:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 24px rgba(0,0,0,.65);
    border-color: #0093E9;
}

/* ── Card image ── */
.card-img {
    width: 100%;
    height: 130px;
    object-fit: cover;
    border-radius: 7px;
    background-color: #2a2a2a;
}
.img-placeholder {
    width: 100%;
    height: 130px;
    border-radius: 7px;
    background-color: #2a2a2a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 36px;
}

/* ── Sub-card (cards dentro de card) ── */
.sub-card {
    background-color: #242424;
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #333;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

/* ── Botão principal ── */
.btn-titulo {
    background-color: #ffffff;
    color: #111111 !important;
    font-weight: 700;
    padding: 7px 10px;
    border-radius: 5px;
    text-decoration: none;
    display: block;
    font-size: 13px;
    transition: background-color .18s, color .18s;
    width: 100%;
    box-sizing: border-box;
}
.btn-titulo:hover {
    background-color: #d4ecff;
    color: #0B3C5D !important;
    text-decoration: none;
}

/* ── Horários ── */
.texto-horario {
    font-size: 11.5px;
    color: #aaaaaa;
    line-height: 1.5;
}

/* ── Seção sugestões ── */
.section-title-box {
    background: linear-gradient(90deg, #0B3C5D, #07263b);
    color: #fff;
    padding: 9px 16px;
    font-weight: 700;
    border-radius: 7px;
    margin-bottom: 16px;
    font-size: 15px;
    text-align: center;
    border: 1px solid #0e4a74;
    box-shadow: 0 4px 10px rgba(0,0,0,.3);
}

/* ── Divider ── */
.divider-line {
    border: none;
    border-top: 1px solid #2a2a2a;
    margin: 20px 0;
}

/* ── Responsividade mobile ── */
@media (max-width: 768px) {
    .banner-title { font-size: 16px; }
    .card-img     { height: 100px; }
    .btn-titulo   { font-size: 12px; }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FUNÇÕES DE RENDERIZAÇÃO
# ─────────────────────────────────────────────
def render_schedule(schedule: list[str]) -> str:
    return "<br>".join(schedule) if schedule else ""

def render_sub_card(sc: dict) -> str:
    sched_html = f'<div class="texto-horario">{render_schedule(sc["schedule"])}</div>' if sc.get("schedule") else ""
    return f"""
    <div class="sub-card">
        <a href="{sc['link']}" target="_blank" class="btn-titulo">{sc['title']}</a>
        {sched_html}
    </div>
    """

def render_card(card: dict) -> str:
    img_html = img_tag(
        card.get("img_b64", ""),
        card.get("img_mime", "image/jpeg"),
        card.get("img_url", ""),
        card["title"],
        "card-img"
    )
    sched_html = (
        f'<div class="texto-horario">{render_schedule(card["schedule"])}</div>'
        if card.get("schedule") else ""
    )
    sub_html = "".join(render_sub_card(sc) for sc in card.get("sub_cards", []))

    return f"""
    <div class="card-pedido">
        {img_html}
        <a href="{card['link']}" target="_blank" class="btn-titulo">{card['title']}</a>
        {sched_html}
        {sub_html}
    </div>
    """

# ─────────────────────────────────────────────
# BANNER
# ─────────────────────────────────────────────
if logo_b64:
    logo_src = f'<img src="data:image/png;base64,{logo_b64}" class="banner-logo" alt="Logo Molicenter">'
else:
    logo_src = '<span style="font-size:28px">🛒</span>'

st.markdown(f"""
<div class="banner-container">
    {logo_src}
    <div class="banner-title">Gestão Pedidos - Molicenter</div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LINHA 1  (4 colunas)
# ─────────────────────────────────────────────
cols1 = st.columns(4)
for col, card in zip(cols1, CARDS_ROW1):
    with col:
        st.markdown(render_card(card), unsafe_allow_html=True)

st.markdown('<hr class="divider-line">', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LINHA 2  (3 colunas)
# ─────────────────────────────────────────────
cols2 = st.columns(3)
for col, card in zip(cols2, CARDS_ROW2):
    with col:
        st.markdown(render_card(card), unsafe_allow_html=True)

st.markdown('<hr class="divider-line">', unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SEÇÃO SUGESTÕES
# ─────────────────────────────────────────────
_, col_center, _ = st.columns([0.5, 3, 0.5])
with col_center:
    st.markdown('<div class="section-title-box">📋 Sugestão de Pedidos</div>', unsafe_allow_html=True)
    sub_cols = st.columns(len(CARDS_SUGESTOES))
    for col, card in zip(sub_cols, CARDS_SUGESTOES):
        with col:
            st.markdown(render_card(card), unsafe_allow_html=True)

# ─────────────────────────────────────────────
# RODAPÉ
# ─────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#ffffff; font-size:11px;">
    Molicenter Supermercados © 2026 — Painel Web de Pedidos Centralizados
</div>
""", unsafe_allow_html=True)
