import cv2 as cv

def main():
    # Original QR
    im = cv.imread('qr.png')
    det = cv.QRCodeDetector()
    print('decoding qr code...')
    retval, points, straight_qrcode = det.detectAndDecode(im)
    print(f'This is the value stored: {retval}')
    print()

    # QR with logo
    im = cv.imread('qr_with_logo.png')
    det = cv.QRCodeDetector()
    print('decoding qr code with logo...')
    retval, points, straight_qrcode = det.detectAndDecode(im)
    print(f'This is the value stored: {retval}')

if __name__=="__main__":
    main()