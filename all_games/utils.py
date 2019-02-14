def get_choice(title, list, display_attr_getter, return_index = False):
    print(title)
    for index, item in enumerate(list):
        print("\t{} - {}".format(index, display_attr_getter(item)))

    while True:
        try:
            index = int(input())
            if 0 <= index < len(list):
                return index if return_index else list[index]
        except: pass
        print("Try again")
