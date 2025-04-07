class Telephone:
    def __init__(self):
        self.telephone = {}
    def add_entry(self, name, number):
        self.telephone[name] = number

    def delete_entry(self, name):
        self.telephone.pop[name]

    def update_entry(self, name, number):
        self.telephone[name]= number

    def lookup_entry(self, name):
        return self.telephone[name]

    def __str__(self):
        ret_dct = ''
        for key, value in self.telephone.item():
            ret_dct += f'{key} : {value}'
        return ret_dct