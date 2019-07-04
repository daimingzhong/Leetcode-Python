class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None

    def build_two_list_node(self):
        l0 = ListNode(0)
        l1 = ListNode(1)
        l0.next = l1
        return l0

    def build_five_list_node(self):
        l0 = ListNode(0)
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l0.next = l1
        l1.next = l2
        l2.next = l3
        l3.next = l4
        return l0