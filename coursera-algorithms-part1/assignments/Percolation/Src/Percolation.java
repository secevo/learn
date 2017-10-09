import edu.princeton.cs.algs4.WeightedQuickUnionUF;
public class Percolation {
    private WeightedQuickUnionUF uf;
    private byte[] statuses; // bit0:0 closed/ 1 open; bit1 connect to top or not;bit2,connect to bottom or not 
    private int side;
    private boolean percolated = false;
    public Percolation(int n) { // create n-by-n grid, with all sites blocked
        if (n <= 0) {
            throw new java.lang.IllegalArgumentException("n<=0");
        }
        side = n;
        statuses = new byte[side * side];
        uf = new WeightedQuickUnionUF(side * side);
    }

    public void open(int row, int col) {       // open site (row, col) if it is not open already
        checkInput(row, col);
        if (isOpen(row, col)) return;
        int index = getIndex(row, col);
        int neighbourStatus = 0;
        
        if (col < side && isOpen(row, col + 1)) {
            int rightIndex = getIndex(row, col + 1);
            neighbourStatus = (neighbourStatus | statuses[uf.find(rightIndex)]);
            uf.union(rightIndex, index);
        }
        if (col > 1 && isOpen(row, col - 1)) {
            int leftIndex = getIndex(row, col - 1);
            neighbourStatus = neighbourStatus | statuses[uf.find(leftIndex)];
            uf.union(leftIndex, index);
        }
        if (row < side && isOpen(row + 1, col)) {
            int bottomIndex = getIndex(row + 1, col);
            neighbourStatus = neighbourStatus | statuses[uf.find(bottomIndex)];
            uf.union(bottomIndex, index);
        }
        if (row > 1 && isOpen(row - 1, col)) {
            int topIndex = getIndex(row - 1, col);
            neighbourStatus = neighbourStatus | statuses[uf.find(topIndex)];
            uf.union(topIndex, index);
        }
        
        statuses[index] = 1; // bit0 opened
        if (row == 1) {
            statuses[index] = (byte) (statuses[index] + 2); // 011 opend connect to top
        }
        if (row == side) {
            statuses[index] = (byte) (statuses[index] + 4); // 101 opend connect to bottom
        }
        int root = uf.find(index);
        statuses[root] = (byte) (statuses[root] | statuses[index] | neighbourStatus);
        percolated = percolated || (statuses[root] & 7) == 7;
    }
    
    private void checkInput(int row, int col)
    {
        if (row < 1 || row > side || col < 1 || col > side) {
            throw new java.lang.IndexOutOfBoundsException();
        }
    }
    
    public boolean isOpen(int row, int col) {  // is site (row, col) open?
        checkInput(row, col);
        return (statuses[getIndex(row, col)] & 1) == 1;
    }
    public boolean isFull(int row, int col) {  // is site (row, col) full?
        checkInput(row, col);
        return (statuses[uf.find(getIndex(row, col))] & 2) == 2; // connect to top
    }
    public boolean percolates() {              // does the system percolate?
        return percolated;
    }
    
    private int getIndex(int row, int col) {
        return (row - 1) * side + col - 1;
    }

    public static void main(String[] args) {   // test client (optional)
    }
}
