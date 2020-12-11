package Arrays.SearchingAlgorithm;

import SingleDImensionalArrays.StdOut;

public class LinearSearch {
    public static int linearSearch(int[] list, int key) {
        for (int i = 0; i < list.length; i++) {
            if (key == list[i])
                return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] list = {7, 3, 5, 9, 0, 4};

        StdOut.println(linearSearch(list, 3));
    }
}
