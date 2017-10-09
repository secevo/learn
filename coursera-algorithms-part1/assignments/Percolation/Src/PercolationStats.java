import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
public class PercolationStats {
    private int side;
    private double[] thresholds;
    public PercolationStats(int n, int trials) {    // perform trials independent experiments on an n-by-n grid
        if (n <= 0 || trials <= 0) {
            throw new java.lang.IllegalArgumentException();
        }
        side = n;
        thresholds = new double[trials];
        for (int i = 0; i < trials; i++) {
            thresholds[i] = tryOnce();
        }
    }
    
    public double mean()
    {                          // sample mean of percolation threshold
        return StdStats.mean(thresholds);
    }
    public double stddev() {                        // sample standard deviation of percolation threshold
        return StdStats.stddev(thresholds);
    }
    public double confidenceLo() {                  // low  endpoint of 95% confidence interval
        return StdStats.mean(thresholds) - 1.96 * StdStats.stddev(thresholds) / Math.sqrt(thresholds.length);
    }
    public double confidenceHi() {                  // high endpoint of 95% confidence interval
        return StdStats.mean(thresholds) + 1.96 * StdStats.stddev(thresholds) / Math.sqrt(thresholds.length);
    }
    
    private double tryOnce() {
        Percolation percolation = new Percolation(side);
        int counter = 0;
        int size = side * side;
        int[] choises = new int[size];
        for (int j = 0; j < size; j++) {
            choises[j] = j;
        }
        while (true) {
            int choisesIndex;
            if (counter == size) {
                choisesIndex = 0;
            }
            else {
                choisesIndex = StdRandom.uniform(size - counter);
            }
            
            int choise = choises[choisesIndex];
            if (counter < size) {
                choises[choisesIndex] = choises[size - counter -1];
            }
            int row = choise / side + 1;
            int col = choise % side + 1;
            percolation.open(row, col);
            counter++;
            if (percolation.percolates()) {
                break;
            }    
        }
        return  counter / ((double) (side * side));
    }

    public static void main(String[] args) {    // test client (described below)
        PercolationStats percolationStats = new PercolationStats(100, 10000);
        StdOut.println(percolationStats.mean());
    }
}
