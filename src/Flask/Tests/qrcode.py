import requests
# https://developers.google.com/chart/infographics/docs/qr_codes (Google Chart API)


text = "QR ok"

req = requests.get('https://chart.googleapis.com/chart?cht=qr&cht=qr&chs=200x200&chl=' + text + '&choe=UTF-8',timeout=60)

with open('qr.png', 'wb') as f:
    f.write(req.content)
