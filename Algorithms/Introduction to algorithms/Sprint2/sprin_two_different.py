# В первой строке записано одно число — количество команд, оно не превосходит 5000.
# Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
# Далее идут команды по одной на строке. Команды могут быть следующих видов:
# push x — добавить число x в очередь
# pop — удалить число из очереди и вывести на печать
# peek — напечатать первое число в очереди
# size — вернуть размер очереди
# # При превышении допустимого размера очереди нужно вывести «error». При вызове операции pop для пустой очереди
# нужно вывести «None».

#
# class MyQueueSized:
#
#     max_size = 0
#
#     storage = []
#
#     def __init__(self, max_size):
#         self.max_size = max_size
#
#     def push(self,x):
#         if not self.is_full():
#             self.storage.append(x)
#
#     def pop(self):
#         if not self.is_empty():
#             print(self.storage.pop(0))
#         else:
#             print(None)
#
#     def is_empty(self):
#         return len(self.storage) == 0
#
#     def peek(self):
#         if not self.is_empty():
#             print(self.storage[0])
#         else:
#             print(None)
#
#     def size(self):
#         print(self.max_size)
#
#     def is_full(self):
#         if len(self.storage) >= self.max_size:
#             print("error")
#             return True
#         else:
#             return False

# commands = int(input())
# max_siz = int(input())
# q = MyQueueSized(max_siz)
#
# for _ in range(commands):
#     value = input().split()
#     if value[0] == "pop":
#         q.pop()
#     if value[0] == "peek":
#         q.peek()
#     if value[0] == "size":
#         q.size()
#     if value[0] == "push":
#         q.push(value[1])

# Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка.
# Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:
# get — вывести элемент в голове очереди и удалить его. Если очередь пуста, то вывести «error».
# put x — добавить число x в очередь
# size — вывести текущий размер очереди


# Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке.
# Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None. При этом push и pop также
# должны выполняться за константное время.
# Формат ввода
# В первой строке записано одно число - количество команд, оно не превосходит 100000. Далее идут команды по одной в
# строке. Команды могут быть следующих видов:
# push x — добавить число x в стек
# pop — удалить число с вершины стека
# get_max — напечатать максимальное число в стеке
# Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».


# commands = int(input())
#
#
# for _ in range(commands):
#     value = input().split()
#         if value[0] == "pop":
#             q.pop()
#         if value[0] == "peek":
#             q.peek()
#         if value[0] == "size":
#             q.size()

# class StackMaxEffective:
#     def __init__(self):
#
#         self.mainStack = []
#         self.trackStack = []
#
#     def push(self, x):
#         self.mainStack.append(x)
#         if (len(self.mainStack) == 1):
#             self.trackStack.append(x)
#             return
#
#         if (x > self.trackStack[-1]):
#             self.trackStack.append(x)
#         else:
#             self.trackStack.append(self.trackStack[-1])
#
#     def get_max(self):
#         if not self.is_empty():
#             print(self.trackStack[-1])
#         else:
#             print(None)
#
#     def pop(self):
#         if not self.is_empty():
#             self.mainStack.pop()
#             self.trackStack.pop()
#         else:
#             print("error")
#
#     def is_empty(self):
#         return len(self.mainStack) == 0
#
#
# commands = int(input())
# q = StackMaxEffective()
#
# for _ in range(commands):
#     value = input().split()
#     if value[0] == "pop":
#         q.pop()
#     if value[0] == "get_max":
#         q.get_max()
#     if value[0] == "push":
#         q.push(int(value[1]))

#
# Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов. Если вы с ней ещё не сталкивались, то
# наверняка столкнётесь –— она довольно популярная.
# Дана скобочная последовательность. Нужно определить, правильная ли она.
# Будем придерживаться такого определения:
# пустая строка —– правильная скобочная последовательность;
# правильная скобочная последовательность, взятая в скобки одного типа, –— правильная скобочная последовательность;
# правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью —–
# тоже правильная.
# На вход подается последовательность из скобок трёх видов: [], (), {}.
# Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True,
# если последовательность правильная, а иначе False.

# class Stack:
#
#     stack = []
#
#     def push(self, x):
#         self.stack.append(x)
#
#     def pop(self):
#         return self.stack.pop()
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
# values = input()
#
# def is_braces_sequence_correct(s: str):
#
#     stack = Stack()
#
#     for brace in s:
#         if brace not in "()[]":
#             continue
#
#         if brace in "([":
#             stack.push(brace)
#         else:
#             if stack.is_empty():
#                 return False
#             left = stack.pop()
#             if left == "(":
#                 right = ")"
#             elif left == "[":
#                 right = "]"
#             if right != brace:
#                 return False
#
#     return stack.is_empty()
#
# print(is_braces_sequence_correct(values))