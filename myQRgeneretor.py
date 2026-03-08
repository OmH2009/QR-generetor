import qrcode
import matplotlib.pyplot as plt
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    # חשוב לשנות ל-H כדי שהקוד יצליח להיקרא עם לוגו עליו
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
qr.add_data(url)

# יצירת התמונה (הפקודה make_image יוצרת את אובייקט התמונה)
img = qr.make_image(fill_color="black", back_color="white")
img = img.convert("RGB")

logo = Image.open("../nakashImg.jpeg")
width, height = img.size
logo_size = width // 5
logo = logo.resize((logo_size, logo_size))

pos = ((width - logo_size) // 2, (height - logo_size) // 2)
img.paste(logo, pos)
# --- התוספת להצגה ב-Plots ---
plt.figure(figsize=(10, 10))  # קביעת גודל החלון
plt.imshow(img, cmap='gray') # טעינת התמונה לתצוגה
plt.axis('off')              # ביטול הצירים (המספרים בצדדים)
plt.show()                   # פקודה זו פותחת את ה-Plots ב-PyCharm