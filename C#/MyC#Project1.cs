namespace PracticeLearning
{
    class Program
    {
    static void Main(string[] args)
    {
        Console.Write("Hello, World!");
        Console.WriteLine("Welcome to My C# Project!");
        Console.WriteLine("This is a simple console application to demonstrate C# syntax.");

        //Example of a comment, this will not affect the code execution, and this is a single-line comment.
        /*
         *  This is a multi-line comment.
         *  It can span multiple lines and is useful for longer explanations.
         */

        console.WriteLine("\tComments are important for\n code readability."); // \t is a tab character, and \n is a newline character.
        Console.WriteLine("Let's explore some basic C# features.");
    
        Console.WriteLine("1. Variables and Data Types:");
        int age; // Declaration of an integer variable
        age = 16; // Initialization of the variable
        int number = 10; // Integer variable, declared and initialized in one line, and it is a whole number
        double pi = 3.14; // Double variable, representing a floating-point number
        string message = "I'm learning C#"; // String variable, representing text
        char symbol = '@'; // Character variable, representing a single character
        bool isLearning = true; // Boolean variable, representing a true/false value
        /*
         *  The above variables demonstrate different data types in C#:
         * - int for integers
         * - double for floating-point numbers
         * - string for text
         * - char for single characters
         * - bool for true/false values
         */

        Console.WriteLine($"Is it true that I am learning C#? Yes, It is '{isLearning}'"); // Using string interpolation to include variable values in the output
        Console.Write($"'{message}' and my age is  '{age}' .");
        Console.WriteLine($"The number is {number}, the symbol is '{symbol}'.");
        Console.WriteLine($"The value of pi is approximately {pi}.");
        /*
         *  The above lines demonstrate one way of outputting variable values using string interpolation.
         *  Example above interpolation with variables like {isLearning}, {message}, {age}, {number}, {symbol}, and {pi}.
         *  Type of Variables were integers, double, string, char, and boolean types in the string interpolations.
         *  String interpolation allows you to embed expressions inside string literals, making it easier to format output.
         *  The $ before the string indicates that it is an interpolated string.
         *  The curly braces {} are used to include variable values directly in the string.
         *  This makes the code cleaner and more readable compared to traditional string concatenation.
         *  String interpolation is a powerful feature in C# that enhances code readability and maintainability.
         *  It allows you to create formatted strings without the need for cumbersome concatenation.
         *  You can include any expression inside the curly braces, not just variable names.
         *  This makes it versatile for various scenarios, such as formatting numbers or dates.
         */

        Console.WriteLine("Is it true that I am learning C#? Yes, It is" + isLearning + ".");
        Console.WriteLine(message + "and my age is " + age + ".");
        Console.WriteLine("The number is " + number + ", the symbol is '" + symbol + "'.");
        Console.WriteLine("The value of pi is approximately " + pi + ".");
        // the above lines demonstrate another way of outputting variable values using string concatenation.
        // Example of string concatenation, where we combine strings using the + operator.
        // This method is less readable than string interpolation but still works, otherwise it is the same as the above example.

        Console.ReadKey(); // Wait for user input before closing the console window
        }
    }
}