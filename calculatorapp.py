print('-'*135)
print(f"{"Calculator Project":^120}")
print('-'*135)
history = []

while True :
        print( f"""
            {'1. Addition':^100}
            {'2. Substraction':^104}
            {'3. Multiplication':^105}
            {'4. Division':^100}
            {'5. Floor Division':^106}
            {'6. Modulus':^99}
            {'7. Square':^98}
            {'8. Cube':^95}
            {'9. Exit':^95}
 """+ '-'*135)
        ch = int(input(f"{'Enter Your Choice : ':>70}"))
        if ch == 9 :
            print('-'*135)
            print(f"{"Calculator Histroy":^120}")
            print('-'*135)      
            if history :
                s = 0
                for h in history:
                    s+=1
                    print(f" {s:>43}.{h}")
                print('-'*135)


            else :
                print(f"{'No Operation Perform':^120}") 
                print('-'*135)


            break

        if ch not in [1,2,3,4,5,6,7,8,9]:
            print("enter youe choice between 1 to 9 ")
            continue
        num1 = float(input(f"{"Enter a number 1  : ":>70}"))
        num2 = float(input(f"{"Enter a number 2  : ":>70}")) 

        if ch == 1 :
            message = f" Addition of {num1} and {num2} = {num1 + num2}"
            print(f"{message:>78}")
            history.append(message)
           
        elif ch == 2 :
            message = f" Substraction of {num1} and {num2} = {num1 - num2}"
            print(f"{message:>78}")
            history.append(message)
            
        elif ch == 3 :
            message = f" Multipication of {num1} and {num2} = {num1 * num2}"
            print(f"{message:>78}")
            history.append(message)
         
        elif ch == 4 :
            if num2 > 0 :
                message = f"Division of {num1} and {num2} = {num1 / num2}"
                print(f"{message:>78}")
                history.append(message)
            else : 
                message1 = f"{'num2 is zero':^50}"
                print(message1)
           

        elif ch == 5 :
            if num2 > 0 :
                message = f"Floor Division of {num1} and {num2} = {num1 // num2}"
                print(f"{message:>78}")
                history.append(message)

            else : 
                message1 = f"{'num2 is zero':^50}"
                print(message1)


        elif ch == 6 :
            if num2 > 0 :
                message = f"Modlus of {num1} and {num2} = {num1 % num2}"
                print(f"{message:>78}")
                history.append(message)

            else : 
                message1 = f"{'num2 is zero':^50}"
                print(message1)
           

        elif ch == 7 :
            if num2 == 2 :
                message = f"square of {num1}  =  {num1**num2}"
                print(f"{message:>78}")
                history.append(message)
            else :
                message1 = f"{'please enter num2 = 2':^45}"
                print(message1)

        elif ch == 8 :
            if num2 == 3 :
                message = f"Cube of {num1}  =  {num1**num2}"
                print(f"{message:>78}")
                history.append(message)

            else :
                message1 = f"{'please enter num2 = 3':^45}"
                print(message1)
                
        print('-'*135)

        




