import math
print("Welcome to Data structure calculator")
print("Select option from below list")
print("1. Number")
print("2. List")
print("3. Sets")
print("4. Strings")
print("5. Tuples")
print("6. Dictionary")
print("7. Data Structure")
user_option = int(input("Enter the number to performoperation:"))
if user_option == 1:
    User_operation_performed=""
    print("Select the type of operation to be performed from below list")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Power")
    print("7. Module")
    print("8. Square")
    print("9. Square root")
    print("10. Cube")
    print("11. Cuberoot")
    print("12. Prime number")
    print("13. Armstrong")
    print("14. Fibbonaci")
    print("15. Factorial")
    print("16. odd/even")

while(user_option==1):
    user_operation_performed = int(input('Enter the number to perform type of operation:'))
    if user_operation_performed ==1:
        a= int(input("Enter the first value in integer:"))
        b= int(input("Enter the second valuein integer:"))
        c= a+b
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==2:
        a= int(input("Enter the first value in integer:"))
        b= int(input("Enter the second valuein integer:"))
        c= a-b
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==3:
        a= int(input("Enter the first value in integer:"))
        b= int(input("Enter the second valuein integer:"))
        c= a*b
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==4:
        a= int(input("Enter the first value in integer:"))
        b= int(input("Enter the second valuein integer:"))
        c= a/b
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")
            
    if user_operation_performed ==5:
        a= int(input("Enter the first value in integer:"))
        b= int(input("Enter the second valuein integer:"))
        c= a//b
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==6:
        a= int(input("Enter the first value in integer:"))
        b= int(input("Enter the second valuein integer:"))
        c= (math.pow(a,b))
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==7:
        a= int(input("Enter the first value in integer:"))
        b= int(input("Enter the second valuein integer:"))
        c= a%b
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==8:
        a= int(input("Enter the value in integer:"))
        c= a*a
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==9:
        a= int(input("Enter the value in integer:"))
        c= (math.sqrt(a))
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==10:
        a= int(input("Enter the value in integer:"))
        c= a*a*a
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==11:
        a= int(input("Enter the value in integer:"))
        c= a**(1/3)
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")
            
    if user_operation_performed ==12:
        a= int(input("Enter the first value in integer:"))
        if a>1:
            for i in range(2,a):
                if a%i==0:
                    print("Given number",a,"is not a prime number")
                    break
            else:
                print("Given number",a,"is a prime number")
        
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==13:
        a=int(input("Enter the value in integer:"))
        final=0
        num=a
        count=0
        divisor=10
        while (num!=0):
            num=int(a/divisor)
            divisor=divisor*10
            count=count+1
        divisor=int(divisor/100)
        initial=a
        while(int(divisor)!=0):
            b= int((a-(a%divisor))/divisor)**count
            final= (final+b)

            a= a-(int((a-(a%divisor))/divisor)*divisor)
            divisor=divisor/10
        if (final==initial):
            print('Given Value is an Armstrong Number')
        else:
            print('Given Value is not an Armstrong Number')

        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed==14:
        a=int(input("Enter the value in integer:"))
        x=0
        y=1
        if (a<=0):
            print("Invalid Number")
        elif a==1:
            print(x)
        else:
            for i in range (0,a):
                print(x)
                z=x+y
                x=y
                y=z
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==15:
        a=int(input("Enter the value in integer:"))
        c=1
        for i in range(1,a+1):
            c=c*i
        print("Result: "+ str(c))
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==16:
        a=int(input("Enter the value in integer:"))
        if a%2==0:
            print("Given Value "+str(a)+",is an even number")
        else:
            print("Given Value "+str(a)+"is an odd number")
        print("Do you want to perform some more operations in Numbers")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


if user_option ==2:
    User_operation_performed=""
    a=[]
    print("Select the type of Operation to be performed from below list")
    print("1. Create List")
    print("2. Length of List")
    print("3. Minimum value of List")
    print("4. Maximum value of List")
    print("5. Insert element to List")
    print("6. SortList")
    print("7. Remove element from List")
    print("8. Pop")
    print("9. Concat List")
    print("10. Indexing")
    print("11. Slicing")
    print("12. Replace element")
    print("13. Duplicate element")
    print("14. Extend List")
    print("15. Delete List")

while(user_option==2):
    print("To perform any operation in list. Please create the list at first")
    
    user_operation_performed = int(input("Enter the number to perform type of operation:"))
    if user_operation_performed ==1:
        print("Do you want to create an empty list?")
        create_list = input("Press Y to create empty list or N to create non empty list:")
        if create_list=='Y' or create_list=='y':
            print(a)
        elif create_list== 'N' or create_list=='n':
            list_element_count =int(input("Enter the number elements to add to list:"))
            for i in range (0,list_element_count):
                list_element_value =input(("Enter the value to be stored in list:"))
                a.append(list_element_value)
            print(a)
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==2:
        list_len = len(a)
        print("length of list is:"+str(list_len))
        if list_len ==0:
            print("List is empty. Below is the length of list. Request you to create a list with data and proceed for further opeations")
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==3:
        print(a)
        c= min(a)
        print("Minimum Value in list is : "+str(c))
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==4:
        print(a)
        c= max(a)
        print("Maximum Value in list is : "+str(c))
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")       
                                   
          
    if user_operation_performed ==5:
        print(a)
        c= (input("Enter the value to be inserted in above List : "))
        d= int(input("Enter the position to insert the value in above List : "))
        a.insert(d,str(c))
        print("Updated list is as below : ")
        print(a)
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")
        
    if user_operation_performed ==6:
        print(a)
        a.sort()
        print("Sorted list is as below : ")
        print(a)
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==7:
        print("Since you have choosen to remove an element. Kindly enter the value from list to remove")
        print(a)
        c=(input("Enter the value to be removed from above list : "))
        a.remove(str(c))
        print(a)
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==8:
        print(a)
        c=int(input("Enter the index value to pop an element from above list : "))
        a.pop(c)
        print(a)
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==9:
        print(a)
        list_element_count = int(input("Enter the number elements to concat to list : "))
        empty_list=[]
        for i in range (0,list_element_count):
            
            list_element_value = input(("Enter the value to be stored in list : "))
            empty_list.append(list_element_value)
        print(empty_list)
        a=a+empty_list
        print(a)
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==10:
        print(a)
        list_element_count = int(input("Enter the indexing value : "))
        print(a[list_element_count])
        print("Do you want to perform some more operations in List")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==11:
        print("Maximum 2 values are allowed for slicing")
        user_input = input("Enter the string : ")
        user_choice = int(input("Enter the number of values for slicing : "))
        if user_choice ==1:
            user_input1= int(input("Enter the value for slicing : "))
        
            print(user_input[user_input1:])
        if user_choice==2:
            user_input1= int(input("Enter the First value for slicing : "))
            user_input2= int(input("Enter the Second value for slicing : "))
            print(user_input[user_input1:user_input2])

        user_continue = str(input("Press Y to continue and N for exit : "))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            
            print("Wrong option")            
                
            
            
    if user_operation_performed ==12:
        print(a)
        f=len(a)
        Replace_Value = int(input("Enter the value to be replaced : "))
        Replace_Value_With =  int(input("Enter the value to be replaced with : "))
        for i in range (0,f):
            if a[i]==str(Replace_Value):
                a[i]=str(Replace_Value_With)
        print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    #if user_operation_performed ==13:



    if user_operation_performed ==14:
        print(a)
        list_element_count = int(input("Enter the number elements to extend the above list : "))
        empty_list=[]
        for i in range (0,list_element_count):
            
            list_element_value = input(("Enter the value to be stored in list : "))
            empty_list.append(list_element_value)
        print(empty_list)
        a.extend(empty_list)
        print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")
        
    if user_operation_performed ==15:
        print(a)
        del a
        print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


if user_option ==3:
    User_operation_performed=""
    a=set()
    print("Select the type of Operation to be performed from below list")
    print("1. Create Set")
    print("2. Duplicate set")
    print("3. Add element to set")
    print("4. Remove element from set")
    print("5. Delete Set")

while(user_option==3):
    print("To perform any operations in set. Please create the set at first")
    user_operation_performed = int(input("Enter the number to perform type of operation : "))


    if user_operation_performed ==1:
        print("Do you want to create an empty set?")
        create_list = input("Press Y to create empty set or N to create non empty set : ")
        if create_list=='Y' or create_list=='y':
            #a=[]
            print(a)
        elif create_list=='N' or create_list=='n':
            list_element_count = int(input("Enter the number elements to add to set : "))
            for i in range (0,list_element_count):
                list_element_value = input(("Enter the value to be stored in set : "))
                a.add(list_element_value)
            print(a)
        print("Do you want to perform some more opeartions in Sets")            
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==2:
        new_set=a.copy()
        print(new_set)
        print("Do you want to perform some more opeartions in Sets")            
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==3:
        list_element_count = int(input("Enter the number elements to add to set : "))
        for i in range (0,list_element_count):
                list_element_value = input(("Enter the value to be stored in set : "))
                a.add(list_element_value)
        print(a)
        print("Do you want to perform some more opeartions in Sets")            
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==4:
        print(a)
        user_input = input("Please choose an element from above set to remove : ")
        a.remove(user_input)
        print(a)
        print("Do you want to perform some more opeartions in Sets")            
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==5:
        print(a)
        a.clear()
        print(a)
        print("Do you want to perform some more opeartions in Sets")            
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")



if user_option ==4:
    print("Select the type of Operation to be performed from below list")
    print("1. Length of string")
    print("2. Revese a string")
    print("3. Join Strings")
    print("4. Split String")
    print("5. Add two strings")
    print("6. starts with")
    print("7. ends with")
    print("8. replace")
    print("9. Palindrome")
    print("10. Vowles")
    print("11. Ascii")

while(user_option==4):
    user_operation_performed = int(input("Enter the number to perform type of operation:"))

    if user_operation_performed ==1:
        user_input = input("Enter the string:")
        a= len(user_input)
        print("Length of string is : "+str(a))
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==2:
        user_input =input("Enter the string :")
        a= user_input[::-1]
        print("Reversed string is :"+a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==3:
        user_input =int(input("Enter the number of words to Join:"))
        b=[]
        for i in range(0,user_input):
            user_input1= input("Enter the string:")
            b.append(user_input)
        d=" ".join(b)
        print(d)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==4:
        user_input = (input("Enter the string : "))
        user_input_split = input("Enter the value based above string on which string has to split : ")
        e=user_input.split(user_input_split)
        print(e)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==5:
        user_input = int(input("Enter the nuber of strings to be concatenate : "))
        e=""
        for i in range(0,user_input):
            user_input_string = input("Enter the string : ")
            e=e+user_input_string
        print(e)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")       
        

    if user_operation_performed ==6:
        str1=input("Enter the string : ")
        user_input = (input("Enter the character to check starts with : "))
        e=str1.startswith(user_input)
        print(e)       
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==7:
        str1=input("Enter the string : ")
        user_input = (input("Enter the character to check ends with : "))
        e=str1.endswith(user_input)
        print(e)          
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==8:
        str1=input("Enter the string : ")
        user_input = (input("Enter the letter to be replace : "))
        user_input1=input("Enter the replacement letter : ")
        e=str1.replace(user_input,user_input1)
        print(e)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==9:
        user_input=input("Enter the string to check palindrome : ")
        a=user_input[::-1]
        if(user_input==a):
            print("Given string is a palindrome")
        else:
            print("Given string is not a palindrome")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==10:
        str1=input("Enter the string : ")
        a=0
        for i in str1:
            if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i'or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
               a=a+1
        print("Number of vowels are : "+str(a))
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==11:
        str1=input("Enter the string : ")
        print(ascii(str1))
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")



if user_option ==5:
    a=[]
    print("Select the type of Operation to be performed from below list")
    print("1. Create Tuple")
    print("2. Delete Tuple")
    print("3. Slicing")
    print("4. Indexing")
    print("5. Assign")

while(user_option==5):
    print("To perform any operations in Tuple. Please create the Tuple at first")
    user_operation_performed=int(input("Enter the Number to perform type of operation:"))
    if user_operation_performed ==1:
        print("Do you want to create an empty Tuple?")
        create_list = input("Press Y to create empty Tuple or N to create non empty Tuple")
        if create_list=="Y" or create_list=='y':
            print(tuple(a))
        elif create_list=="N" or create_list=='n':
            list_element_count = int(input("Enter the number elements to add to Tuple:"))
            for i in range (0,list_element_count):
                list_element_value = input(("Enter the value to be stored in Tuple:"))
                a.append(list_element_value)
            a=(tuple(a))
            print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==2:
        print((a))
        del a
        print("After deleting")
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


   #if user_operation_performed ==3:
            




    if user_operation_performed ==4:
        print(a)
        user_input = int(input("Please provide an index value : "))
        a=a[user_input]
        print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

              
    if user_operation_performed ==5:
        user_input= int(input("Enter the assigingn value : "))
        b=a[user_input:]
        print(b)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")



if user_option ==6:
    a={}
    print("Select the type of opeartion to be performed from below list")
    print("1. Create Dictionary")
    print("2. Add element")
    print("3. Remove element")
    print("4.Remove last elements")
    print("5. Keys")
    print("6. Values")
    print("7. Items")
    print("8. Replace")

while(user_option==6):
    print("To perform any operations in Dictionary. Please create the Dictionary at first")
    print("Please enter only integer values for Keys values")
    user_operation_performed=int(input("Enter the Number to perform type of operation:"))

    if user_operation_performed ==1:
        print("Do you want to create an empty Dictionary?")
        create_list = input("Press Y to create empty Dictionary or N to create non empty Dictionary:")
        if create_list=="Y" or create_list=='y':
            print(a)
        elif create_list=="N" or create_list=='n':
            list_element_count = int(input("Enter the number elements to add to dictionary:"))
            for i in range (0,list_element_count):
                list_element_value = input(("Enter the value to be stored in dictionary:"))
                a[i]=(list_element_value)
        print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==2:
        user_input = int(input("Enter the Key value : "))
        user_value = input("Enter the value : ")
        a[user_input]=user_value
        print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")            
            

    if user_operation_performed ==3:
        user_input= int(input("Enter the key value : "))
        a.pop(user_input)
        print(a)     
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option") 


    if user_operation_performed ==4:
        a.popitem()
        print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option") 


    if user_operation_performed ==5:
        print(a.keys())
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==6:
        print(a.values())
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==7:
        print(a.items())
        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")


    if user_operation_performed ==8:
        user_input = int(input("Enter the Key value to be replaced : "))
        user_value = input("Enter the value to be replaced with : ")
        a[user_input] = a[user_value]
        user_continue = str(input("Press Y to continue and N for exit:"))        
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")



if user_option ==7:  
    a=[]
    print("Select the type of Operation to be performed from below list")
    print("1. Stack")
    print("2. Queue")

while(user_option==7):
    user_operation_performed = int(input("Enter the number to perform type of operation:"))

    if user_operation_performed==1:
        print("To perform any operations in DS. Please create the list at first")
        print("Below operations can be performed in stack")
        print("1. Push")
        print("2. Pop")
        print("Do you want to create an empty list?")
        create_list = input("Press Y to create empty list or N to create non empty list:")
        if create_list=="Y" or create_list=="y":
            print(a)
        elif create_list=="N" or create_list=="n":
            list_element_count = int(input("Enter the number elements to add to list : "))
            for i in range (0,list_element_count):
                list_element_value = input(("Enter the value to be stored in list : "))
                a.append(list_element_value)
            print(a)
            
        user_option=int(input("Select the type of operation to be performed in stack:"))

        if user_option ==1:
            user_input=input("Enter the value to be pushed in stack:")
            a.append(user_input)
            print(a)

        if user_option ==2:
            a.pop()
            print(a)
        user_continue = str(input("Press Y to continue and N for exit:"))            
        if user_continue == "Y" or user_continue =="y":
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")

    if user_operation_performed ==2:
        print("To perform any operations in DS. Please create the list at first")
        print("Below operations can be performed in Queue")
        print("1. Enqueue")
        print("2. Dequeue")
        print("Do you want to create an empty list?")
        create_list = input("Press Y to create empty list or N to create non empty list : ")
        if create_list=='Y' or create_list=='y':
            print(a)
        elif create_list=='N' or create_list=='n':
            list_element_count = int(input("Enter the number elements to add to list : "))
            for i in range (0,list_element_count):
                list_element_value = input(("Enter the value to be stored in list : "))
                a.append(list_element_value)
          
            print(a)
            
        user_option=int(input("Select the type of operation to be performed in queue : "))
        if user_option ==1:
            user_input=input("Enter the value to be enqueued in queue : ")
            a.append(user_input)
            print(a)
        if user_option ==2:
            a.pop(0)
            print(a)             

        user_continue = str(input("Press Y to continue and N for exit:"))
        if user_continue == "Y" or user_continue =='y':
            print("Thanks for choosing continue")
        elif user_continue == "N" or user_continue =='n':
            print("Thanks for your Input. Since you have choosen N, we are exiting from this module")
            break
        else:
            print("Wrong option")           
