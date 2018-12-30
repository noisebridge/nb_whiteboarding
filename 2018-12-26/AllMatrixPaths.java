/**
 * Print all paths from top left to bottom right of
 * an n by m matrix moving only right and down
 */

public class AllMatrixPaths {
    public static void main(String[] args) {
        printAllPaths(3, 3);
    }

    static void printAllPaths(int n, int m) {
        printAllPaths(0, 0, n, m, new int[n+m-1], 0);
    }

    static void printAllPaths(int y, int x, int n, int m, int[] path, int i) {
        if (x < m && y < n) {
            path[i] = y * n + x + 1;

            if (x + 1 >= m && y + 1 >= n) {
                System.out.println(java.util.Arrays.toString(path));
            }

            printAllPaths(y, x + 1, n, m, path, i + 1);
            printAllPaths(y + 1, x, n, m, path, i + 1);
        }
    }
}
