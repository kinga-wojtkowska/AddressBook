from faker import Faker

class BaseContact:
    def __init__(self, name, surname, phone, email):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return ("{} {} {} {}".format(self.name, self.surname, self.phone, self.email))

    def contact(self):
        return f"Wybieram numer {self.contact_phone} i dzwonię do {self.name} {self.surname}"
            
    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1

    @property
    def contact_phone(self):
        return self.phone
                
class BusinessContact(BaseContact):
    def __init__(self, company, occupation, bus_phone, *args):
        super().__init__(*args)
        self.company = company
        self.occupation = occupation
        self.bus_phone = bus_phone

    def __str__(self):
        return ("{} {} {} {} {}, {} {}".format(self.name, self.surname, self.phone, self.email, self.company, self.occupation, self.bus_phone))
    
    @property
    def contact_phone(self):
        return self.bus_phone

def create_contacts(classid, number):
    fake = Faker('pl_PL')

    for x in range(number+1):
        if classid == BaseContact:
            address.append(classid(fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()))
        elif classid == BusinessContact:
            address.append(classid(fake.company(), fake.job(), fake.phone_number(), fake.first_name(), fake.last_name(), fake.phone_number(), fake.email()))

def fullshow():
    by_surname = sorted(address, key=lambda person: person.surname)
    n = 1
    print('number', 'surname', 'name', 'email')
    for i in by_surname:
        print(n, i.surname, i.name, i.email, i.contact_phone)
        n += 1

def contact(name, surname):
    for i, j in enumerate(address):
        l = address[i]
        if name == l.name and surname == l.surname:
            person = address[i]
            print(person.contact())

address=[]       
address.append(BusinessContact('Muscle Factory', 'Oral and maxillofacial radiologist', '+48-735-5518-27', 'Jowita', 'Zawadzka', '+48-515-5551-66', 'JowitaZawadzka@armyspy.com'))
address.append(BusinessContact('Friendly Advice', 'Claims investigator', '+48-735-5519-22', 'Miłogost', 'Dudek', '+48-455-5541-53', 'MilogostDudek@dayrep.com'))
address.append(BusinessContact('Kleinhans', 'Telecommunications line installer', '+48-535-5575-13', 'Apolonia', 'Sokołowska', '+48-725-5599-16', 'ApoloniaSokolowska@teleworm.us'))
address.append(BusinessContact('Jafco', 'Film processing technician', '+48-725-5528-72', 'Wiesław', 'Pawlak', '+48-575-5556-26', 'WieslawPawlak@rhyta.com'))
address.append(BusinessContact('Laneco', 'University dean', '+48-695-5550-72', 'Dobrosława', 'Dudek', '+48-725-5572-12', 'DobroslawaDudek@armyspy.com'))
address.append(BaseContact('Jowita', 'Gmurek', '+48-455-5599-75', 'JowitaGmurek@wp.pl'))
address.append(BaseContact('Marek', 'Górecki', '+48-321-6123-22', 'MarekGorecki@onet.pl'))

by_name = sorted(address, key=lambda person: person.name)
by_surname = sorted(address, key=lambda person: person.surname)
by_email = sorted(address, key=lambda person: person.email)

if __name__ == "__main__":
    fullshow()