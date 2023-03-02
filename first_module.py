import array

pin=array.array('i',[1234])

def main():
    print("this is a module ,it's not meant for you to run --its literally called first_module.py")

if __name__=="__main__":
    main()

def start():
    print("Welcome to your online banking app")
    print("Your default pin is 1234")

def human_check():
    lst=[1,2,3,4,5,6,7,8,9]
    print("Are you human? proof to me ")
    print(lst)
    even =list(filter(lambda a: a%2==0,lst))
    for i in lst:
        answer=[]
        for x in range(4):
            typin=int(input("enter even number {} in the list above to prove your human :".format(x)))
            answer.append(typin)
        if even == answer:
            print("Now we are certain that your human , you may proceed")
            break
        else:
            if i!=9:
                print("Are sure your human","try again","you have {} more trials".format(9-i) )
                continue
            else:
                print("your not human , or maybe your not smart enough to be classified as one")
            break

def autentication(input_pin):
    global pin
    if pin[0]==input_pin:
        print("PIN correct you may proceed")
    else:
        print("incorrect PIN")
def pin_change():
    global pin
    for x in range(3):
        new_pin=int(input("input pin : "))
        if x==2:
            print("you have reached maximun trial can't try again")
            break
        if new_pin<=9999 and new_pin>=1000:
            pin[0]=new_pin
            print("PIN successfully changed")
            break
        else:
            print("invalid PIN try again")
