"""Importing all module used for this file"""
import sys

from order import read_file, sorted_item
if __name__ == '__main__':
    read_file(file="items.txt")
    USER_REQUEST = input("Enter your preferred order either asc or desc: ")
    USER_REQUEST.upper()
    # if user_request != "asc" or user_request != "desc":
    #     print("The sorted order provided is not supported please choose 'ASC' of 'DESC'! ")
    COLUMNS_CHOICE = input("Enter the column you want to sort, either sequence, size or priority: ")
    COLUMNS_CHOICE.upper()
    sorted_item(COLUMNS_CHOICE, USER_REQUEST)
    sys.exit(0)
