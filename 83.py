class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def main(head):
    original_head = head
    while head is not None:
        block = head.next
        while block is not None and block.val == head.val:
            block = block.next
        head.next = block
        head = block

    return original_head


if __name__ == '__main__':
    head_ = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    main(head_)
