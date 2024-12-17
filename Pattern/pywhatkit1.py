import qrcode

def create_whatsapp_qr():
    phone_number = input("Enter your WhatsApp phone number: ")
    # message = input("Enter the message to be pre-filled (optional): ")
    
    whatsapp_url = f"https://wa.me/{phone_number}?"
    
    qr = qrcode.make(whatsapp_url)
    qr.save("whatsapp_qr.png")

if __name__ == "__main__":
    create_whatsapp_qr()
