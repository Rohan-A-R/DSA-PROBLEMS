class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# this method will not work for largeinputs
def linkedlist_to_int(head):
        num=0
        while head:
            num=num*10+head.val
            head=head.next
        return num
    
def int_linkedist(num):
        if num==0:
            return Node(0)
        dummy=Node(-1)
        current=dummy
        for digit in str(num):
            current.next=Node(int(digit))
            current=current.next
        return dummy.next
    
def sum(num1,num2):
    int1=linkedlist_to_int(num1)
    int2=linkedlist_to_int(num2)
    total=int1+int2
    return int_linkedist(total)


def add_optimize(num1,num2):
    def reverse(head):
            prev=None
            current=head
            while current:
                next_node=current.next
                current.next=prev
                prev=current
                current=next_node
            return prev
    num1=reverse(num1)
    num2=reverse(num2)

    dummy=Node(0)
    current=dummy
    carry=0
    while num1 or num2 or carry:
        sum=carry
        if num1:
             sum+=num1.data
             num1=num1.next
        if num2:
             sum+=num2.data
             num2=num2.next
        carry=sum//10
        current.next=Node(sum%10)
        current=current.next

    return reverse(dummy.next)

         
