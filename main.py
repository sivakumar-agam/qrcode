import qrcode

def generate_qr(url, filename='qr_code.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code generated and saved as {filename}")
if __name__ == "__main__":
    url = "https://www.neovault.app/scan/?vr=NT03041201-02B030405B0607080910111226&ln=D2602007&ex=2028-01-01T00:00:00Z"
    generate_qr(url,"Neotest Multi Drug Cassette.png")