import socket

hostname = socket.gethostname()

print("=== Información del equipo ===")
print(f"Hostname: {hostname}")

try:
    ip = socket.gethostbyname(hostname)
    print(f"IP local: {ip}")
except socket.error:
    print("No se pudo obtener la dirección IP.")