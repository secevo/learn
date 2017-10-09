import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    private Item[] a;         // array of items
    private int n;            // number of elements on stack
public RandomizedQueue() {
       // construct an empty randomized queue
       a = (Item[]) new Object[2];
       n = 0;
   }
   public boolean isEmpty() {
       return n == 0;
       // is the queue empty?
   }
   public int size() {
    return n;
       // return the number of items on the queue
   }
   
   private void resize(int capacity) {
       assert capacity >= n;

       // textbook implementation
    Item[] temp = (Item[]) new Object[capacity];
       for (int i = 0; i < n; i++) {
           temp[i] = a[i];
       }
       a = temp;

      // alternative implementation
      // a = java.util.Arrays.copyOf(a, capacity);
   }


   
   public void enqueue(Item item) {
       // add the item
       if (item == null) {
           throw new NullPointerException();
       }
       if (n == a.length) resize(2*a.length);    // double size of array if necessary
       a[n++] = item;      
   }
   public Item dequeue() {
       if (isEmpty()) throw new NoSuchElementException("Stack underflow");
       int randomIndex = StdRandom.uniform(n);
       Item item = a[randomIndex];
       a[randomIndex] = a[n-1];
       a[n-1] = null;                              // to avoid loitering
       n--;
       // shrink size of array if necessary
       if (n > 0 && n == a.length/4) resize(a.length/2);
       return item;
   }
   public Item sample() {
       if (isEmpty()) throw new NoSuchElementException("Stack underflow");
       int randomIndex = StdRandom.uniform(n);
       Item item = a[randomIndex];
       return item;
       // return (but do not remove) a random item
   }
   public Iterator<Item> iterator() {
    return new RandomArrayIterator();
       // return an independent iterator over items in random order
   }
   
   private class RandomArrayIterator implements Iterator<Item> {
       private int i;
       private int[] indexs;
       public RandomArrayIterator() {
           i = n;
           indexs = new int[i];
           for (int j = 0; j < i; j++) {
               indexs[j] = j;
           }
       }

       public boolean hasNext() {
           return i >= 1;
       }

       public void remove() {
           throw new UnsupportedOperationException();
       }

       public Item next() {
           if (!hasNext()) throw new NoSuchElementException();
           int randomIndex = StdRandom.uniform(i);
           int index = indexs[randomIndex];
           indexs[randomIndex] = indexs[i-1];
           i--;
           return a[index];
       }
   }
   
   public static void main(String[] args) {
       // unit testing
   }
}