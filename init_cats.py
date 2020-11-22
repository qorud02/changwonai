class Cat:
    #이름,색깔
    def __init__(self, name, color="흰색"):
        self.name = name
        self.color = color

    def meow(self, name):
        print('my name is{}, my color {}, 야옹, {}'.format(self.name, self.color, name))

nabi = Cat('나비', '검은색')
ne = Cat('네네', '무지개')
nam = Cat('남', '백')
nabi.meow('dw')
ne.meow('ds')
nam.meow('dz')