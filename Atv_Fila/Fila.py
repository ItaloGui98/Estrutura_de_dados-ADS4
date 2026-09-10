class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def contar_nos(head):
    contador = 0
    while head:
        contador += 1
        head = head.next
    return contador


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    total = contar_nos(list1) + contar_nos(list2)
    if total > 50:
        raise ValueError(f"A lista final teria {total} nós, o que ultrapassa o limite de 50.")

    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val <= list2.val:
        list1.next = merge_two_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists(list1, list2.next)
        return list2


def imprimir(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4, ListNode(7))))
    list2 = ListNode()
    resultado = merge_two_lists(list1, list2)
    imprimir(resultado) 

#Essa validação adiciona um passo O(n + m) extra (contar os nós), mas isso não muda a ordem de grandeza da complexidade total, que continua O(n + m) de tempo. O espaço extra também permanece O(n + m) por conta da recursão.