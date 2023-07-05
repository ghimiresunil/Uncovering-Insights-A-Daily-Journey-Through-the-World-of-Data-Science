"""
Python OOP: Explanation and uses of magic methods.
"""

class MyList:
    def __init__(self, list_data) -> None:
        self.data = list_data

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value


if __name__ == "__main__":
    # initialize list data
    list_data  = [10, 20, 30, 40, 50]
    
    # define index to get and set value
    get_index = 0
    set_index = len(list_data) - 1

    # instantiate object
    my_list = MyList(list_data)
    print(f"List data: {my_list.data}")
    print(f"Length of list data via magic method is: {len(my_list)}")

    # get item
    print(f'\nGetting first item from class via magic method: {my_list[get_index]}')

    # set item
    print(f'\nUpdating item at index: {set_index}')
    my_list[set_index] = 60

    # get new set value
    print(f"\nNew set item is: {my_list[set_index]}")
    print(f"Updated list after setting value: {my_list.data}")

    
