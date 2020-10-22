class Alpha:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        print(self.a+self.b)

if __name__ == "__main__":

  A = Alpha(10, 20)
  print(A.a+ A.b)
  A.sum()
        