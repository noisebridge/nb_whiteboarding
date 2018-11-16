/**
 * https://www.hackerrank.com/challenges/torque-and-development/problem
 *
 * Note: getting this to pass HR was a task. Their provided boilerplate 
 * and function header is incorrect, so ints need to be changed to long 
 * to satisfy hidden tests.
 */

import java.util.*;


class RoadsAndLibraries {
    static long roadsAndLibraries(int n, int c_lib, int c_road, int[][] cities) {
        if (c_lib <= c_road) { return n * c_lib; }
        
        long total = 0;
        HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
        HashSet<Integer> visited = new HashSet<>();
        
        for (int[] edge : cities) {
            for (int node : edge) {
                if (!graph.containsKey(node)) {
                    graph.put(node, new ArrayList<Integer>());
                }
            }
            
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        
        for (int i : graph.keySet()) {
            if (!visited.contains(i)) {
                Stack<Integer> stack = new Stack<>();
                stack.push(i);
                visited.add(i);
                total += c_lib;
                
                while (!stack.empty()) {
                    for (int neighbor : graph.get(stack.pop())) {
                        if (!visited.contains(neighbor)) {
                            visited.add(neighbor);
                            stack.push(neighbor);
                            total += c_road;
                        }
                    }
                }
            }
        }
        
        return total + (n - visited.size()) * c_lib;
    }

    public static void main(String[] args) {
        System.out.println(roadsAndLibraries(3, 2, 1, new int[][] {{1, 2}, {3, 1}, {2, 3}}));
    }
}
