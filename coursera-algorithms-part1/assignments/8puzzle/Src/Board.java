import java.util.ArrayList;
public class Board {
    private int n;
    private int blank;
    private int[][] theBlocks;
    
    public Board(int[][] blocks) {
        // construct a board from an n-by-n array of blocks
        // (where blocks[i][j] = block in row i, column j)
        if (blocks.length < 2 || blocks.length != blocks[0].length) {
            throw new java.lang.IllegalArgumentException();
        }
        n = blocks.length;
        theBlocks = clone(blocks);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j  < n; j++) {
                if (theBlocks[i][j] == 0) {
                    blank = i*n + j;
                }
            }
        }
    }
    
    private int[][] clone(int[][] source)
    {
        int[][] target = new int[source.length][source[0].length];
        for (int i = 0; i < source.length; i++) {
            for (int j = 0; j < source[0].length; j++) {
                target[i][j] = source[i][j];
            }
        }
        return target;
    }
    
    public int dimension() {
        return n;
    }
    public int hamming() {
        int sum = 0;
        for (int k = 0; k < n*n - 1; k++) {
            int i = k / n;
            int j = k % n;
            if (theBlocks[i][j] != k+1) {
                sum++;
            }
        }
        return sum;
    }
    public int manhattan() {
    // sum of Manhattan distances between blocks and goal
        int sum = 0;
        for (int k = 0; k < n*n; k++) {
            int i0 = k / n;
            int j0 = k % n;
            int block = theBlocks[i0][j0];
            if (block == 0) continue;
            int in = (block - 1) / n;
            int jn = (block - 1) % n;
            sum += (Math.abs(i0-in) + Math.abs(j0-jn));        
        }
        return sum;
    }
    public boolean isGoal() {
        for (int k = 0; k < n*n - 1; k++) {
            int i = k / n;
            int j = k % n;
            if (theBlocks[i][j] != k+1) {
                return false;
            }
        }
        return true;    
    }
    public Board twin() {
        // a board that is obtained by exchanging any pair of blocks
        int[][] twin = clone(theBlocks);
        if (blank == 0) {
            int temp = twin[n -1][n - 1];
            twin[n -1][n - 1] = twin[n -1][n - 2];
            twin[n -1][n - 2] = temp;
        }
        else if (blank == 1) {
            int temp = twin[0][0];
            twin[0][0] = twin[1][0];
            twin[1][0] = temp;
        }
        else {
            int temp = twin[0][0];
            twin[0][0] = twin[0][1];
            twin[0][1] = temp;
        }
        return new Board(twin); 
    }
    public boolean equals(Object y) {        // does this board equal y?
        if (this == y) return true;
        if (y == null) return false;
        if (this.getClass() != y.getClass()) return false;
        Board other = (Board) y;
        if (this.dimension() != other.dimension()) return false;
        int sz = this.dimension();
        for (int i = 0; i < sz; i++) {
            for (int j = 0; j < sz; j++) {
                if (this.theBlocks[i][j] != other.theBlocks[i][j])
                    return false;
            }
        }
        return true;
    }
    public Iterable<Board> neighbors() {
        // all neighboring boards
        ArrayList<Board> list = new ArrayList<Board>();
        int i = blank / n;
        int j = blank % n;
        if (i > 0) {
            int[][] up = clone(theBlocks);
            up[i][j] = up[i - 1][j];
            up[i - 1][j] = 0;
            list.add(new Board(up));
        }
        if (i < n-1) {
            int[][] bottom = clone(theBlocks);
            bottom[i][j] = bottom[i + 1][j];
            bottom[i + 1][j] = 0;
            list.add(new Board(bottom));
        }
        if (j > 0) {
            int[][] left = clone(theBlocks);
            left[i][j] = left[i][j - 1];
            left[i][j - 1] = 0;
            list.add(new Board(left));
        }
        if (j < n - 1) {
            int[][] right = clone(theBlocks);
            right[i][j] = right[i][j + 1];
            right[i][j + 1] = 0;
            list.add(new Board(right));
        }
        return list;
    }
    public String toString() {
        StringBuilder sb = new  StringBuilder();
        sb.append(n);
        sb.append("\n");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(String.format("%2d ", theBlocks[i][j]));
            }
            sb.append("\n");
        }
        return sb.toString();
        // string representation of this board (in the output format specified below)
    }
    
    public static void main(String[] args) {
        // unit tests (not graded)
    }

}
