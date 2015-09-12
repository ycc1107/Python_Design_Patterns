# Adapter
# interface didn't fit the server

class Adapter:
    def __init__(self,objectClass,**attr):
        self._object = objectClass
        self.__dict__.update(attr)

    def __getattr__(self,attr):
        return getattr(self._object,attr)

class Chinese:
    def __init__(self):
        self._name = 'Chinese'

    def speak_chinese(self):
        return 'Ni Hao'

class English:
    def __init__(self):
        self._name = 'English'

    def speak_english(self):
        return 'how are you?'

o = []
chinese = Chinese()
english = English()

o.append(Adapter(chinese,speak = chinese.speak_chinese))
o.append(Adapter(english,speak = english.speak_english))

for item in o:
    print(item.speak())
