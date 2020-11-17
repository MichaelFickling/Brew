def listify (objectclass, dict):
    object_attributes = []
    object_list = []

    names_of_objects = [*dict]  # get the names of all the objects in this class
    for objectname in names_of_objects:
        object_attributes.append(dict[objectname].keys())  # get the attributes of one object
        for attribute in object_attributes:
            object_list.append(objectclass(objectname, attribute[0] , attribute[1]))  # construct that object and put them in a list