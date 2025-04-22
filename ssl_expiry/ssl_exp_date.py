import ssl
import socket
from datetime import datetime

def get_domain():
    domain = input("Enter domain name: ")
    return domain

def main():
    domain = get_domain()
    port = 443

    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:
                cert = secure_sock.getpeercert()
                not_after = cert['notAfter']
                expiry_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                now = datetime.utcnow()
                days_left = (expiry_date - now).days

                print(f"The SSL certificate for {domain} expires in {days_left} days (on {expiry_date}).")

    except socket.error as e:
        print(f"Socket error: {e}")
    except ssl.SSLError as e:
        print(f"SSL error: {e}")
    except KeyError:
        print("Could not retrieve the certificate's expiration date.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
