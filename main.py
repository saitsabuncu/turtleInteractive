import turtle

# Çizim tahtasını oluştur ve ayarlarını yap
drawing_board = turtle.Screen()
drawing_board.bgcolor("blue")  # Arka plan rengini mavi yap
drawing_board.title("Python Turtle")  # Pencere başlığını ayarla

# Kaplumbağa nesnesini oluştur
muzzy = turtle.Turtle()

# Kaplumbağa ileri hareket eder
def turtle_forward():
    muzzy.forward(100)  # Kaplumbağa 100 birim ileri gider

# Kaplumbağayı sağa döndür
def rotate_angle_right():
    muzzy.setheading(muzzy.heading() - 100)  # Kaplumbağayı 100 derece sağa döndür

# Kaplumbağayı sola döndür
def rotate_angle_left():
    muzzy.setheading(muzzy.heading() + 100)  # Kaplumbağayı 100 derece sola döndür

# Ekranı temizle
def clear_screen():
    muzzy.clear()  # Kaplumbağanın çizdiği tüm çizgileri temizler

# Kalemi kaldır (çizim yapmadan hareket eder)
def turtle_pen_up():
    muzzy.penup()  # Kalemi kaldır, hareket sırasında çizim yapmaz

# Kalemi indir (çizim yapar)
def turtle_pen_down():
    muzzy.pendown()  # Kalemi indir, hareket sırasında çizim yapar

# Kaplumbağayı başlangıç konumuna döndür
def turtle_return_home():
    muzzy.home()  # Kaplumbağayı başlangıç pozisyonuna geri döndür

# Klavye girişlerini dinle
drawing_board.listen()

# Klavye tuşlarını belirli fonksiyonlara bağla
drawing_board.onkey(key="space", fun=turtle_forward)  # Boşluk tuşuna basıldığında ileri git
drawing_board.onkey(key="Down", fun=rotate_angle_right)  # Aşağı ok tuşuna basıldığında sağa dön
drawing_board.onkey(key="Up", fun=rotate_angle_left)  # Yukarı ok tuşuna basıldığında sola dön
drawing_board.onkey(key="c", fun=clear_screen)  # "c" tuşuna basıldığında ekran temizle
drawing_board.onkey(key="q", fun=turtle_pen_up)  # "q" tuşuna basıldığında kalemi kaldır
drawing_board.onkey(key="w", fun=turtle_pen_down)  # "w" tuşuna basıldığında kalemi indir
drawing_board.onkey(key="h", fun=turtle_return_home)  # "h" tuşuna basıldığında kaplumbağa başlangıç noktasına dön

# Çizim tahtası açık kalmaya devam eder
turtle.mainloop()
