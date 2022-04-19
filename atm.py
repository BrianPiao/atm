class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def checkBalance (self):
        print ("balance is 1000000000..")
    def withdrawl (self):
        print ("withdrawl is 1..")

def main():
    atm_obj = Atm( 9, 69420)
    atm_obj.checkBalance()
    atm_obj.withdrawl()
if __name__=="__main__":
    main ()