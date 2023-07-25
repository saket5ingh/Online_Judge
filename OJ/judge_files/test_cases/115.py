import java.util.Scanner;

public class ArraySumCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        // Create an array to store the elements
        int[] array = new int[n];

        // Take input for each element from the user
        for (int i = 0; i < n; i++) {
            System.out.print("Element " + (i + 1) + ": ");
            array[i] = scanner.nextInt();
        }

        // Calculate the sum of all elements
        int sum = 0;
        for (int num : array) {
            sum += num;
        }

        // Display the result
        System.out.println(sum);

        scanner.close();
    }
}
