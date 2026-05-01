import ssl
import os
import socket
from cryptography import x509
from cryptography.hazmat.primitives import serialization

def get_certificate_chain(hostname, port):
	context = ssl.create_default_context()
	with socket.create_connection((hostname,port)) as sock:
		with context.wrap_socket(sock, server_hostname=hostname) as ssock:
			cert_chain = ssock.getpeercert(binary_form=True)
			peer_certs = ssock.get_peer_cert_chain()
			return peer_certs if peer_certs else [cert_chain]


def save_certificates_to_file(certificates, output_dir="certificates"):
	os.makedirs(output_dir, exist_ok=True)
	for idx, cert in enumerate(certificates):
		cert_obj = x509.load_der_x509_certificate(cert)
		pem_data = cert_obj.public_bytes(encoding=serialization.Encoding.PEM)
		file_path = os.path.join(output_dir, f"cert_{idx + 1}.pem")
		with open(file_path, "wb") as cert_file:
			cert_file.write(pem_data)

		print(f"Saved: {file_path}")


hostname = "qa.voereir.io"
cert_chain = get_certificate_chain(hostname, 443)
save_certificates_to_files(cert_chain)
