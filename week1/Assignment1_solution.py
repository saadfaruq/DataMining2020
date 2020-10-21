# creating a new class name ListKeeper
class ListKeeper():
    
    def __init__(self):
        self.named_lists = {
            'example':[1,2,3,4,5]
        }       
    def show(self):                                                  #defining a function to show all list name 
        return list(self.named_lists.keys())
    def add(self, name, list_elements):                                # defining a funtion add
        self.named_lists[name] = list_elements    
    def delete(self, name):                                             # defining a funtion to delete 
        del self.named_lists[name]
    def sort(self, name):                                              # defining a funtion to sort
        return sorted(self.named_lists[name]) 
    def append(self, name, list_elements):                             # defining a funtion to append
        self.named_lists[name].extend(list_elements)