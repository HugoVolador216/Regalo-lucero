import datetime
import streamlit as st
import streamlit.components.v1 as components
import random

# 1. Configuración básica de la página
st.set_page_config(page_title="Calendario para Lucero", page_icon="🎄")

# 2. Diccionario con todas tus sorpresas
sorpresas = {
    1: {
        'texto': 'Cuando te digo que te quiero me refiero a él',
        'foto': 'fotos/f,y,peque con camisa azul.jpg'
    },
    2: {
        'texto': 'Aunque tambien a él tambien',
        'foto': 'fotos/cezon.jpg'
    },
    3: {
        'texto': 'Cuando te miro veo a este bellezon',
        'foto': 'fotos/ella dormida.jpg'
    },
    4: {
        'texto': 'Eres la persona con la que no me importa hacer cosas asi: ',
        'foto': 'fotos/beso garaje.jpg'
    },
    5: {
        'texto': 'Y me encanta hacer cosas asi tambien:',
        'foto': 'fotos/juntos parque ft.jpeg'
    },
    6: {
        'texto': 'No se cuantos besos nos quedaran pero espero que sean todos los que tengamos y algunos más',
        'video': 'Videos/videos besos 1 (1).mp4'
    },
    7: {
        'texto': 'Tampoco cuantas tonterias nos quedaran',
        'video': 'Videos/Videos tonterias nuestras.mp4'
    },
    8: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    9: {
        'texto': 'Gracias por aguantar mis tonterias como esta',
        'foto': 'fotos/yo calvo.jpg'
    },
    10: {
        'texto': 'Me encanta cuando me besas, de verdad, te quiero mucho por todo',
        'video': 'Videos/videos besos 3.mp4'
    },
    11: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    12: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    13: {
        'texto': '''Me encanta estar contigo en cualquier lugar, aunque no nos dejen volver a ese Domino's jajaja''',
        'video': 'Videos/video pizza.mp4',
        'ubicacion': "https://www.google.com/maps/place/Domino's+Pizza/@40.37807,-3.7715649,17z/data=!4m14!1m7!3m6!1s0xd41884f2d8a2a6d:0xce315a1e93f284ad!2sDomino's+Pizza!8m2!3d40.37807!4d-3.76899!16s%2Fg%2F12qhjgqrj!3m5!1s0xd41884f2d8a2a6d:0xce315a1e93f284ad!8m2!3d40.37807!4d-3.76899!16s%2Fg%2F12qhjgqrj?entry=ttu&g_ep=EgoyMDI2MTEyMi4wIKXMDSoASAFQAw%3D%3D"
    },
    14: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    15: {
        'texto': 'Contigo aprendi a que puede que no salga tan mal en las fotos',
        'foto': 'fotos/foto mia espejo criminal ruso.jpeg'
    },
    16: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    17: {
        'texto': 'Aunque llevamos juntos solo 3 meses y 5 días me encanta estar contigo',
        'video': 'Videos/videos besos 2.mp4'
    },
    18: {
        'texto': 'Y me encanta sacarme fotos contigo aunque no me dejes subir todas',
        'foto': 'fotos/foto juntos espejo 1.jpg'
    },
    19: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    20: {
        'texto': 'Me encanta hacer el tonto contigo en cualquier lado',
        'foto': 'fotos/juntos peluches.jpg',
        'ubicacion': 'https://www.google.com/maps/place/Carrefour/@40.3860597,-3.7668085,17z/data=!3m1!5s0xd418840a7c6f483:0x7edf0a3a627f0afc!4m14!1m7!3m6!1s0xd418840a7baa8d9:0xf403be35678f91e7!2sCentro+Comercial+Plaza+Aluche!8m2!3d40.3860597!4d-3.7642336!16s%2Fg%2F11g5z_3d4k!3m5!1s0xd41883f4dcc3eeb:0x3b71e4bf4fa7b564!8m2!3d40.3864338!4d-3.7643726!16s%2Fg%2F11kb0y62tm?entry=ttu&g_ep=EgoyMDI2MTEyMi4wIKXMDSoASAFQAw%3D%3D'
    },
    21: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    22: {
        'texto': 'Aunque me mientas diciendo que salgo bien en las fotos pero bueno, te quiero mucho igualmente amor',
        'foto': 'fotos/yo real madrid.jpg'
    },
    23: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    },
    24: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/descarga.jpg'
    }
}

# 3. Configuración de fecha y hora (en diciembre cambia MES_OBJETIVO = 12)
MES_OBJETIVO = 11
HORA_APERTURA = 20
MINUTO_APERTURA = 11
ahora = datetime.datetime.now()

# 4. Memorias de estado: orden, tamaños aleatorios y qué tarjeta está abierta
if 'intro_abierta' not in st.session_state:
    st.session_state['intro_abierta'] = False
if 'dia_abierto' not in st.session_state:
    st.session_state['dia_abierto'] = 0

if 'orden_dias' not in st.session_state:
    dias = list(sorpresas.keys())
    random.shuffle(dias)
    st.session_state['orden_dias'] = dias

# Asignamos alturas aleatorias una sola vez (el 24 siempre será el más grande: 125px)
if 'alturas_dias' not in st.session_state:
    alturas = {}
    for d in sorpresas.keys():
        if d == 24:
            alturas[d] = 125
        else:
            alturas[d] = random.choice([60, 75, 95])
    st.session_state['alturas_dias'] = alturas

# 5. Estilos CSS dinámicos (brillo dorado + alturas personalizadas por botón)
css_botones = ""
for d, altura in st.session_state['alturas_dias'].items():
    tamaño_letra = "24px" if d == 24 else "18px"
    borde_extra = "border: 2px solid #FFD700;" if d == 24 else ""
    css_botones += f"""
    div.stButton > button:has(p:contains("Día {d}")),
    button[kind="secondary"]:has(p:contains("Día {d}")),
    button[kind="primary"]:has(p:contains("Día {d}")) {{
        height: {altura}px;
        font-size: {tamaño_letra};
        {borde_extra}
    }}
    """

st.markdown(f"""
<style>
@keyframes brilloDorado {{
    0% {{ box-shadow: 0 0 6px #FFD700; border-color: #FFD700; transform: scale(1); }}
    50% {{ box-shadow: 0 0 22px #FFD700, 0 0 10px #FFF8DC; border-color: #FFF8DC; transform: scale(1.04); }}
    100% {{ box-shadow: 0 0 6px #FFD700; border-color: #FFD700; transform: scale(1); }}
}}

div.stButton > button {{
    font-weight: bold;
    border-radius: 12px;
    min-height: 60px;
}}

div.stButton > button[kind="primary"] {{
    border: 2px solid #FFD700 !important;
    animation: brilloDorado 1.8s infinite;
}}
</style>
""", unsafe_allow_html=True)

# 6. Título CENTRADO y efecto nieve
st.markdown("<h1 style='text-align: center;'>🎄 Calendario para Lucero 🎄</h1>", unsafe_allow_html=True)
st.snow()

# 7. Contador en tiempo real hasta las próximas 20:11
components.html(f"""
<div id="contador" style="text-align:center; color:#FFD700; font-family:sans-serif; font-size:18px; font-weight:bold; padding:8px; background:rgba(0,0,0,0.25); border-radius:10px; border:1px solid #FFD700;">
    Calculando tiempo para las 20:11...
</div>
<script>
function actualizarContador() {{
    const ahora = new Date();
    let objetivo = new Date();
    objetivo.setHours({HORA_APERTURA}, {MINUTO_APERTURA}, 0, 0);
    if (ahora >= objetivo) {{
        objetivo.setDate(objetivo.getDate() + 1);
    }}
    const diff = objetivo - ahora;
    const h = Math.floor(diff / (1000 * 60 * 60));
    const m = Math.floor((diff / (1000 * 60)) % 60);
    const s = Math.floor((diff / 1000) % 60);
    document.getElementById("contador").innerHTML =
        `⏳ Próxima sorpresa a las 20:11 en: ${{h}}h ${{m}}m ${{s}}s`;
}}
setInterval(actualizarContador, 1000);
actualizarContador();
</script>
""", height=55)

# 8. Botón y tarjeta de Introducción arriba del todo
if st.button("💌 Lee esto primero", use_container_width=True):
    st.session_state['intro_abierta'] = True
    st.rerun()

if st.session_state['intro_abierta']:
    with st.container(border=True):
        st.subheader("💌 Para ti, Lucero")
        st.write("Escribe aquí tu texto de introducción antes de que empiece a abrir los días...")
        st.image("fotos/foto juntos espejo 1.jpg", use_column_width=True)

        if st.button("❌ Cerrar introducción", use_container_width=True):
            st.session_state['intro_abierta'] = False
            st.rerun()

# 9. Tarjeta superior cuando Lucero pulsa un día del calendario
if st.session_state['dia_abierto'] != 0:
    dia_actual = st.session_state['dia_abierto']
    regalo = sorpresas[dia_actual]
    momento_apertura = datetime.datetime(ahora.year, MES_OBJETIVO, dia_actual, HORA_APERTURA, MINUTO_APERTURA)

    with st.container(border=True):
        st.subheader(f"🎁 Día {dia_actual}")

        if ahora >= momento_apertura:
            if 'texto' in regalo:
                st.write(regalo['texto'])
            if 'foto' in regalo:
                st.image(regalo['foto'], use_column_width=True)
            if 'video' in regalo:
                st.video(regalo['video'])
            if 'audio' in regalo:
                st.audio(regalo['audio'])
            if 'ubicacion' in regalo:
                st.link_button('📍 Ver ubicación en el mapa', regalo['ubicacion'])
        else:
            st.warning(f'Aún no es día {dia_actual} a las 20:11 🎅')

        if st.button("❌ Cerrar sorpresa", use_container_width=True):
            st.session_state['dia_abierto'] = 0
            st.rerun()

# 10. Cuadrícula de 4 columnas con tamaños variados y el 24 destacado
columnas = st.columns(4, gap='large')

for i, dia in enumerate(st.session_state['orden_dias']):
    es_hoy = (ahora.month == MES_OBJETIVO and ahora.day == dia)
    tipo_boton = "primary" if es_hoy else "secondary"

    # Añadimos saltos de línea invisibles según la altura aleatoria para variar el tamaño de forma 100% compatible
    altura = st.session_state['alturas_dias'][dia]
    if dia == 24:
        etiqueta = f"🎄\n\nDÍA 24\n\n🎄"
    elif altura == 95:
        etiqueta = f"\nDía {dia}\n\n"
    elif altura == 75:
        etiqueta = f"\nDía {dia}\n"
    else:
        etiqueta = f"Día {dia}"

    with columnas[i % 4]:
        if st.button(etiqueta, type=tipo_boton, use_container_width=True):
            st.session_state['dia_abierto'] = dia
            st.rerun()