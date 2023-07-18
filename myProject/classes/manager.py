class Manager():
    def __init__(self,reg,inlog,userModerAdmin,dataList):
        self.reg = reg
        self.inlog = inlog
        self.userModerAdmin = userModerAdmin
        self.dataList = dataList
    def work(self):
        print(self)