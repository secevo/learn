import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.StdOut;

public class Solver {
    private BoardNode targetBoardNode; // record targetBoardNode
    
    private class BoardNode implements Comparable<BoardNode> {
        private Board item;
        private BoardNode prev;
        private int move;
        private boolean isTwin;
        
        // compare by priority
        public int compareTo(BoardNode that) {
            if (that == null) 
                throw new NullPointerException("Input argument is null");
            int thisPriority = this.move + this.item.manhattan();
            int thatPriority = that.move + that.item.manhattan();
            return thisPriority-thatPriority;
        }
    }
    public Solver(Board initial) {
        // find a solution to the initial board (using the A* algorithm)
        targetBoardNode = null;
        MinPQ<BoardNode> minpq = new MinPQ<BoardNode>();
        BoardNode bn = new BoardNode();
        bn.item = initial;
        bn.isTwin = false;
        bn.move = 0;
        bn.prev = null;
        minpq.insert(bn);
        BoardNode bntwin = new BoardNode();
        bntwin.item = initial.twin();
        bntwin.isTwin = true;
        bntwin.move = 0;
        bntwin.prev = null;
        minpq.insert(bntwin);
        while (!minpq.isEmpty()) {
            BoardNode current = minpq.delMin();
            if (current.item.isGoal()) {
                if (current.isTwin) {
                    targetBoardNode = null;
                    break;
                }
                else {
                    targetBoardNode = current;
                    break;
                }
                    
            }
            else {
                for (Board bd : current.item.neighbors()) {
                    if (current.prev != null && current.prev.item.equals(bd)) continue;
                    BoardNode neighborNode = new BoardNode();
                    neighborNode.item = bd;
                    neighborNode.isTwin = current.isTwin;
                    neighborNode.move = current.move + 1;
                    neighborNode.prev = current;
                    minpq.insert(neighborNode);
                }
            }
        }
    }
    

    public boolean isSolvable() {
        // is the initial board solvable?
        return targetBoardNode != null;
    }
    public int moves() {
        // min number of moves to solve initial board; -1 if unsolvable
        if (isSolvable()) {
            return targetBoardNode.move;    
        }
        return -1;
    }
    public Iterable<Board> solution() {
        // sequence of boards in a shortest solution; null if unsolvable
        Stack<Board> stack = new Stack<Board>();
        BoardNode tmpbn = targetBoardNode;
        while (tmpbn != null) {
            stack.push(tmpbn.item);
            tmpbn = tmpbn.prev;
        }
        if (stack.isEmpty()) 
            return null;
        else 
            return stack;
    }
    public static void main(String[] args) {
        // solve a slider puzzle (given below)
     // create initial board from file
        In in = new In(args[0]);
        int n = in.readInt();
        int[][] blocks = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                blocks[i][j] = in.readInt();
        Board initial = new Board(blocks);

        // solve the puzzle
        Solver solver = new Solver(initial);

        // print solution to standard output
        if (!solver.isSolvable())
            StdOut.println("No solution possible");
        else {
            StdOut.println("Minimum number of moves = " + solver.moves());
            for (Board board : solver.solution())
                StdOut.println(board);
        }
    }
}
