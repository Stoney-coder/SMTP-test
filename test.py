import smtplib
from email.message import EmailMessage

# Configura tus credenciales aquí
SENDER_EMAIL = "andres.osorio_garzon@boehringer-ingelheim.com"
SENDER_PASSWORD = "Libna197169*"

# Dirección del destinatario (puedes dejar esta fija para la prueba)
TO_EMAIL = "andres.osorio_garzon@boehringer-ingelheim.com"

def send_test_email():
    msg = EmailMessage()
    msg["Subject"] = "Prueba de conexión SMTP desde Streamlit"
    msg["From"] = SENDER_EMAIL
    msg["To"] = TO_EMAIL
    msg.set_content("Hola Andrés,\n\nEste es un correo de prueba enviado desde una aplicación Streamlit usando el servidor SMTP corporativo.\n\nSaludos,\nStreamlit App")

    try:
        with smtplib.SMTP("authsmtp.boehringer.com", 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        print("✅ Correo enviado correctamente.")
    except Exception as e:
        print("❌ Error al enviar el correo:", e)

if __name__ == "__main__":
    send_test_email()
