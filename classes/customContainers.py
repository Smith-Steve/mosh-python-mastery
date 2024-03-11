#When we add a "__" as a prefix proceeding a variable, that variable is automatically private.
#When a variable in a class (I think their called, 'members') is private, it cannot be utilized
#outside of the class.
#It can still be used inside the class to define members, etc..

class TagCloud:
    def __init__(self):
        self.__tags = {}
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
    
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    
    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
print(cloud.__tags)
cloud.add("python")
cloud.add("Python")
cloud.add("Python")
print(cloud.__tags["PYTHON"])