class Corpus:
    def __init__(self, block, matplata, proccesor, opermemory, videocard, postmemory):
        self.block = block
        self.matplata = matplata
        self.proccessor = proccesor
        self.opermemory = opermemory
        self.videocard = videocard
        self.postmemory = postmemory
    
    def start(self):
        print("ПК включен")

    def stop(self):
        print("ПК выключен")


class Block:
    def __init__(self, marka, power):
        self.marka = marka   
        self.power = power

    def start(self):
        print("Запуск блока питания")

    def stop(self):
        print("Стоп")

class MatPlata:
    def __init__(self, marka, form):
        self.marka = marka
        self.form = form

    def start(self):
        print("Запуск материнской платы")

    def stop(self):
        print("Стоп")

class Proccessor:
    def __init__(self, marka, cores):
        self.marka = marka
        self.cores = cores
         

    def start(self):
        print("Запуск процессора")

    def stop(self):
        print("Стоп") 

class Opermemory:
    def __init__(self, marka, volume):
        self.marka = marka
        self.ram = volume

    def start(self):
        print("Запуск оперативной памяти")

    def stop(self):
        print("Стоп")

class Videocard:
    def __init__(self, marka,speed):
        self.marka = marka
        self.vram = speed
         
    def start(self):
        print("Запуск видеокарты")

    def stop(self):
        print("Стоп")

class Postmemory:
    def __init__(self, marka, Gbytes):
        self.marka = marka
        self.memory = Gbytes

    def start(self):
        print("Запуск постоянной памяти")

    def stop(self):
        print("Стоп")

myBlock = Block("Samsung",500)
myMatPlata = MatPlata("ASUS","GTX")
myProccessor = Proccessor("IBM",3)
myOpermemory = Opermemory("DDR",12)
myVideocard = Videocard("Nvidia", 800)
myPostmemory = Postmemory("SONY",500)
myPC = Corpus(myBlock,myMatPlata,myProccessor,myOpermemory,myVideocard,myPostmemory)


def Reg():
    choice = int(input("Выберите действие:\n1 - Включить ПК\n2 - Выключить ПК\n"))
    if choice == 1:
        myPC.block.start()
        myPC.matplata.start()
        myPC.proccessor.start()
        myPC.opermemory.start()
        myPC.videocard.start()
        myPC.postmemory.start()
        myPC.start()

    elif choice == 2:
        myPC.block.stop()
        myPC.matplata.stop()
        myPC.proccessor.stop()
        myPC.opermemory.stop()
        myPC.videocard.stop()
        myPC.postmemory.stop()
        myPC.stop()

    
Reg()