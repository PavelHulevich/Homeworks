# class MyNumbers:
#     def __init__(self):
#         self.a = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             e = self.a
#             self.a += 1
#             return e
#         else:
#             raise StopIteration
#
#
# myiter = MyNumbers()
# for x in myiter:
#     print(myiter.a, end='')
#     print(f'{x} ', end='')
#
#     # class CharSet:
#     #     def __init__(self, reg_chars, password):
#     #         self.reg_chars = reg_chars
#     #         self.password = password
#     #     def __next__(self):
#     #         if self.reg_chars in upper_chars:
