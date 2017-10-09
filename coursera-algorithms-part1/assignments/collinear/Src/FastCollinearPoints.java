import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class FastCollinearPoints {
    private List<LineSegment> segments;
    public FastCollinearPoints(Point[] points) {
        // finds all line segments containing 4 or more points
        if (points == null)
            throw new java.lang.NullPointerException();
        for (int i = 0; i < points.length; i++) {
            if (points[i] == null)
                throw new java.lang.NullPointerException();
            for (int j = i+1; j < points.length; j++) {
                if (points[i].compareTo(points[j]) == 0)
                    throw new java.lang.IllegalArgumentException();
            }
        }
        
        Point[] thePoints = Arrays.copyOf(points, points.length);
        segments = new ArrayList<LineSegment>();
        
        for (int i = 0; i < thePoints.length-3; i++) {
            Arrays.sort(thePoints, i, thePoints.length);
            int j = i+1;
            Arrays.sort(thePoints, j, thePoints.length, thePoints[i].slopeOrder());
            while (j < thePoints.length) {
                double slope = thePoints[i].slopeTo(thePoints[j]);
                int counter = 1;
                int k = j+1;
                while (k < thePoints.length) {
                    if (Double.compare(slope, thePoints[i].slopeTo(thePoints[k])) == 0) {
                        counter++;
                        k++;
                    }
                    else {
                        break;
                    }
                }
                if (counter >= 3) {
                    segments.add(new LineSegment(thePoints[i], thePoints[k-1]));
                }
                j = k;
            }
        }
    }
    
    public int numberOfSegments() {
        // the number of line segments
        return segments.size();
    }
    public LineSegment[] segments() {
        return segments.toArray(new LineSegment[segments.size()]);
    }
    
    public static void main(String[] args) {

        // read the n points from a file
        In in = new In(args[0]);
        int n = in.readInt();
        Point[] points = new Point[n];
        for (int i = 0; i < n; i++) {
            int x = in.readInt();
            int y = in.readInt();
            points[i] = new Point(x, y);
        }

        // draw the points
        StdDraw.enableDoubleBuffering();
        StdDraw.setXscale(0, 32768);
        StdDraw.setYscale(0, 32768);
        for (Point p : points) {
            p.draw();
        }
        StdDraw.show();

        // print and draw the line segments
        FastCollinearPoints collinear = new FastCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
    }
}

