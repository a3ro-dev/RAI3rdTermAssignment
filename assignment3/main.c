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

// Main function
int main(){
    // Call the function to calculate and print the class average grade
    classAvgCalc();
    return 0;
}