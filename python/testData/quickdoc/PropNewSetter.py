class A(object):
  @property
  def x(self):
    "Does things to X"
    return 1

  @x.setter
  def x(self, v):
    "Sets X"
    self.__x = v

a = A()
a.<the_ref>x = 1

