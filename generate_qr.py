import qrcode
from PIL import Image
import hashlib

def main():
    # Generate Hash
    hash_seq = hashlib.sha224(b'Randomly generated string').hexdigest()
    print(f'This is the hash value: {hash_seq}')

    print('Generating QR code...')
    qr = qrcode.QRCode(
        version=16,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(hash_seq)
    qr.make(fit=True)

    img = qr.make_image(fill_color="green",
                        back_color="white").convert('RGB')
    img.save('qr.png')

    # Integrate with logo
    print('Integrating SCB logo...')
    logo_display = Image.open('scb_logo.png')
    logo_display.thumbnail((160,160))
    logo_pos = ((img.size[0] - logo_display.size[0]) // 2, 
                (img.size[1] - logo_display.size[1]) //2 )

    img.paste(logo_display, logo_pos)
    img.save('qr_with_logo.png')

if __name__=="__main__":
    main()