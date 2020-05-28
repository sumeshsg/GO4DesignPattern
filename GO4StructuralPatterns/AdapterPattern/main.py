from GO4StructuralPatterns.AdapterPattern.Intranet import Intranet
from GO4StructuralPatterns.AdapterPattern.PersonnelSystem import PersonnelSystem
from GO4StructuralPatterns.AdapterPattern.PhoneListAdapter import PhoneListAdapter


if __name__ == '__main__':
    personnel_system = PersonnelSystem()
    print(personnel_system.get_employee())

    adapter = PhoneListAdapter(personnel_system)

    intranet = Intranet(adapter)
    for item in intranet.get_employee():
        print (item)
