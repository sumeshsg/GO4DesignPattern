# Check the string (mutable) and List (immutable) behaviour.

class InstanceVariable(object):
    test_class_string = None
    test_class_list = []

    def __init__(self):
        self.test_instance_list = []


obj_1 = InstanceVariable()
obj_1.test_class_string = 'string 1'
obj_1.test_class_list.append(1)
obj_1.test_instance_list.append(1)

obj_2 = InstanceVariable()
obj_2.test_class_string = 'string 2'
obj_2.test_class_list.append(2)
obj_2.test_instance_list.append(2)

InstanceVariable.test_class_string = 'string 3'
InstanceVariable.test_class_list.append(100)

print("******************** Object 1*******************")
print(">>>>>>>>> Class string from object", obj_1.test_class_string, id(obj_1.test_class_string))
print(">>>>>>>>> Class string from class", InstanceVariable.test_class_string, id(InstanceVariable.test_class_string))

print(">>>>>>>>> Class list from object", obj_1.test_class_list, id(obj_1.test_class_list))
print(">>>>>>>>> Class list from class", InstanceVariable.test_class_list, id(InstanceVariable.test_class_list))
print(">>>>>>>>> Instance list from object", obj_1.test_instance_list, id(obj_1.test_instance_list))

print("******************** Object 2*******************")
print(">>>>>>>>> Class string from object", obj_2.test_class_string, id(obj_2.test_class_string))
print(">>>>>>>>> Class string from class", InstanceVariable.test_class_string, id(InstanceVariable.test_class_string))

print(">>>>>>>>> Class list from object", obj_2.test_class_list, id(obj_2.test_class_list))
print(">>>>>>>>> Class list from class", InstanceVariable.test_class_list, id(InstanceVariable.test_class_list))
print(">>>>>>>>> Instance list from object", obj_2.test_instance_list, id(obj_2.test_instance_list))
