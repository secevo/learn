import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
public class Subset {
   public static void main(String[] args) {
       int k = Integer.parseInt(args[0]);
       RandomizedQueue<String> queue = new RandomizedQueue<String>();
       int n = 0;
       while (!StdIn.isEmpty()) {
           n++;
           String item = StdIn.readString();
           if (n <= k) {
               queue.enqueue(item);
           }
           else {
               int randomIndex = StdRandom.uniform(n);
               if (randomIndex < k) {
                   queue.dequeue();
                   queue.enqueue(item);
               }
           }
           
       }
       for (String str : queue)
           StdOut.println(str);
   }
}