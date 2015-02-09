__author__ = 'Joel'
from linked_list import LinkedList


def main():
    list1 = LinkedList()
    list1.add_to_front(2)
    list1.add_to_front(3)
    list1.add_to_back(4)
    list1.add(1)
    list1.add(5)
    print list1
    #for value in list1.enumerate():
        #print value

    # 1) 3=>2=>4=>1=>5=>None remove(4) 3=>2=>1=>5=>None
    list1.remove(4)
    print list1
    list1.remove(5)
    print list1
    # 2) 3=>2=>4=>1=>5=>None remove(5) 3=>2=>4=>1=>None
    list1.remove_front()
    # print list1
    # 3) 3=>2=>4=>1=>5=>None remove(3) 2=>4=>1=>5=>None
    # list1.remove_back()
    # print list1

    list1.clear()
    print list1

if __name__ == "__main__":
    main()
