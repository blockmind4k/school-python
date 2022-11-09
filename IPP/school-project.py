#Sorting program for school

#   function for menu banner
def text_banner():
    logo = """
    ________________________________________________________________________________________

         ██████╗███████╗    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
        ██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
        ██║     ███████╗    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
        ██║     ╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
        ╚██████╗███████║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
         ╚═════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   
                            By: Aparajith, Sai Ganesha, Thijil                                                                    
    ________________________________________________________________________________________                                                                                    
                                                                                        """
    print(logo)


#   function for merge sort
def merge_sort(num_array):
    mid = len(num_array)//2

    if len(num_array) > 1:
        left_num_array = num_array[:mid]
        right_num_array = num_array[mid:]

        # recursively calling the function as long as num_array > 1 
        merge_sort(left_num_array)
        merge_sort(right_num_array)

        i = 0 # left most index of left_num_list array
        j = 0 # left most index of right_num_list array
        k = 0 # index in merged array

        # while left index is > len(left array) and right idx < len(right array) do this
        while i < len(left_num_array) and j < len(right_num_array):
            # comparing left most indices of the split arrays...
            if left_num_array[i] < right_num_array[j]:
                num_array[k] = left_num_array[i] # adding left most index from the left array to merged list
                i = i + 1
                k = k + 1
            
            else:
                num_array[k] = right_num_array[j] # adding right most index from the right array to merged list
                j = j + 1
                k = k + 1
        
        while i < len(left_num_array): # if and when left most index has not reached end of left array 
            num_array[k] = left_num_array[i]
            k = k + 1
            i = i + 1

        while j < len(right_num_array): # if and when right most index has not reached end of right array
            num_array[k] = right_num_array[j]
            k = k + 1
            j = j + 1


#   taking input from a file and converting it into a list
def file_input():
    data = open('input.txt', 'r')
    inputData = data.read() # reads input.txt

    dataList = inputData.split('\n') # splits data from input.txt and converts it to a list

    for i in range(0, len(dataList), 1):
        dataList[i] = float(dataList[i]) # projecting string into a float

    #print(dataList)

    merge_sort(dataList) # sorts the list into (ascending order)

    outputData = open("output.txt", "w") # opens the output file

    for i in range(0, len(dataList), 1): # iterates for every element in list
        outputData.write(str(dataList[i])) # writes each element from the list onto the output file
        outputData.write('\n')

#   enter the input manually for number list sorting 
def func_numlist(): #numbers ascending sort
    var_num_ls = []
    var_n = int(input('Enter number of elements: '))
    for i in range (0, var_n):
        var_num_elmt = float(input('Enter a number: '))
        var_num_ls.append(var_num_elmt)

    print('The list is: ', var_num_ls, '\n')
    # merge_sort(var_num_ls)
    merge_sort(var_num_ls)

    print('The sorted list in ascending order is: \n\n', var_num_ls)

#   reversing a sorted list
def func_descending():
    var_num_ls = [] # declaring empty list
    var_n = int(input('Enter number of elements: ')) # taking number of elements
    for i in range (0, var_n): # declaring for loop
        var_num_elmt = float(input('Enter a number: ')) # number input
        var_num_ls.append(var_num_elmt) # appending input number to a list

    merge_sort(var_num_ls) # sorting the list in ascending order...

    arr_len = len(var_num_ls)

    t = -1
    rev_array = []
    neg_len = arr_len-(arr_len*(2))

    while(t >= neg_len):
        rev_array.append(var_num_ls[t])
        t -= 1

    print('\nOriginal List: ', var_num_ls, '\n')
    print('\nList sorted in Descending order: ', rev_array)


#   sorting an list consisting of strings
def func_alphalist(): #array of strings sort
    var_alph_ls = []
    var_n_strings = int(input('Enter number of elements: '))
    for i in range (0, var_n_strings):
        var_alph_elmt = input('Enter a string: ')
        var_alph_ls.append(var_alph_elmt) # appends element to list
    
    print('The array of strings is: ', var_alph_ls, '\n')
    var_alph_ls.sort() # sorts alphabet list
    print ('The Alphabetically sorted list is: ', var_alph_ls)

var_usr_0 = 0

# running an infinite loop unitl user decides to break 
while True:
    if var_usr_0 == 0:
        text_banner() # calling the text_banner so that logo is printed
        print('\n----------MENU----------\n')

        print('1. Sort a list')
        print('2. Sort a List of Names according to Alphabetic order')
        print('3. Exit')

        var_usr_1 = int(input('Choose a number from the menu to proceed: '))
        
        if (var_usr_1 == 1):
            # numeric sorting
            print('Do you want to sort input from a text file? If so, enter "file" \n')
            print('\n If you want to input data manually, enter "manual"\n')
            choice = input('Enter input: ')
            choice.lower
            if(choice == "file"):
                print('\n___________________________________________________________\n')
                print('Note: Please save input.txt before running this program')
                print('\n___________________________________________________________\n')

                file_input() # calling file_input to read input from a file

                print("Output is stored in output.txt\n")
                print('Enter "menu" to go back to menu')
                menu = input('Input here: ')
                menu.lower()
                if(menu == "menu"):
                    var_usr_0 = 0 # redirects to menu

            if(choice == "manual" or var_usr_0 == 2): # manual
                print('A. Sort in Ascending order')
                print('D. Sort in Descending order')
                print('Enter "menu" to go back to menu')
                var_usr_2 = input('Enter a number to proceed: ')

                if (var_usr_2 == "A" or var_usr_2 == "a"):
                    func_numlist()

                if (var_usr_2 == "D" or var_usr_2 == "d"):
                    func_descending()

                elif(var_usr_2 == "menu"):
                    var_usr_0 = 0 # redirects to menu

                else:
                    print('Enter a valid input')
                    var_usr_0 = 2 # redirects to manual
            
            else:
                var_usr_1 = 1 # redirects to start of numeric sorting

        # sorting alphabet list
        if (var_usr_1 == 2):
            func_alphalist()
        
        elif (var_usr_1 == 3):
            print('Thank you for using the program\n')
            print('This program was made by: Aparajith, Sai Ganesha, Thijil')
            break

        else:
            print('\nInput a proper value...\n')
            var_usr_0 = 0 # returns to menu
