import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private int n; // size
    private Node first;     
    private Node last;
    
    private class Node {
        private Item item;
        private Node next;
        private Node pre;
    }
    
    public Deque() {
        // construct an empty deque
        first = null;
        last = null;
        n = 0;
        assert check();
    }
   public boolean isEmpty() {
    return first == null;
       // is the deque empty?
   }
   public int size() {
    return n;
       // return the number of items on the deque
   }
   public void addFirst(Item item) {
       if (item == null) {
           throw new NullPointerException();
       }
       // add the item to the front
       Node oldfirst = first;
       first = new Node();
       first.item = item;
       first.next = oldfirst;
       first.pre = null;
       if (oldfirst != null) {
           oldfirst.pre = first;
       }
       else {
           last = first;
       }
       n++;
       assert check();
   }
   public void addLast(Item item) {
       // add the item to the end
       if (item == null) {
           throw new NullPointerException();
       }
       Node oldlast = last;
       last = new Node();
       last.item = item;
       last.next = null;
       last.pre = oldlast;
       if (oldlast != null) {
           oldlast.next = last;
       }
       else {
           first = last;
       }
       n++;
       assert check();
   }
   public Item removeFirst() {
           // remove and return the item from the front
       if (isEmpty()) throw new NoSuchElementException("Queue underflow");
       Item item = first.item;        // save item to return
       if (first == last) {
           last = null;
       }  
       first = first.next;            // delete first node
       if (first != null) {
           first.pre = null;
       }
       n--;
       assert check();
       return item;                   // return the saved item
   }
   public Item removeLast() {
       // remove and return the item from the end
       if (isEmpty()) throw new NoSuchElementException("Queue underflow");
       Item item = last.item;        // save item to return
       if (first == last) {
           first = null;
       }   
       last = last.pre;            // delete last node
       if (last != null) {
           last.next = null;
       }
       n--;
       assert check();
       return item;                   // return the saved item
   }
   public Iterator<Item> iterator() {
       return new ListIterator();
       // return an iterator over items in order from front to end
   }
   
   private class ListIterator implements Iterator<Item> {
       private Node current = first;
       public boolean hasNext()  { return current != null;                     }
       public void remove()      { throw new UnsupportedOperationException();  }

       public Item next() {
           if (!hasNext()) throw new NoSuchElementException();
           Item item = current.item;
           current = current.next; 
           return item;
       }
   }
   
// check internal invariants
   private boolean check() {

       // check a few properties of instance variable 'first'
       if (n < 0) {
           return false;
       }
       if (n == 0) {
           if (first != null) return false;
           if (last != null) return false;
       }
       else if (n == 1) {
           if (first == null)      return false;
           if (first.next != null) return false;
           if (last == null)    return false;
           if (last.pre != null) return false;
       }
       else {
           if (first == null)      return false;
           if (first.next == null) return false;
           if (last == null)      return false;
           if (last.pre == null) return false;
       }

       // check internal consistency of instance variable n
       int numberOfNodes = 0;
       for (Node x = first; x != null && numberOfNodes <= n; x = x.next) {
           numberOfNodes++;
       }
       if (numberOfNodes != n) return false;

       return true;
   }
   
   public static void main(String[] args) {
       Deque<String> deque = new Deque<String>();
       deque.addLast("1");
       deque.addLast("2");
       deque.addFirst("3");
       deque.removeLast();
       deque.removeLast();
       deque.removeFirst();
       deque.addFirst("3");
       deque.removeFirst();
       deque.addLast("1");
       deque.addLast("2");
       deque.addFirst("3");
       for (String str : deque)
           System.out.println(str);
   }
}