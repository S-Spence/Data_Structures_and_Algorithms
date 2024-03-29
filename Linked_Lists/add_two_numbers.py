import unittest
"""
Problem: Given two linked lists storing digits in reverser oder, retrun the sum of the linked lists also in reverse order. 

        Ex. 2->4->3
            5->6->4
            -------
            7->0->8
        Leetcode: https://leetcode.com/problems/add-two-numbers/ 
Constraints:
        What to return if the list is empty? -> Assume the list will not be empty

Tests: 
    l1 = 2->4->3, l2 = 5->6->4 ->  342 + 465 = 807 = result = 7->0->8
    l1 = 3->0->9, l2 = 0 -> 0-> 2 -> = 903 + 200 = 1103 + result = 3->0->1->1
    l1 = 0, l2 = 0 -> reult = 0

Solution: Keep track of the variable to carry on every iteration. Leave the head element as None since the output is in reverse order
          Return result.next to skip none
          Runtime O(max(m,n)) Space: O(max(m,n))
"""

class ListNode:
    def __init__(self, val=None):
         self.val = val
         self.next = None


def add_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Take two linked lists and add the numbers together. Return 
    a linked list containging the sum in reverse order. 
    Runtime O(max(m, n)), Space: O(max(m,n)). 
    Time and space are the longest list in the worst case. 
    """
    result = ListNode()    # Create a linked list to return
    current = result       # Set the current node value to the results linked list
    carry = 0              # Carry value for sum >= 10

    # While there are numbers to add
    while l1 or l2 or carry:
        # Iniialize val 1 and val 2 to zero so nothing gets added if one list is shorter
        val_1 = 0
        val_2 = 0
        
        # If linked list one has a value, move pointers
        if l1:
            val_1 = l1.val
            l1 = l1.next
               
        # If linked list two has a value, move pointers
        if l2:
            val_2 = l2.val
            l2 = l2.next
       
        # Add total
        total = carry + val_1 + val_2
        # Add value less than ten in current.next
        current.next = ListNode(total % 10)
        # Carry the rest over for the next iteration
        carry = total//10
        # Move pointer
        current = current.next
          
    # print result.next because the sum is in reverse order, so the first node is None. Reverse R/S: O(max(m,n))
    return result.next


class TestMethods(unittest.TestCase):
    def setUp(self):
        # Create L1 elements
        self.l1_1 = ListNode(2)
        self.l1_1.next = ListNode(4)
        self.l1_1.next.next = ListNode(3)

        self.l1_2 = ListNode(3)
        self.l1_2.next = ListNode(0)
        self.l1_2.next.next = ListNode(9)

        self.l1_3 = ListNode(0)

        # Create L2 elements
        self.l2_1 = ListNode(5)
        self.l2_1.next = ListNode(6)
        self.l2_1.next.next = ListNode(4)

        self.l2_2 = ListNode(0)
        self.l2_2.next = ListNode(0)
        self.l2_2.next.next = ListNode(2)

        self.l2_3 = ListNode(0)

    # Tests for linked lists
    def test_1(self):
        result = add_numbers(self.l1_1, self.l2_1)
        expected = "708"
        i = 0
        while result != None:
            self.assertTrue((result.val) == int(expected[i]))
            i += 1
            result = result.next

    def test_2(self):
        result = add_numbers(self.l1_2, self.l2_2)
        expected = "3011"
        i = 0
        while result != None:
            self.assertTrue((result.val) == int(expected[i]))
            i += 1
            result = result.next

    def test_3(self):
        result = add_numbers(self.l1_3, self.l2_3)
        expected = "0"
        i = 0
        while result != None:
            self.assertTrue((result.val) == int(expected[i]))
            i += 1
            result = result.next

# Run tests
if __name__ == "__main__":
    unittest.main()
