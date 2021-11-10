from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import argparse
import subprocess
import getpass


parser = argparse.ArgumentParser()
parser.add_argument("-emisor", dest="emisor",
                    help="Correo del emisor", required=True)
parser.add_argument("-receptor", dest="receptor", help="Correo del receptor",
                    required=True)
parser.add_argument("-name", dest="name", help="Nombre del archivo del reporte",
                    required=True)
params = parser.parse_args()
emisor = str(params.emisor)
receptor = str(params.receptor)
name = str(params.name)

try:
    print("--POWERSHELL EVENT LOG REPORT--")
    targetLogName = input("Target Log Name: ")
    eventCount = input("Event Count: ")
    eventType = input("Event Type: ")
    comando = "powershell -Executionpolicy ByPass -File ReportEvent.ps1 " \
              " -ReportFile " + name + " -targetLogName " + targetLogName + "" \
              " -eventCount " + eventCount + " -eventType " + eventType
    runningProcesses = subprocess.check_output(comando)
    print(runningProcesses.decode())
    mensaje = "El script funcionó y generó el siguiente resultado"
except Exception as e:
    error = "Ocurrió un error " + str(e)
    mensaje = "El script no funcionó: " + error
    pass

print("--SEND RESULT TO E-MAIL--")
user = emisor
pasw = getpass.getpass("Contraseña: ")
email_msg = MIMEMultipart()
email_msg["From"] = emisor
receipents = [receptor]
email_msg["To"] = ", ".join(receipents)
email_msg["Subject"] = "Reporte de Ejecución de Script"
email_msg.attach(MIMEText(mensaje, "plain"))


if mensaje == "El script funcionó y generó el siguiente resultado":
    with open(name, "rb") as arch:
        attach = MIMEApplication(arch.read(), _subtype="html")
    attach.add_header("Content-Disposition", "attachment", filename=name)
    email_msg.attach(attach)


server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
server.login(emisor, pasw)
server.sendmail(email_msg["From"], receipents, email_msg.as_string())
server.quit()
print("successfully sent email to %s:" % (email_msg["To"]))