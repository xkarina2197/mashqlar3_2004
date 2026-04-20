# 21-misol
class MusicPlayer:
    def __init__(self, song):
        self.song = song

    def play(self):
        print(f"{self.song} chalinyapti")

    def stop(self):
        print(f"toxtatildi")

m1 = MusicPlayer("AU")
m1.play()

# 22-misol
class Fan:
    def __init__(self, speed):
        self.speed = speed

    def increase(self):
        self.speed += 1
        print("Tezlik oshdi")

    def decrease(self):
        if self.speed > 0:
            self.speed -= 1
        print("Tezlik kamaydi")


f1 = Fan(12)
f1.decrease()
f1.increase()

# 23-misol
class TV:
    def __init__(self, channel):
        self.channel = channel

    def next_channel(self):
        self.channel  + 1
        print(f"Keyingi kanal")

    def oldingi_kanal(self):
        self.channel - 1
        print(f"Oldingi kanal")


t1 =  TV(11)
t1.next_channel()
t1.oldingi_kanal()


# 24-misol
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"{self.name} - {self.price} so'm")

    def discount(self):
        print("Chegirma qo‘llandi")


p1 = Product("Ali", 24)
p1.show()
p1.discount()

# 25-misol
class Alarm:
    def __init__(self, time):
        self.time = time

    def set_alarm(self):
        print(f"Alarm {self.time} ga ornatilgan")

    def ring(self):
        print(f"Jiring!!!")

a1 = Alarm("07:00")
a1.set_alarm()


# 26-misol
class Message:
    def __init__(self, text):
        self.text = text

    def send(self):
        print(f"xabar yuborildi")

    def delete(self):
        print(f"xabar o'chirlidi")


m1 = Message("xabar")
m1.send()

# 27-misol
class File:
    def __init__(self, name):
        self.name = name

    def open(self):
        print(f"{self.name} ochildi")

    def close(self):
        print(f"{self.close} yopildi")

f1 = File("Text.txt")
f1.open()

# 28-misol
class Doorlock:
    def init(self, locked):
        self.locked = locked

    def lock(self):
        print("qulflandi")

    def unlock(self):
        print("ochildi")

d1 = Doorlock()
d1.unlock()

# 29-misol
class Camera:
    def __init__(self, mode):
        self.mode = mode

    def capture(self):
        print(f"{self.mode} rejimida rasm olindi")

    def switch_mode(self):
         print("Rejim o‘zgardi")

c1 = Camera("file.txt")
c1.capture()
