# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

    #self.n = 5
    #self.key = [4, 2, 5, 1, 3]
    #self.left = [1, 3, -1, -1, -1]
    #self.right = [2, 4, -1, -1, -1]


  def inOrder(self):
    self.result = []
    self.inOrder_recursive(0, self.result)
    # Finish the implementation
    # You may need to add a new recursive method to do that
    return self.result

  def inOrder_recursive(self, note, result):
    if note == -1:
        return
    self.inOrder_recursive(self.left[note], result)
    result.append(self.key[note])
    self.inOrder_recursive(self.right[note], result)


  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preOrder_recursive(0, self.result)
    return self.result

  def preOrder_recursive(self, note, result):
    if note == -1:
        return
    result.append(self.key[note])
    self.preOrder_recursive(self.left[note], result)
    self.preOrder_recursive(self.right[note], result)


  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.posOrder_recursive(0, self.result)
    return self.result

  def posOrder_recursive(self, note, result):
    if note == -1:
        return
    self.posOrder_recursive(self.left[note], result)
    self.posOrder_recursive(self.right[note], result)
    result.append(self.key[note])

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
