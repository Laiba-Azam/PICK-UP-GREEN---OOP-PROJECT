class Products:#This class is for management of Product store like adding or removing items from the store 
    def __init__(self):
        self.products=[]
    ID=0
    def set_item(self): #This method adds items to the store
        L=[]
        Products.ID+=1
        self.id=Products.ID
        name=input('Enter the name of the plant: ')
        type=input('Enter the type of the plant: ')
        price=int(input('Enter the price of the plant: '))
        quantity=int(input('Enter the number of the plants available: '))
        self.name,self.type,self.price,self.quantity=name,type,price,quantity
        self.products.append([self.id,name,type,price,quantity])
        L.append([self.id,name,type,price,quantity])
        f=open('Products(1).txt','a')
        for p in L:
            f.write(str(p[0])+',')
            f.write(p[1]+',')
            f.write(p[2]+',')
            f.write(str(p[3])+',')
            f.write(str(p[4])+'\n')
        f.close()            
                            
    def remove_product(self): #This method removes product from the store
        f=open('Products(1).txt','r')
        lines=f.readlines()
        f.close()

        new_file=open('Products(1).txt','w')
        n=input('Enter the name of the product to be removed: ')
        p=n.title()
        for line in lines:
            if n not in line:
                new_file.write(line)
        new_file.close()        
                          
    def display_products(self): #This method displays the list of products available in the store
        i='PRODUCT ID'
        a='PLANT NAME:'
        b='PLANT TYPE:'
        c='PRICE IN PKR:'
        #d='QUANTITY:'
        print(f'{i:20} {a:20} {b:28} {c:23} ')
        f=open('Products(1).txt','r')               
        for i in f:
            item=i.split(',')
            print(f'\n{item[0]:23} {item[1]:20} {item[2]:30} {item[3]:20}')
        f.close()


class Shopping_cart:  #This is the class for the buyer to add or remove the products in his cart
    c=[]
    c1=[]
    def __init__(self):
        self.obj_products=Products()
        self.cart=Shopping_cart.c
        self.list_of_products=[]
        self.obj_products.display_products()
        self.price=0
        self.current_cart=Shopping_cart.c1
        

    def convert_from_file(self):         
        f=open('Products(1).txt','r')
        for line in f:
            item=line.strip()
            item=item.split(',')
        #self.list_of_products=eval(f.read())
            self.list_of_products.append(item)
        f.close()

    def add_to_cart(self):
        self.L=[]
        name=input('Enter the name of the product you want to add to your cart:')      
        try:
            quantity=int(input('Enter the number of the plants you want to add: '))
        except ValueError:
            print('Enter the quantity in digits')
            quantity=int(input('Enter the number of plants available:')) 
        except:
            print('Something went wrong, Sorry! Please try again...')
            
        for item in self.list_of_products:
            
            if name in item:
                print('yes')
                self.price=item[3]
                print(self.price)   
            else: 
                price=0
        self.cart.append([name,quantity,self.price])
        self.L.append([name,quantity,self.price])
        self.Current_cart()

    def Current_cart(self):
        f=open('currentCart.txt','w')
        for p in self.L:
            f.write(str(p[0])+',')
            f.write(str(p[1])+',')
            f.write(str(p[2])+'\n')
            f.close()

        f=open('CurrentCart.txt','r')
        for line in f:
            item=line.strip()
            item=item.split(',')
            self.current_cart.append(item)
        f.close()

    def confirm(self):
        confirmation=int(input('1.Buy Now Or 2.Remove any product'))
        if confirmation==1:
            print('Hope you had a nice experience, Here you go!')
            print('Your bill is: ',Shopping_cart.Bill(self.current_cart))
            self.save_cart()
            #print(self.reduce_quantity())
            
        elif confirmation==2:      
            x=int(input('Enter the name of the plant you want to remove:'))
            for i in self.cart:
                if x in i:
                   self.cart.remove(i)
            self.save_cart()
            

    def reduce_quantity(self):
         i1=0
         i2=1
         i3=2
         i4=4
         for i in range(len(self.current_cart)):
             if self.list_of_products[i][i1]==self.current_cart[i][i1]:
                  (self.list_of_products[i][i4])-=(self.current_cart[i][i2])
         return (self.list_of_products)
         #print(self.list_of_products)
                

    def display_currentCart(self):
        a='PLANT NAME:'
        b='QUANTITY:'
        d='PRICE:'
        print(f'{i:20} {a:20} {b:28} {c:23} {d:20}')
        f=open('CurrentCart.txt','r')               
        for i in f:
            item=i.split(',')
            print(f'\n{item[0]:23} {item[1]:20} {item[2]:30}')
        f.close()


    def save_cart(self):         #Ye buy now k baad chalega
        f=open('cart(2).txt','w')
        for product in self.cart:
            f.write(str(product)+'\n')
        f.close()
    def save_cart_1(self):
        f=open('cart_1.txt','a')
        for p in self.cart:
            f.write(str(p)+'\n')
        f.close

    @staticmethod          #This static method calculates the total bill generated by taking the instance attribute of current cart as argument
    def Bill(x):
        s1=0
        for item in x:
            s1+=(int(item[1])*int(item[2]))
        result=s1
        return result


    def check_cart(self):
        #i='PRODUCT ID'
        a='PLANT NAME:'
        #b='PLANT TYPE:'
        c='PRICE IN PKR:'
        d='QUANTITY:'
        print(f' {a:20} {d:15} {c:20}')
        f=open('cart(2).txt','r')
        items=f.readlines()                
        for i in items:
            item=i.split(',')
            print(f'\n{item[0]:23} {item[1]:20} {item[2]:30}')
        f.close()


class user:
    def __init__(self,name,password):
        self.name=name
        self.password=password


class admin(user):
    def __init__(self,name,password):
        user.__init__(self,name,password)

class customer(user):
    a=[]
    def login(self,name,password):
        
        user.__init__(self,name,password)
    def signup(self,name,password,email,phone_no,payment_method):
        user.__init__(self,name,password)
        self.email=email
        self.phone_no=phone_no
        self.payment_method=payment_method
        customer.a.append(self.name)
        customer.a.append(self.password)
        customer.a.append(self.email)
        customer.a.append(self.phone_no)
        customer.a.append(self.payment_method)
        self.info1=[]
        self.info1.append([self.name,self.password,self.email,self.phone_no,self.payment_method])
        f=open('customerinfo.txt','a')
        for p in self.info1:
            f.write(str(p[0])+',')
            f.write(p[1]+',')
            f.write(p[2]+',')
            f.write(str(p[3])+',')
            f.write(str(p[4])+'\n')
        f.close()
        f=open('cart_ 1.txt','a')
        for p in self.info1:
            f.write('customer info '+'\n')
            f.write(str(p[0])+',')
            f.write(p[1]+',')
            f.write(p[2]+',')
            f.write(str(p[3])+',')
            f.write(str(p[4])+'\n')
        f.close()
class abc(customer,Shopping_cart):
    def a(self):
        u=(customer.a+Shopping_cart.c)
        f=open('history.txt','a')
        f.write(str(u)+'\n')
        f.close()
    def b(self):
        p=input('your password ')
        f=open('history.txt','r')
        for i in f:
            if p in i:
                print(i)#yahan pr sahi wala jesay print krti ho tum woh krwado woh mujhay nhi arha
            else:
                pass
        f.close()
    def c(self):
        p=input('enter your password ')
        f=open('history.txt','r')
        for i in f :
            if p in i:
                f.write(str(i[5])+str(Shopping_cart.c1))
            else:
                pass
        f.close()
    #def d(self):
    
        
        
        

#class CustomerHistory(customer,Shopping_cart):
    #def __init__(self):
        #self.customer_info=[]
        
    #def Add_History(self):
        #f=open('customerinfo.txt','r')
        #for line in f:
            #item=line.strip()
            #item=item.split(',')
            #self.customer_info.append(item)
        #f.close()

        #for customer in self.customer_info(self):
            #history=

    

from abc import ABC, abstractmethod
class Interface:
    def __init__(self):
        self.MainMenu()
    @abstractmethod
    def MainMenu(self):
        pass

    
class UserInterface(Interface):
    def __init__(self):
        print('**************************************************Welcome to PICK UP GREEN!!!***************************************************************')
        self.MainMenu()

    def MainMenu(self):
        print('Do You want to enter the application as a customer or as an admin?')
        c=input()
        if c=='admin' or c=='ADMIN'or c=='Admin':
             while True:
                C1=input('press any key to teminate and c to continue ')
                if C1=='C' or C1=='c':
                  na=input('enter your name ')
                  pa=input('enter password ')#enter this 11234
                  if pa=='11234':
                      a=admin(na,pa)
                      p=Products()
                      n=input('''1:ADD PLANT
2:DISPLAY STOCK
3: REMOVE PLANT
4: EXIT''')
                      if n=='1':
                          n2=int(input('How many new plants do you want to add to your store?'))
                          for i in range(n2):
                              p.set_item()
                          p.display_products()

                      elif n=='3':
                          n3=int(input('How many products do you want to remove? Enter in digits:'))
                          for i in range (n3):
                              p.remove_product()
                          p.display_products()
                      elif n=='2':
                          p.display_products()
                          
                      else:
                          break
                  else:
                       print('Incorrect Password...!!!')
                else:
                    print('Have a good day!')
                    break

        elif c=='customer' or c=='Customer' or c=='CUSTOMER':
            a=int(input('''press
1 for login
2 for signup to make account'''))
            if a==2:
                na=input('Enter your name: ')
                pa=input('Enter your password: ')
                e=input('Enter your email address: ')
                ph=input('Enter your phone number in digits: ')
                pm=input('Enter the payment method: ')
                cus=customer(na,pa)
                cus.signup(na,pa,e,ph,pm)
                s=Shopping_cart()
                try:
                    n3=int(input('Enter the number of plants you want to buy: '))
                except ValueError:
                    print('Enter the quantity in digits please!')
                    n3=int(input())
                except:
                    print('Something went wrong, Soory! Please enter the number again...')
                    n3=int(input())
                for i in range(n3):
                    s.convert_from_file()
                    s.add_to_cart()
                s.save_cart_1()
                s.confirm()
                s.check_cart()
                b=abc(na,pa)
                b.a()
            elif a==1:
                na=input('enter your name: ')
                pa=input('enter your password: ')
                cus=customer(na,pa)
                cus.login(na,pa)
                b=abc(na,pa)
                n=input('do you want to see your history?write yes or no :')
                if n=='yes' or n=='YES' or n=='Yes':
                    b.b()
                elif n=='no' or n=='NO' or n=='No':
                    print('thankyou')
                s=Shopping_cart()
                try:
                    n3=int(input('Enter the number of plants you want to buy: '))
                except ValueError:
                    print('Enter the quantity in digits please!')
                    n3=int(input())
                except:
                    print('Something went wrong, Soory! Please enter the number again...')
                    n3=int(input())
                for i in range(n3):
                    s.convert_from_file()
                    s.add_to_cart()
                s.save_cart_1()
                s.confirm()
                s.check_cart()
                b.c()
            #b.b()

                                                                
#DriverCode
User=UserInterface()

    
