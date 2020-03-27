from AdapterPattern.Intranet import Intranet
from AdapterPattern.PersonnelSystem import PersonnelSystem
from AdapterPattern.PhoneListAdapter import PhoneListAdapter

if __name__ == '__main__':
    personnel_system = PersonnelSystem()
    print(personnel_system.get_employee())

    adapter = PhoneListAdapter(personnel_system)

    intranet = Intranet(adapter)
    print(intranet.show_phone_list())
