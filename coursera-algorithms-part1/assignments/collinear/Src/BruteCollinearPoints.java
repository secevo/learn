import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;

public class BruteCollinearPoints {
    private List<LineSegment> segments;
    public BruteCollinearPoints(Point[] points) {
        // finds all line segments containing 4 points
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
       
        Arrays.sort(thePoints);
        for (int i = 0; i < thePoints.length; i++) {
            for (int j = i+1; j < thePoints.length; j++) {
                for (int k = j+1; k < thePoints.length; k++) {
                    for (int l = k+1; l < thePoints.length; l++) {
                        if (thePoints[i].slopeOrder().compare(thePoints[j], thePoints[k]) == 0 && 
                                thePoints[i].slopeOrder().compare(thePoints[j], thePoints[l]) == 0) {
                            segments.add(new LineSegment(thePoints[i], thePoints[l]));
                        }
                    }
                }
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
        BruteCollinearPoints collinear = new BruteCollinearPoints(points);
        for (LineSegment segment : collinear.segments()) {
            StdOut.println(segment);
            segment.draw();
        }
        StdDraw.show();
    }
}
