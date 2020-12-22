# Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом.
# Методы push_back, push_front, pop_back, pop_front работали корректно. Но, если в деке было много элементов,
# программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите
# эффективную реализацию.
# Внимание: при реализации нельзя использовать связный список.
# Формат ввода
#
# В первой строке записано количество команд n — целое число, не превосходящее 5000. Во второй строке записано число
# m — максимальный размер дека. Он не превосходит 1000. В следующих n строках записана одна из команд:
# push_back value – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов,
# вывести «error».
# push_front value – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов,
# вывести «error».
# pop_front – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
# pop_back – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
# value — целое число, по модулю не превосходящее 1000.



class Deq:

    storage = {}
    max_size, head, tail, count = 0, 0, 0, 0

    def __init__(self, size):
        self.max_size = size

    def push_back(self, value):
        if not self.handle_push_error():
            self.set_tail(1)
            self.storage[self.tail] = value

    def push_front(self, value):
        if not self.handle_push_error():
            self.set_head(-1)
            self.storage[self.head] = value

    def pop_front(self):
        if not self.handle_pop_error():
            print(self.storage.pop(self.head))
            self.set_head(1)

    def pop_back(self):
        if not self.handle_pop_error():
            print(self.storage.pop(self.tail))
            self.set_tail(-1)

    def set_tail(self, direction):
        self.count += direction

        if self.count == 1:
            self.tail = self.head
            return

        self.tail += direction

    def set_head(self, direction):
        self.count += -direction

        if self.count == 1:
            self.head = self.tail
            return

        self.head += direction

    def handle_pop_error(self):
        if self.count == 0:
            print("error")
            return True
        else:
            return False

    def handle_push_error(self):
        if self.count + 1 > max_size:
            print("error")
            return True
        else:
            return False



number_of_commands = int(input())
max_size = int(input())

deq = Deq(max_size)

for i in range(number_of_commands):
    value = input().split()
    if value[0] == "pop_front":
        deq.pop_front()
    if value[0] == "pop_back":
        deq.pop_back()
    if value[0] == "push_back":
        deq.push_back(value[1])
    if value[0] == "push_front":
        deq.push_front(value[1])