import easyocr
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def applyEasyocr(frame):

    reader = easyocr.Reader(['pt'], gpu=False)

    out = reader.readtext(frame, detail=0)

    return out

def applyPytesseract(frame):

    out = pytesseract.image_to_string(frame)

    return out