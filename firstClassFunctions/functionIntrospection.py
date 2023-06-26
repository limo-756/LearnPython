def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()


class C: pass


def F(): pass


if __name__ == '__main__':
    upper_case_name.short_description = 'Customer name'
    print(upper_case_name)
    classObj = C()
    functionObj = F
    print("Function exclusive methods")
    print(set(dir(functionObj)) - set(dir(classObj)))
    print("Class exclusive methods")
    print(sorted(set(dir(classObj)) - set(dir(functionObj))))
