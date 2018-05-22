from data_structures.linked_list.single_linked_list import Node


def random_list():
    return Node(25, Node(12, Node(35, Node(6, Node(15, Node(45))))))


def ascending_list():
    return Node(10, Node(20, Node(30, Node(40, Node(50, Node(60, Node(70)))))))


def palindrome_list():
    return Node(10, Node(20, Node(30, Node(40, Node(30, Node(20, Node(10)))))))


def another_ascending_list():
    return Node(12, Node(22, Node(33, Node(45, Node(53, Node(61, Node(78)))))))


def combined_ascending_list():
    return Node(10,
                Node(12,
                     Node(20,
                          Node(22,
                               Node(30,
                                    Node(33,
                                         Node(40,
                                              Node(45,
                                                   Node(50,
                                                        Node(53,
                                                             Node(60,
                                                                  Node(61,
                                                                       Node(70,
                                                                            Node(78))))))))))))))


def descending_list():
    return Node(70, Node(60, Node(50, Node(40, Node(30, Node(20, Node(10)))))))


def duplicate_list():
    return Node(10, Node(20, Node(30, Node(40, Node(10, Node(20, Node(30, Node(40))))))))


def non_duplicate_list():
    return Node(10, Node(20, Node(30, Node(40))))
