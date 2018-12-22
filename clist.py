class Clist:
    class _Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_items(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        n = self._Node(item, None)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        self.size += 1

    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        f = self.last.next
        return f.item

    def delete(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print('리스트 비어있음')
        else:
            f = self.last.next
            p = f
            while p.next != f:
                print(p.item, ' -> ', end=' ')
                p = p.next
            print(p.item)

class EmptyError(Exception):
    pass


if __name__ == '__main__':
    s = Clist()
    s.insert('pear')
    s.insert('cherry')
    s.insert('orange')
    s.insert('apple')
    s.print_list()

    print(f's의 길이={s.no_items()}')
    print(f's의 첫 항목 :{s.first()}')

    s.delete()
    print(f'첫 노드 삭제 후: ', end=' ')
    s.print_list()
    print(f's의 길이={s.no_items()}')
    print(f's의 첫 항목 :{s.first()}')

    s.delete()
    print(f'첫 노드 삭제 후: ', end=' ')
    s.print_list()
    print(f's의 길이={s.no_items()}')
    print(f's의 첫 항목 :{s.first()}')


    s.delete()
    print(f'첫 노드 삭제 후: ', end=' ')
    s.print_list()
    print(f's의 길이={s.no_items()}')
    print(f's의 첫 항목 :{s.first()}')

    s.delete()
    print(f'첫 노드 삭제 후: ', end=' ')
    s.print_list()
    print(f's의 길이={s.no_items()}')
    print(f's의 첫 항목 :{s.first()}')



