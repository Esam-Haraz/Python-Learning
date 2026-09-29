boxes = ["book", "pen", ["shirt", "shoes"], ["apple", ["key", "orange"]]]
def find_key(box_list):
    for item in box_list:
        if item == "key":
            print("Found it")
            return True
        elif isinstance(item, list):
            found = find_key(item)
            if found == True:
                return True
    return False

find_key(boxes)
