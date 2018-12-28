import java.util.Scanner;

/*
  Problem: Given n bits, return all possible combinations of k 1's.
  Example for n = 8 and k = 3:
  [1 1 1 0 0 0 0 0] - would be one combination
  [1 1 0 1 0 0 0 0] - would be one combination
  [0 0 1 1 1 0 0 0] - would be one combination

  [1 1 0 1 0 0 1 0] - would NOT be one combination

  This solution relies heavily in the one for combinations found in this website:
  https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
*/
class KBitsCombination {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("This is the solution for k bits combinator in n bits array");
    System.out.println("Please specify the number of total bits n:");
    Integer n = scanner.nextInt();
    System.out.println("Please specify the number of bits to combine k:");
    Integer k = scanner.nextInt();

    KBitsCombination kBitsCombination = new KBitsCombination();

    kBitsCombination.findAllCombinations(n, k);
  }

  /**
   * Method that prints all combinations of possible 1's inside an n-length array
   *
   * @param n length of the array
   * @param k number of 1 bits to combine
   */
  private void findAllCombinations(int n, int k) {
    int[] array = new int[n];
    // The array is created with the indices we want to combine
    // if n is 8, an array of [0 1 2 3 4 5 6 7] is created.
    for(int i=0; i<n; i++) {
      array[i] = i;
    }
    
    findAllCombinations(array, new int[k], k, 0, 0);
  }
  
  /**
   * Recursive method that finds all possible combinations of indices
   * where to put the k 1 bits inside the array. And then prints the array.
   *
   * Example for n=8 and k=3:
   * combination -> resulting array
   * {0 1 2}     -> [1 1 1 0 0 0 0 0]
   * {0 1 3}     -> [1 1 0 1 0 0 0 0]
   * ...
   * {5 6 7}     -> [0 0 0 0 0 1 1 1]
   *
   * @param array of indices to combine.
   * @param combination the current combination of indices.
   * @param k the number of 1's to insert in the array.
   * @param combinationIndex the current index of the current combination in the recursive stack.
   * @param arrayIndex the current index of the array in the recursive stack.
   */
  private void findAllCombinations(int[] array, int[] combination, int k, int combinationIndex, int arrayIndex) {
    if(combinationIndex == k) {
      int[] solution = new int[array.length];
      for(int i : combination) {
        solution[i] = 1;
      }
      
      for(int i : solution) {
        System.out.print(i+" ");
      }
      System.out.println("\n");
      return;
    }
    
    if(arrayIndex >= array.length) {
      return;
    }
    
    combination[combinationIndex] = array[arrayIndex];
    
    findAllCombinations(array, combination, k, combinationIndex+1, arrayIndex+1);
    findAllCombinations(array, combination, k, combinationIndex, arrayIndex+1);
  }
}