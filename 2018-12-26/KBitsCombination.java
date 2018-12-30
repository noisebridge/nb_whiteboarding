import java.util.ArrayList;
import java.util.Arrays;

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
    ArrayList<int[]> combinations;

    System.out.println(" ================================= ");
    System.out.println(" Case for n = 8 and k = 3 ");
    combinations = KBitsCombination.findAllCombinations(8, 3);
    
    for (int[] c : combinations) {
      System.out.println(java.util.Arrays.toString(c));
    }

    System.out.println(" ================================= ");
    System.out.println("  Case for n = 4 and k = 2 ");
    combinations = KBitsCombination.findAllCombinations(4, 2);

    for (int[] c : combinations) {
      System.out.println(java.util.Arrays.toString(c));
    }
  }

  /**
   * Method that returns all combinations of possible 1's inside an n-length array
   *
   * @param n length of the array
   * @param k number of 1 bits to combine
   * @return list with all possible combinations
   */
  private static ArrayList<int[]> findAllCombinations(int n, int k) {
    int[] array = new int[n];
    // The array is created with the indices we want to combine
    // if n is 8, an array of [0 1 2 3 4 5 6 7] is created.
    for (int i = 0; i < n; i++) {
      array[i] = i;
    }
    
    ArrayList<int[]> combinations = new ArrayList<>();
    KBitsCombination.findAllCombinations(array, new int[k], combinations, k, 0, 0);

    return combinations;
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
  private static void findAllCombinations(int[] array, int[] combination, ArrayList<int[]> combinations, int k, int combinationIndex, int arrayIndex) {
    if (combinationIndex == k) {
      // A possible solution has been found, there is no need to continue down this path.
      int[] solution = new int[array.length];
      for (int i : combination) {
        solution[i] = 1;
      }
      combinations.add(solution);
    } else if (arrayIndex < array.length) {
      // A solution is still being composed, therefore further recursive calls are made
      // to continue creating possible solutions.
      combination[combinationIndex] = array[arrayIndex];
    
      KBitsCombination.findAllCombinations(array, combination, combinations, k, combinationIndex+1, arrayIndex+1);
      KBitsCombination.findAllCombinations(array, combination, combinations, k, combinationIndex, arrayIndex+1);
    }
  }
}