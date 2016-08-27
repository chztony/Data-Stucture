# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height)
                return maxHeight


def fill_depth(parent, i, depth):

        if depth[i] != 0:
                return

        if parent[i] == -1:
                depth[i] = 1
                return

        if depth[parent[i]] == 0:
                fill_depth(parent, parent[i], depth)

        depth[i] = depth[parent[i]] + 1

def find_height(parent):
        n = len(parent)
        depth = [0 for i in range(n)]

        for i in range(n):
                fill_depth(parent, i, depth)

        ht = depth[0]
        for i in range(1, n):
                ht = max(ht, depth[i])

        return ht



def main():
        tree = TreeHeight()
        tree.read()
        parent = tree.parent
        print(find_height(parent))


threading.Thread(target=main).start()
