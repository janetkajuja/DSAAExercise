"""all necessary module is imported"""

LIST_OF_ITEMS = []
ROW_SEPARATOR = " "
FILE_NAME = "items.txt"
SEQUENCE_FILE = "order_by_sequence.txt"
SIZE_FILE = "order_by_size.txt"
PRIORITY_FILE = "order_by_priority.txt"


def read_file(file):
    """This function will read the text file in the terminal"""
    try:
        with open(file, "r") as txt_file:
            for data in txt_file:
                items_dic = {}
                data_line = data.replace("\n", "")
                new_data = data_line.split(ROW_SEPARATOR)
                items_dic["sequence"] = int(new_data[0])
                items_dic["size"] = int(new_data[1])
                items_dic["priority"] = new_data[2]
                LIST_OF_ITEMS.append(items_dic)
        return LIST_OF_ITEMS
    except FileNotFoundError:
        pass

def new_file_sequence(columns, items_list_sorted):
    """This is a function for creating a file"""
    file = str(f'order_by_{columns}.txt')
    with open(file, "w") as created_file:
        final_data = ""
        for data in items_list_sorted:
            sequence = data["sequence"]
            size = data["size"]
            priority = data["priority"]
            new_line = str(f'{sequence} {size} {priority} \n')
            final_data = str(f'{final_data}') + new_line
        created_file.write(final_data)


def sorted_item(column, order):
    """This function is for the ascending and descending order depending on the user request"""
    if str(order) == "asc":
        list_sorted = sorted(LIST_OF_ITEMS, key=lambda n: n[column])
        # print(column, list_sorted)
        new_file_sequence(column, list_sorted)
        return

    if str(order) == "desc":
        list_sorted1 = sorted(LIST_OF_ITEMS, key=lambda f: f[column], reverse=True)
        new_file_sequence(column, list_sorted1)
        return
