#include <stdio.h>

#include <string.h>
#include <ctype.h>
int main()
{
    // create an array of characters with '\0'
    char a_array[17] = {'M', 'y', ' ', 'n', 'a', 'm', 'e', ' ','i', 's', ':', ' ', 'R', 'o', 'y', '!', '\0'};
    //iterate throught the array. Do not print directly, should using the format printing with "%c" not "%s"
    //update : if no terminator sign, can not use %s, other wise we can just use %s
    int a_array_size = sizeof(a_array);    /*should be 17*/
    int a_array_length = strlen(a_array);  /*should be 16*/
    for (int i = 0; i <= 15; i++)
    {
        printf("%c", a_array[i]);
    }
    printf ("\nthe size of the array: %i", a_array_size);
    printf ("\nthe length of the array: %i", a_array_length);
    printf ("\n--------------------\n");
    //------------------------------
    
    
    
    
    
    
    
    //------------------------------
    
    //create an array of strings, not characters. You have to use 
    //the string literal(*) if the element is string. Notice number 4.(not 3+5+4+5 = 17)
    //Because b_array is an array of 4 pointers.
    //each pointer points to the first element of the string respectively
    char *b_array[4] = {"My", "name", "is:", "Roy!"};
    //this size should be 8. Beacuse my mac system is 64bits.
    // Therefore a pointer to char type is 8 bytes.
    int string_pointer_size = sizeof(char *);  /*char * = b_array[0,1,2]*/
    // This size should be 4 * 8 = 32
    int size_of_array = sizeof(b_array);
    for (int i = 0; i <= 3; i++)
    {
        printf("%s ", b_array[i]);
    }
    printf ("\nthe size of type pointer to char: %i", string_pointer_size);
    printf ("\nThe size of the array: %i", size_of_array);
    printf("The first letter in the string arrat is: %s\n",b_array[0]);
    printf("Change the first letter to N by moving the pointer: %c\n", *b_array[0]+1);
    printf ("\n--------------------\n");
    //------------------------------
    
    
    
    
    
    //----------------------------
    char c_array[] = "My name is: Roy!";
    printf("%s\n", c_array);
    printf("the length of c_array is: %lu\n", strlen(c_array));
    printf("the size of c_array is: %lu\n", sizeof(c_array));
    printf("can we print out the terminate sign: %c\n", c_array[16]);
    printf ("\n--------------------\n");
    //------------------------------
    
    
    
    
    //----------------------------
    char d_array[] = {'M','y',' ','n', 'a', 'm', 'e', ' ','i', 's', ':', ' ', 'R', 'o', 'y', '!', '\0'};
    printf("%s\n", d_array);
    printf("the length of d_array is: %lu\n", strlen(d_array));
    printf("the size of d_array is: %lu\n", sizeof(d_array));
    printf("can we print out the terminate sign: %c\n", c_array[16]);
    printf ("\n--------------------\n");
    //------------------------------
    
    
    //----------------------------
    string e_array = "My name is: Roy!";
    printf("%s\n", e_array);
    printf("the length of e_array is: %lu\n", strlen(e_array));
    printf("the size of e_array is: %lu\n", sizeof(e_array));
    printf("can we print out the terminate sign: %c\n", c_array[16]);
    printf("The second letter is: %c\n",a_array[1]);
    a_array[0] = 'E';
    printf("Can we modify the seconde letter: %s\n",a_array);
    printf ("\n--------------------\n");
    //------------------------------
    
   
    //----------------------------
    char *f_array = "My name is: Roy!";
    printf ("%s\n", f_array);
    printf("the length of f_array is: %lu\n", strlen(f_array));
    printf("the size of f_array is: %lu\n", sizeof(f_array));
    printf("can we print out the terminate sign: %c\n", c_array[16]);
    printf ("\n--------------------\n");
    //------------------------------
}
