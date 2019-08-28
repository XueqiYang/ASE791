# /usr/bin/env python
import random
import numpy as np


class Col(object):

    def __init__(self):
        self.means1 = []
        self.sd1 = []
        self.list = []
        self.means2 = []
        self.sd2 = []
        self.step = 10
        self.list_length = 100
        self.value_range = range(300)

    def generate(self):
        return random.sample(self.value_range, self.list_length)

    def up(self):
        for i in self.generate():
            self.list.append(i)
            mean = sum(self.list)/len(self.list)
            sd = np.std(self.list)
            if len(self.list) % self.step == 0:
                self.means1.append(mean)
                self.sd1.append(sd)
        return self.means1, self.sd1

    def down(self):
        for i in range(self.step-1, len(self.list)):
            mean = sum(self.list)/len(self.list)
            sd = np.std(self.list)
            if (i+1) % self.step == 0:
                self.means2.insert(0, mean)
                self.sd2.insert(0, sd)
            len1 = len(self.list)
            del self.list[len1 - 1]
        return self.means2, self.sd2

    def check(self):
        for i in range(len(self.sd1)):
            if self.means1[i] == self.means2[i] and self.sd1[i] == self.sd2[i]:
                print("list: 0 --", (i + 1) * self.step, "same-->True")
            else:
                print("list: 0--", (i + 1) * self.step, "same-->False")
            print("Mean1:", self.means1[i], "Mean2:", self.means2[i], "sd1:", self.sd1[i], "sd2:", self.sd2[i])


if __name__ == "__main__":
    read = Col()
    m1, sd1 = read.up()
    m2, sd2 = read.down()
    read.check()
