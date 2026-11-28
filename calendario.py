import datetime
from zoneinfo import ZoneInfo
import streamlit as st
import streamlit.components.v1 as components
import random

# 1. Configuración básica de la página
st.set_page_config(page_title="Calendario para Lucero", page_icon="🎄", layout="centered")

# 2. Diccionario con todas tus sorpresas ('pendiente': True pinta el botón en gris para orientarte)
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
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
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
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
    },
    12: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
    },
    13: {
        'texto': '''Me encanta estar contigo en cualquier lugar, aunque no nos dejen volver a ese Domino's jajaja''',
        'video': 'Videos/video pizza.mp4',
        'ubicacion': "https://www.google.com/maps/place/Domino's+Pizza/@40.37807,-3.7715649,17z/data=!4m14!1m7!3m6!1s0xd41884f2d8a2a6d:0xce315a1e93f284ad!2sDomino's+Pizza!8m2!3d40.37807!4d-3.76899!16s%2Fg%2F12qhjgqrj!3m5!1s0xd41884f2d8a2a6d:0xce315a1e93f284ad!8m2!3d40.37807!4d-3.76899!16s%2Fg%2F12qhjgqrj?entry=ttu&g_ep=EgoyMDI2MTEyMi4wIKXMDSoASAFQAw%3D%3D"
    },
    14: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
    },
    15: {
        'texto': 'Contigo aprendi a que puede que no salga tan mal en las fotos',
        'foto': 'fotos/foto mia espejo criminal ruso.jpeg'
    },
    16: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
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
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
    },
    20: {
        'texto': 'Me encanta hacer el tonto contigo en cualquier lado',
        'foto': 'fotos/juntos peluches.jpg',
        'ubicacion': 'https://www.google.com/maps/place/Carrefour/@40.3860597,-3.7668085,17z/data=!3m1!5s0xd418840a7c6f483:0x7edf0a3a627f0afc!4m14!1m7!3m6!1s0xd418840a7baa8d9:0xf403be35678f91e7!2sCentro+Comercial+Plaza+Aluche!8m2!3d40.3860597!4d-3.7642336!16s%2Fg%2F11g5z_3d4k!3m5!1s0xd41883f4dcc3eeb:0x3b71e4bf4fa7b564!8m2!3d40.3864338!4d-3.7643726!16s%2Fg%2F11kb0y62tm?entry=ttu&g_ep=EgoyMDI2MTEyMi4wIKXMDSoASAFQAw%3D%3D'
    },
    21: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
    },
    22: {
        'texto': 'Aunque me mientas diciendo que salgo bien en las fotos pero bueno, te quiero mucho igualmente amor',
        'foto': 'fotos/yo real madrid.jpg'
    },
    23: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
    },
    24: {
        'texto': 'Nuestro primer dia juntos',
        'foto': 'fotos/foto juntos espejo 1.jpg',
        'pendiente': True
    }
}

# 3. Configuración de fecha y hora oficial de España (en diciembre cambia MES_OBJETIVO = 12)
ZONA_ES = ZoneInfo("Europe/Madrid")
MES_OBJETIVO = 11
HORA_APERTURA = 20
MINUTO_APERTURA = 11
ahora = datetime.datetime.now(ZONA_ES)

# 4. Memorias de estado: orden y tamaños aleatorios
if 'intro_abierta' not in st.session_state:
    st.session_state['intro_abierta'] = False
if 'dia_abierto' not in st.session_state:
    st.session_state['dia_abierto'] = 0

if 'orden_dias' not in st.session_state:
    dias = list(sorpresas.keys())
    random.shuffle(dias)
    st.session_state['orden_dias'] = dias

if 'alturas_dias' not in st.session_state:
    st.session_state['alturas_dias'] = {
        d: (125 if d == 24 else random.choice([60, 75, 95]))
        for d in sorpresas.keys()
    }

# 5. CSS: Nieve en el fondo (z-index: 0), contenido delante (z-index: 10) y botones grises para días pendientes
st.markdown("""
<style>
.snow-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.main .block-container {
    position: relative;
    z-index: 10;
}

.snowflake {
    position: absolute;
    top: -10%;
    color: rgba(255, 255, 255, 0.75);
    user-select: none;
    animation: caer linear infinite;
}

@keyframes caer {
    0% { transform: translateY(-10vh) rotate(0deg); }
    100% { transform: translateY(110vh) rotate(360deg); }
}

@keyframes brilloDorado {
    0% { box-shadow: 0 0 6px #FFD700; border-color: #FFD700; transform: scale(1); }
    50% { box-shadow: 0 0 22px #FFD700, 0 0 10px #FFF8DC; border-color: #FFF8DC; transform: scale(1.04); }
    100% { box-shadow: 0 0 6px #FFD700; border-color: #FFD700; transform: scale(1); }
}

div.stButton > button {
    position: relative;
    z-index: 15;
    font-weight: bold;
    border-radius: 12px;
    min-height: 60px;
}

div.stButton > button[kind="primary"] {
    border: 2px solid #FFD700 !important;
    animation: brilloDorado 1.8s infinite;
}

/* Estilo gris para botones marcados como pendientes (\u200B invisible al final) */
div.stButton > button:has(p:contains("\u200B")) {
    background-color: #4a4e54 !important;
    color: #b0b5bc !important;
    border: 1px dashed #7a808a !important;
    opacity: 0.75;
}
</style>

<div class="snow-container">
    <div class="snowflake" style="left: 5%; font-size: 18px; animation-duration: 9s; animation-delay: 0s;">❄</div>
    <div class="snowflake" style="left: 15%; font-size: 12px; animation-duration: 12s; animation-delay: 2s;">❅</div>
    <div class="snowflake" style="left: 25%; font-size: 20px; animation-duration: 8s; animation-delay: 4s;">❄</div>
    <div class="snowflake" style="left: 35%; font-size: 14px; animation-duration: 11s; animation-delay: 1s;">❆</div>
    <div class="snowflake" style="left: 48%; font-size: 18px; animation-duration: 10s; animation-delay: 3s;">❄</div>
    <div class="snowflake" style="left: 60%; font-size: 13px; animation-duration: 13s; animation-delay: 0.5s;">❅</div>
    <div class="snowflake" style="left: 72%; font-size: 22px; animation-duration: 9s; animation-delay: 2.5s;">❄</div>
    <div class="snowflake" style="left: 84%; font-size: 15px; animation-duration: 11s; animation-delay: 4.5s;">❆</div>
    <div class="snowflake" style="left: 93%; font-size: 19px; animation-duration: 10s; animation-delay: 1.5s;">❄</div>
</div>
""", unsafe_allow_html=True)

# 6. Título CENTRADO
st.markdown("<h1 style='text-align: center; position: relative; z-index: 10;'>🎄 Calendario para Lucero 🎄</h1>", unsafe_allow_html=True)

# 7. Contador en tiempo real hasta las próximas 20:11
components.html(f"""
<div id="contador" style="text-align:center; color:#FFD700; font-family:sans-serif; font-size:18px; font-weight:bold; padding:8px; background:rgba(0,0,0,0.35); border-radius:10px; border:1px solid #FFD700;">
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
        `⏳ Próxima sorpresa en: ${{h}}h ${{m}}m ${{s}}s`;
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
        st.write("Hola amor, este es el regalo que te queria dar, va a ser un poco tonteria pero bueno, ns si te gustara del todo o que pero bueno, mi regalo es dedicarte a ti mi primera aplicacion en si misma, no va a haber otra primera aplicacion y mejor porque como tú no hay dos. Como tu no hay dos porque eres lo primero que pienso al despertarme y lo ultimo que pienso al acostarme, me encantaria poder verte todos los días pero bueno, el destino nos ha separado pero por suerte tu cierto 12 de septiembre de este año a las 20:11 decidiste escribirme")
        st.image('fotos/foto conversa.jpg', use_column_width=True)
        st.write('Eramos dos chavales (tu más que yo la verdad), aun lo somos pero ahora hemos aprendido un poco más el uno del otro y cada vez que se más de ti me gustas más, de verdad, estoy super orgulloso de ti, de que a pesar de todo sigues adelante, eres muy fuerte y que sigas adelante y tengas la razon de la mayorias de mis sonrisas en el día, mi mejor pensamiento y siempre estas en mis mejores momentos de la semana siempre y TE AMO A TI RIZOS, a ti y solo a ti, me vuelves lokito, muy lokito.')
        st.write('Creo que todos estn hartos de que hable tanto de ti la verdad, te quiero mucho de verdad y seguro qeu vas a lograr todo lo que te propongas en la vida y vas a poder seguir adelante, yo voy a estar ahi para ti siempre.')
        st.write('Este calendario la idea es que cada día te vas a encontrar una sorpresa distinta, a ver si te gustan y que sepas que estoy orgulloso de la persona en la que te has covertido, un beso a ti, a Doña Ruth, Don Jesusito y la Torre chulilla jajaja')
        st.image("fotos/foto juntos espejo 1.jpg", use_column_width=True)

        if st.button("❌ Cerrar introducción", use_container_width=True):
            st.session_state['intro_abierta'] = False
            st.rerun()

# 9. Tarjeta superior cuando Lucero pulsa un día del calendario
if st.session_state['dia_abierto'] != 0:
    dia_actual = st.session_state['dia_abierto']
    regalo = sorpresas[dia_actual]
    momento_apertura = datetime.datetime(ahora.year, MES_OBJETIVO, dia_actual, HORA_APERTURA, MINUTO_APERTURA, tzinfo=ZONA_ES)

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

# 10. Cuadrícula de 4 columnas con tamaños variados, el 24 destacado y grises en los pendientes
columnas = st.columns(4, gap='large')

for i, dia in enumerate(st.session_state['orden_dias']):
    regalo_dia = sorpresas[dia]
    es_pendiente = regalo_dia.get('pendiente', False)
    es_hoy = (ahora.month == MES_OBJETIVO and ahora.day == dia)
    tipo_boton = "primary" if (es_hoy and not es_pendiente) else "secondary"

    # Añadimos el carácter invisible \u200B si el día está pendiente para que el CSS lo pinte en gris
    marca_gris = "\u200B" if es_pendiente else ""

    altura = st.session_state['alturas_dias'][dia]
    if dia == 24:
        etiqueta = f"🎄\n\nDÍA 24\n\n🎄{marca_gris}"
    elif altura == 95:
        etiqueta = f"\nDía {dia}\n\n{marca_gris}"
    elif altura == 75:
        etiqueta = f"\nDía {dia}\n{marca_gris}"
    else:
        etiqueta = f"Día {dia}{marca_gris}"

    with columnas[i % 4]:
        if st.button(etiqueta, key=f"btn_dia_{dia}", type=tipo_boton, use_container_width=True):
            st.session_state['dia_abierto'] = dia
            st.rerun()