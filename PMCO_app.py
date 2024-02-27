import streamlit as st
import math
from bg_ui import page_config
from PIL import Image


def main():
    operation = page_config()

    #Addition
    if operation == "Addition":
        def Addition(lst):
            s = 0
            for i in lst:
                s += i  
            return s

        lst_element = st.text_input("Enter the elements of the list (separated by space):")
        lst = list(map(int, lst_element.split()))
        st.write("Addition of the given numbers is:", Addition(lst))
    
    #Substraction
    elif operation == "Substraction":
        def Subtraction(lst):
            result = lst[0]  # Initialize result with the first element
            for i in lst[1:]:
                result -= i  # Subtract each element from the current result
            return result

        lst_element = st.text_input("Enter the elements of the list (separated by space):")
        lst = list(map(int, lst_element.split()))
        st.write("Subtraction of the given numbers is:", Subtraction(lst))
    
    #Multiplication:
    elif operation == "Multiplication":
        def Multiplication(lst):
            s = 1
            for i in lst:
                s *= i  
            return s

        lst_element = st.text_input("Enter the elements of the list (separated by space):")
        lst = list(map(int, lst_element.split()))
        st.write("Multiplication of the given numbers is:", Multiplication(lst))

    #Division
    elif operation == "Division":
        num1 = st.number_input("Give the first value:", min_value=1, value=1)
        num2 = st.number_input("Give the second value:", min_value=1, value=1)

        if num2 != 0:
            result = num1 / num2
            st.success(f"Division of given values is {result}")
        else:
            st.error("Cannot divide by zero. Please choose a non-zero value for the second number.")

    #Modulus
    elif operation == "Modulus":
        num1 = st.number_input("Give first value:", min_value=1, value=1)
        num2 = st.number_input("Give second value:", min_value=1, value=1)
        st.success(f"Modulus of the given value is {num1%num2}")

    #Exponential
    elif operation == "Exponential":
        num1 = st.number_input("Give first value:", min_value=1, value=1)
        num2 = st.number_input("Give second value:", min_value=1, value=1)
        st.success(f"Exponential of the given value is {num1**num2}")
    
    #Floar division
    elif operation == "Floar division":
        num1 = st.number_input("Give first value:", min_value=1, value=1)
        num2 = st.number_input("Give second value:", min_value=1, value=1)
        st.success(f"Floar division of the given value is {num1//num2}")

    #Square_of_number_upto_specific_number
    elif operation == "Square_of_number_upto_specific_number":
        def Square_of_number_upto_specific_number(num):
            squares = [i**2 for i in range(1, num + 1)]
            return squares

        num = st.number_input("Enter the Value:", min_value=0, value=0)

        squares_result = Square_of_number_upto_specific_number(num)
        st.write(squares_result)

    #Cube
    elif operation == "Cube":
        num1=st.number_input("Enter the Value:",min_value=1, value=1)
        sum_value = 0
        temp = num1
        while temp > 0:
            digit = temp % 10
            sum_value = num1 ** 3 # digit ** 3
            temp = temp// 10
        st.success(f"Cube of the given number is {sum_value}")

    #Computepay
    elif operation == "Computepay":
        days=st.number_input("Enter the Value:",min_value=1, value=1)
        if(days<=40):
            ans = days * 10
            st.success(f"Compute Pay of the given number of days is {ans}")
        elif(days>40):
            n=days-40
            ans = 40*10+n*1.5*10
            st.success(f"Compute Pay of the given number of days is {ans}")
    
    #Fibonnaci_series
    elif operation == "Fibonnaci_series":
        def Fibonacci(num):
            if num<= 0:
                st.warning(f"Incorrect input")
            elif num == 1:
                st.success(f"fibonacci value of 1 is 0")
            elif num == 2:
                st.success(f"Fibonacci value of 2 is 1")
            else:
                return Fibonacci(num-1)+Fibonacci(num-2)
        num=st.number_input("Enter the Value:",min_value=0, value=0)
        
        st.success(f"Fibonacci value of is, {Fibonacci(num)}")

    #list_of_even
    elif operation == "list_of_even":
        def list_of_even(num):
            for i in range (1,num+1):
                if (i%2==0):
                    st.write(i)
        num=st.number_input("Enter the Value:",min_value=0, value=0)
        st.write(f"This is list of even number upto {num} {list_of_odd(num)}")

    #list_of_odd    
    elif operation == "list_of_odd":
        def list_of_odd(num):
            for i in range (1,num+1):
                if (i%2!=0):
                    st.write(i)    

        num=st.number_input("Enter the Value:",min_value=0, value=0)
        st.write(f"This is list of odd number upto {num} {list_of_odd(num)}")

    #list_intersection
    elif operation == "list_intersection":
        def list_intersection(lst1, lst2):
            lst3 = [value for value in lst1 if value in lst2]
            return lst3

        lst1_element = st.text_input("Enter the elements of the first list (separated by space):")
        lst1 = lst1_element.split()

        lst2_element = st.text_input("Enter the elements of the second list (separated by space):")
        lst2 = lst2_element.split()

        result = list_intersection(lst1, lst2)
        st.write(f"List_intersection between both list is: {result}")


    #list_difference
    elif operation == "list_difference":
        def list_difference(lst1, lst2):
            lst3 = [value for value in lst1 if value not in lst2]
            return lst3

        lst1_element = st.text_input("Enter the elements of the first list (separated by space):")
        lst1 = lst1_element.split()

        lst2_element = st.text_input("Enter the elements of the second list (separated by space):")
        lst2 = lst2_element.split()

        result = list_difference(lst1, lst2)
        st.write(f"This are list_difference in first list is: {result}")


    #list_symmetric_difference
    elif operation == "list_symmetric_difference":
        def list_symmetric_difference(lst1, lst2):
            sym_diff = [value for value in lst1 + lst2 if (value in lst1 and value not in lst2) or (value in lst2 and value not in lst1)]
            return sym_diff

        lst1_element = st.text_input("Enter the elements of the first list (separated by space):")
        lst1 = lst1_element.split()

        lst2_element = st.text_input("Enter the elements of the second list (separated by space):")
        lst2 = lst2_element.split()

        ans = list_symmetric_difference(lst1, lst2)
        st.write(f"This are list_symmetric_difference between two list {ans}")

    #longest_increasing_subsequence
    elif operation == "longest_increasing_subsequence":
        def longest_increasing_subsequence(lst):
            num = len(lst)
            lis = [1] * num
            for i in range(1, num):
                for j in range(0, i):
                    if lst[i] > lst[j] and lis[i] < lis[j] + 1:
                        lis[i] = lis[j] + 1
            maximum = 0
            for i in range(num):
                maximum = max(maximum, lis[i])
            return maximum

        lst_element = st.text_input("Enter the elements of the list (separated by space):")
        lst = list(map(int, lst_element.split()))

        ans = longest_increasing_subsequence(lst)
        st.write(f"Length of longest increasing subsequence is: {ans}")

    # Longest_common_subsequence: -----------------------------------------------------
    elif operation == "longest_common_subsequence":
        def longest_common_subsequence(lst):
            num = len(lst)
            lcs_length = [1] * num
            for i in range(1, num):
                for j in range(0, i):
                    if lst[i] == lst[j] and lcs_length[i] < lcs_length[j] + 1:
                        lcs_length[i] = lcs_length[j] + 1
            maximum = 0
            for i in range(num):
                maximum = max(maximum, lcs_length[i])
            return maximum

        lst_element = st.text_input("Enter the elements of the list (separated by space):")
        lst = list(map(int, lst_element.split()))

        result = longest_common_subsequence(lst)
        st.write(f"Length of longest common subsequence is: {result}")

   

if __name__ == "__main__":
    main()
