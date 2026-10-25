import discord
from discord.ext import commands
import requests
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def ayuda(ctx):
    texto = (
        "🛡️ **Bot de prevención de estafas**\n\n"
        "Este bot está diseñado para ayudar a los usuarios a prevenir estafas y proteger su información personal. "
        "Puedes hacer preguntas sobre cómo evitar estafas, proteger tu cuenta y reconocer llamadas falsas.\n\n"
        "Para hacer una pregunta, utiliza el siguiente formato:\n"
        "$preguntar EDAD PREGUNTA\n\n"
        "Ejemplos:\n"
        "$preguntar 10 como evitar estafas\n"
        "$preguntar 30 como proteger mi cuenta\n"
        "$preguntar 70 como reconocer llamadas falsas"
    )

    await ctx.send(texto)

@bot.command()
async def preguntar(ctx, edad: int, *, pregunta: str):
    pregunta = pregunta.lower()

    if edad < 1 or edad > 120:
        await ctx.send("Por favor, introduce una edad válida entre 1 y 120.")
        return

    if edad < 18:
        publico = "niños"
    elif edad < 60:
        publico = "adultos"
    else:
        publico = "adultos mayores"

    if "estafa" in pregunta or "engaño" in pregunta:
        if edad < 18:
            respuesta = (
                "Una estafa es un engaño para quitarte algo, "
                "como tu cuenta de un videojuego.\n"
                "No confíes en premios gratis y pide ayuda a un adulto."
            )
        elif edad < 60:
            respuesta = (
                "Las estafas buscan engañarte para obtener dinero "
                "o información personal. Verifica quién te contacta, "
                "no compartas códigos y desconfía de las ofertas urgentes."
            )
        else:
            respuesta = (
                "Algunas estafas usan llamadas, mensajes o premios "
                "falsos para conseguir dinero o datos personales. "
                "No tomes decisiones apresuradas y confirma la información "
                "llamando al número oficial de la entidad."
            )

    elif "contraseña" in pregunta or "cuenta" in pregunta:
        respuesta = (
            "🔐 Protege tu cuenta con una contraseña única y difícil "
            "de adivinar. Activa la autenticación en dos pasos y nunca "
            "compartas contraseñas ni códigos de verificación."
        )

        if edad < 18:
            respuesta = (
                "No compartas tu contraseña con desconocidos, "
                "ni siquiera si prometen regalarte monedas o premios "
                "en un videojuego. Pide ayuda a un adulto de confianza."
            )

    elif "enlace" in pregunta or "link" in pregunta:
        respuesta = (
            "🔗 No abras enlaces sospechosos. Comprueba cuidadosamente "
            "el dominio y entra a la página oficial escribiendo su "
            "dirección en el navegador. Un candado HTTPS no garantiza "
            "que una página sea segura."
        )

        if edad < 18:
            respuesta = (
                "🔗 Si alguien te envía un enlace para ganar premios "
                "o conseguir objetos gratis, no lo abras sin consultar "
                "a un adulto de confianza."
            )

    elif "premio" in pregunta or "regalo" in pregunta:
        respuesta = (
            "Desconfía de los premios que exigen pagar, compartir "
            "contraseñas o entregar códigos para reclamarlos. "
            "Comprueba la promoción en la página oficial."
        )

    elif "llamada" in pregunta or "teléfono" in pregunta:
        respuesta = (
            "Si alguien te llama diciendo que es del banco o de "
            "una entidad oficial, no compartas códigos, contraseñas "
            "ni datos bancarios. Cuelga y llama al número oficial."
        )

    elif "compra" in pregunta or "tienda" in pregunta:
        respuesta = (
            "🛒 Antes de comprar, revisa la reputación de la tienda, "
            "sus datos de contacto y las opiniones independientes. "
            "Desconfía de precios demasiado bajos y evita pagos "
            "difíciles de recuperar."
        )

    elif "caso real" in pregunta or "ejemplo" in pregunta:
        respuesta = (
            "Ejemplo de estafa: una persona recibe un mensaje que "
            "afirma que ganó un premio y le pide pagar una tarifa "
            "o entregar su contraseña. Si lo hace, puede perder dinero "
            "o su cuenta. La señal de alerta es que le exijan datos "
            "secretos o dinero para recibir el supuesto premio."
        )

    elif "consejo" in pregunta or "recomendación" in pregunta:
        respuesta = (
            "Recomendaciones:\n"
            "1. No compartas contraseñas ni códigos.\n"
            "2. Verifica los mensajes con la fuente oficial.\n"
            "3. No abras enlaces sospechosos.\n"
            "4. Activa la autenticación en dos pasos.\n"
            "5. Reporta los mensajes fraudulentos."
        )

    else:
        respuesta = (
            "Puedo ayudarte con estafas, contraseñas, enlaces, "
            "premios falsos, llamadas sospechosas y compras seguras. "
            "Escribe $ayuda para ver ejemplos."
        )

    await ctx.send(
        "Público: " + publico + "\n\n" + respuesta
    )

    
bot.run("TOKEN")