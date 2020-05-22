class Account:
    def __init__(self,number, balance, Annualinterestrate):
        self.number = number
        self.balance = balance
        self.Annualinterestrate = Annualinterestrate
        self.Monthlyinterestrate = Annualinterestrate/12
    def save(self,money):
        self.balance = self.balance + money
        print("存款成功！余额为：%.2f"%(self.balance))
    def get(self,money):
        if self.balance<money:
            print("取款失败！余额不足！")
            return
        self.balance = self.balance - money
        print("取款成功！余额为：%.2f"%(self.balance))
    def show(self):
        print("账号：%s"%(self.number))
        print("余额：%.2f"%(self.balance))
        print("年利率：%.2f%%"%(self.Annualinterestrate*1000))
        print("月利率：%.3f%%"%(self.Monthlyinterestrate*1000))
        print("月息：%.2f"%(self.balance*self.Monthlyinterestrate))

Account1 = Account(998866,2000,0.0045)
while(1):
    print("存钱请输入1\n取钱请输入2\n展示信息请输入3\n退出请输入0")
    x = int(input())
    if x==0:
        break
    elif x==1:
        print("输入你要存入的钱数：")
        money = int(input())
        Account1.save(money)
    elif x==2:
        print("输入你要取出的钱数：")
        money = int(input())
        Account1.get(money)
    elif x==3:
        Account1.show()
    else:
        print("输入错误！请重新输入！")
