#########
# Stack #
#########


class Stack:
     def __init__(self):
         """creates a new stack that is empty. It needs no parameters and returns an empty stack"""
         self.items = []

     def isEmpty(self):
         """to see whether the stack is empty. It needs no parameters and returns a boolean value"""
         return self.items == []

     def push(self, item):
         """adds a new item to the top of the stack. It needs the item and returns nothing"""
         self.items.append(item)

     def pop(self):
         """removes the top item from the stack. It needs no parameters and returns the item. The stack is modified"""
         return self.items.pop()

     def peek(self):
         """returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified"""
         return self.items[len(self.items)-1]

     def size(self):
         """returns the number of items on the stack. It needs no parameters and returns an integer"""
         return len(self.items)

##################
# Main() to test #
##################
if __name__ == '__main__':
    
    def baseConverter(decNumber,base):
        digits = "0123456789ABCDEF"
        remstack = Stack()

        while decNumber > 0:
            rem = decNumber % base
            remstack.push(rem)
            decNumber = decNumber // base

        newString = ""
        while not remstack.isEmpty():
            newString = newString + digits[remstack.pop()]

        return newString

    print(baseConverter(25,2))
    print(baseConverter(25,16))
