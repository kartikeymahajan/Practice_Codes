class MidAdd():
    counter = 1
    output = []
    temp = []
    midd = 0
    prev_midd = 0
    def findmid(self, li):
        while len(list1) > MidAdd.counter:
            if MidAdd.counter == 1:
                self.calc_mid(li)
                MidAdd.prev_midd = MidAdd.midd
            else:
                MidAdd.prev_midd = MidAdd.midd
                self.calc_mid(li)
                
            self.output.append(li[MidAdd.midd ])
            if MidAdd.counter % 2 != 0:
                temp = list1[:MidAdd.prev_midd +1]
                MidAdd.counter += 1
            else:
                temp = list1[MidAdd.prev_midd +1:]
            self.findmid(temp)

    def calc_mid(self,li):
        if len(li)%2==0:
            MidAdd.midd = (len(li)//2)-1
        else:
            MidAdd.midd  = len(li)//2
           
list1 = [1,2,3,4,5,6,7,8,9,10]
obj = MidAdd().findmid(list1)
print(obj)