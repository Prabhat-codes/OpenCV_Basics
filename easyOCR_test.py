import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('image.jpeg',detail=0)
print(result)

