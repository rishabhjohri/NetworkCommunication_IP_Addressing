def b2d(n):
    s = 0
    for i in range(len(n)):
        j = len(n)-i-1
        s = s + (2**i)*int(n[j])
    return s
def d2b(n):
    s = ''
    if n==0:
        s = '0'
    while n>0:
        s = s + str(n%2)
        n = n//2
    b = s[::-1]
    if len(b)==8:
        return b
    else:
        return (8-len(b))*'0'+b

def dec2bin(IP):
    l = IP.split(".")
    l1 = []
    for i in l:
        l1.append(d2b(int(i)))
    return l1

def bNOT(B):
    B1 = ''
    for i in B:
        if i == '0':
            B1 = B1+'1'
        else:
            B1 = B1+'0'
    return B1
def AND(b1,b2):
    if b1=='1' and b2=='1':
        return '1'
    else:
        return '0'
def OR(b1,b2):
    if b1=='0' and b2=='0':
        return '0'
    else:
        return '1'
    
def bAND(B1,B2):
    ans = ''
    for i in range(len(B1)):
        ans = ans + AND(B1[i],B2[i])
    return ans
def bOR(B1,B2):
    ans = ''
    for i in range(len(B1)):
        ans = ans + OR(B1[i],B2[i])
    return ans

def a_c():
    IP = input("Enter IP address in binary:")
    MASK = input("Mask in binary:")
    l1 = IP.split()
    l2 = MASK.split()
    mask = ''
    for m in l2:
        mask = mask + m
    print("Number of addressses:",b2d(bNOT(mask))+1)
    print("1st address:")
    first = ''
    for i in range(len(l1)):
        first = first + bAND(l1[i],l2[i])+"."
    print(first[0:len(first)-1])
    print("last address:")
    l22 = []
    for var in l2:
        l22.append(bNOT(var))
    last = ''
    for i in range(len(l1)):
        last = last + bOR(l1[i],l22[i])+"."
    print(last[0:len(last)-1])
         
def bin2dec(IP):
    l = IP.split()
    ip=""
    c = 1
    for i in l:
        if c!=4:
            ip = ip + str(b2d(i))+"."
        else:
            ip = ip + str(b2d(i))
        c=c+1
    return ip



def IPclass(IP_d):
    l = IP_d.split('.')
    a = int(l[0])
    if a in range(0,128):
        c = 'A'
    elif a in range(128,192):
        c = 'B'
    elif a in range(192,224):
        c = 'C'
    elif a in range(224,240):
        c = 'D'
    elif a in range(240,256):
        c = 'E'
    else :
        c = 'invalid'
    return c

def net_host_id(IP_d):
    l = IP_d.split('.')
    c  = IPclass(IP_d)
    if c == 'A':
        print("Network id:",l[0])
        print("Host id:",l[1]+"."+l[2]+"."+l[3])
    elif c == 'B':
        print("Network id:",l[0]+"."+l[1])
        print("Host id:",l[2]+"."+l[3])
    elif c == 'C':
        print("Network id:",l[0]+"."+l[1]+"."+l[2])
        print("Host id:",l[3])
    else:
        print("In this Class, IP address is not divided into Network and Host ID")
        
def validate_IP_b():
    flag = 1
    IP = input("Enter IP address (eg: 11000000 10101010 11110000 00000000)")
    l = IP.split()
    if len(l)!=4:
        flag=0
    for var in l:
        if len(var)!=8:
            flag=0
            break
    for i in l:
        if set(i).union({'0','1'})!= {'0','1'}:
            flag = 0
            break
    if flag ==1:
        print("Valid")
    else:
        print("Invalid")
    
def validate_IP_d():
    IP = input("Enter IP addess(Example: 191.10.10.1)")
    l = IP.split(".")
    flag = 1
    if len(l) != 4:
        flag=0
    for var in l:
        if var.isnumeric()=="False":
            flag = 0
            break

    if flag==1:
        for v in l:
            if v[0]=='0':
                flag = 0
                break
        for i in l:
            if int(i) not in range(0,256):
                flag =0
                break
    if flag == 0:
        print("invalid")
    else:
        print("Valid")
            
def b_c():
    IP = input("Enter IP address:")
    MASK = input("Mask:")
    l1 = dec2bin(IP)
    l2 = dec2bin(MASK)
    mask = ''
    for m in l2:
        mask = mask + m
    print("Number of addressses:",b2d(bNOT(mask))+1)
    print("1st address:")
    first = []
    for i in range(len(l1)):
        first.append(b2d(bAND(l1[i],l2[i])))
    f = ''
    for var in first:
        f = f + str(var) +"."
    print(f[0:len(f)-1])
    print("last address:")
    l22 = []
    for var in l2:
        l22.append(bNOT(var))
    last = []
    for i in range(len(l1)):
        last.append(b2d(bOR(l1[i],l22[i])))
    L = ''
    for var in last:
        L = L + str(var) +"."
    print(L[0:len(L)-1])
   
def menu():
    print("a. To check the class, network id and host id of an IPv4 address.\nb. To check whether given IP address is valid or not.\nc. To find first address, last address and number of addresses in the block.")

print("a)Binary\nb)Decimal")
c = input("Enter choice a or b: ")
if(c not in {'a','b'}):
    print("Invalid choice")
if c=='a':
    menu()
    choice = input("Enter a,b or c: ")
    if choice == "a":
        IP = input("Enter IP address(eg:11111111 10101010 00000000 00000000)")
        IP_d = bin2dec(IP)
        address_class = IPclass(IP_d)
        print("Class :",address_class)
        net_host_id(IP_d)
        
    elif choice =="b":
        validate_IP_b()
    elif choice == "c":
        a_c()
    else:
        print("invalid choice")
elif c=='b':
    menu()
    choice = input("Enter a,b or c: ")
    if choice == "a":
        IP = input("Enter IP address(eg: 111.56.45.78)")
        print("Class :",IPclass(IP))
        net_host_id(IP)
        
    elif choice =="b":
        validate_IP_d()
    elif choice == "c":
        b_c()
    else:
        print("invalid choice")
        


