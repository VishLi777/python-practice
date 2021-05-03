# Рассмотрим следующее определение классов. Почему произошла ошибка?
#class A:
#    pass

#class B(A):
#    pass

#class C(A, B):
#    pass


# TypeError                                 Traceback (most recent call last)
# <ipython-input-3-23dfd2d101ea> in <module>
#       5     pass
#       6
# ----> 7 class C(A, B):
#       8     pass
#
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B

# Class C inherits from A and B.
# But since class B is already inherited from class A, then Python cannot determine
# the methods of which class to take first.
# *Cannot create a consistent method resolution order (MRO) for bases A, B*


# so you only need to inherit from B to fix this error
class A:
    pass


class B(A):
    pass


class C(B):
    pass