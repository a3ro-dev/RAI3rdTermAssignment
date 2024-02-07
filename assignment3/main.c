#include <stdio.h>

// Function to calculate and print the class average grade
int classAvgCalc() {
    // Variable to store the grade entered by the user
    int grade;
    // Counter for the number of grades entered
    int count = 0;
    // Variable to store the total of all grades entered
    float total = 0;
    // Variable to store the average grade
    float average;

    // Loop to continuously ask the user to enter grades
    do {
        printf("Enter grade, -1 to end: ");
        scanf("%d", &grade);

        // If the entered grade is not -1, add it to the total and increment the counter
        if (grade != -1) {
            total += grade;
            count++;
        }
    } while (grade != -1); // End the loop when the user enters -1

    // Calculate the average grade
    average = total / count;

    // Print the average grade
    printf("Class average is %.2f\n", average);

    // If the average grade is less than 40, print a "year back" message
    if (average < 40) {
        printf("Year back message\n");
    }

    return 0;
}

// Function to convert decimal to octal
void decimalToOctal(int decimal) {
    // Array to store the octal digits
    int octal[100];
    // Counter for the number of digits
    int i = 0;

    // Loop to convert the decimal number to octal
    while (decimal != 0) {
        // Store the remainder when the decimal number is divided by 8
        octal[i] = decimal % 8;
        // Divide the decimal number by 8
        decimal /= 8;
        // Increment the counter
        i++;
    }

    // Print the octal number
    printf("Octal: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", octal[j]);
    }
    printf("\n");
}

// Function to convert decimal to hexadecimal
void decimalToHexadecimal(int decimal) {
    // Array to store the hexadecimal digits
    char hexadecimal[100];
    // Counter for the number of digits
    int i = 0;

    // Loop to convert the decimal number to hexadecimal
    while (decimal != 0) {
        // Store the remainder when the decimal number is divided by 16
        int remainder = decimal % 16;
        // Convert the remainder to a hexadecimal digit
        if (remainder < 10) {
            hexadecimal[i] = remainder + '0';
        } else {
            hexadecimal[i] = remainder + 55;
        }
        // Divide the decimal number by 16
        decimal /= 16;
        // Increment the counter
        i++;
    }

    // Print the hexadecimal number
    printf("Hexadecimal: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%c", hexadecimal[j]);
    }
    printf("\n");
}

// Function to convert decimal to binary
void decimalToBinary(int decimal) {
    // Array to store the binary digits
    int binary[100];
    // Counter for the number of digits
    int i = 0;

    // Loop to convert the decimal number to binary
    while (decimal != 0) {
        // Store the remainder when the decimal number is divided by 2
        binary[i] = decimal % 2;
        // Divide the decimal number by 2
        decimal /= 2;
        // Increment the counter
        i++;
    }

    // Print the binary number
    printf("Binary: ");
    for (int j = i - 1; j >= 0; j--) {
        printf("%d", binary[j]);
    }
    printf("\n");
}

// Main function
int main(){
    // Variable to store the user's choice
    int choice;
    // Variable to store the decimal number entered by the user
    int decimal;

    // Print the menu
    printf("Menu:\n");
    printf("1. Calculate and print the class average grade\n");
    printf("2. Convert decimal to octal\n");
    printf("3. Convert decimal to hexadecimal\n");
    printf("4. Convert decimal to binary\n");
    printf("Enter your choice (1-4): ");
    scanf("%d", &choice);

    // Execute the user's choice
    switch (choice) {
        case 1:
            classAvgCalc();
            break;
        case 2:
            printf("Enter a decimal number: ");
            scanf("%d", &decimal);
            decimalToOctal(decimal);
            break;
        case 3:
            printf("Enter a decimal number: ");
            scanf("%d", &decimal);
            decimalToHexadecimal(decimal);
            break;
        case 4:
            printf("Enter a decimal number: ");
            scanf("%d", &decimal);
            decimalToBinary(decimal);
            break;
        default:
            printf("Invalid choice\n");
            break;
    }

    return 0;
}
