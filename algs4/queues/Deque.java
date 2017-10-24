import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdIn;


public class Deque<Item> implements Iterable<Item> {
    private int n;         // number of elements on queue
    private Node head;    // beginning of queue
    private Node tail;     // end of queue

    // helper linked list class
    private class Node {
        private Item item;
        private Node next;
        private Node prev;
    }

    public Deque() {
        head = null;
        tail  = null;
        n = 0;

    }

    public boolean isEmpty() {
        return head == null;
    }

    
    public int size() {
        return n;     
    }

    public void addFirst(Item item) {
        if (item == null) {throw new IllegalArgumentException();}
        Node newHead = new Node();
        newHead.item = item;

        if (head != null) {
            newHead.next = head;
            head.prev = newHead;
        }
        head = newHead;
        if (tail == null) tail = head;

        n++;
    }
    
    public void addLast(Item item) {
        if (item == null) {throw new IllegalArgumentException();}
        Node newTail = new Node();
        newTail.item = item;

        if (tail != null) {
            newTail.prev = tail;
            tail.next = newTail;
        }
        tail = newTail;
        if (head == null) head = tail;
        n++;
    }

    public Item removeFirst() {
        if (isEmpty()) throw new NoSuchElementException ("Queue underflow");
        Node oldHead = head;
        head = head.next;

        if (head == null)
            tail = null;
        else
            head.prev = null;
        n--;

        return oldHead.item;
    }
    
    public Item removeLast() {
        if (isEmpty()) throw new NoSuchElementException ("Queue underflow");
        Node oldTail = tail;
        tail = oldTail.prev;
        if (tail == null)
            head = null;
        else
            tail.next = null;
        n--;

        return oldTail.item;
    }


    public String toString() {
        StringBuilder s = new StringBuilder();
        for (Item item : this)
            s.append(item + " ");
        return s.toString();
    } 


    public Iterator<Item> iterator()  {
        return new ListIterator();  
    }

    private class ListIterator implements Iterator<Item> {
        private Node current = head;

        public boolean hasNext()  { return current != null;                     }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next;
            return item;
        }
    }

    public static void main(String[] args) {
        Deque<String> deck = new Deque<String>();

    }
}