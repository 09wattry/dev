import java.util.Iterator;
import java.util.NoSuchElementException;
import edu.princeton.cs.algs4.StdRandom;

public class RandomizedQueue<Item> implements Iterable<Item> {
    
    private int n; 
    private Item[] data;
    
    public RandomizedQueue() {
        data = (Item[]) new Object[1];
        n = 0;
    }// construct an empty randomized queue
    
    public boolean isEmpty() {
        return n == 0;
    }// is the queue empty?
    
    public int size() {
        return n;
    }// return the number of items on the queue
    
    private void resizeArray(int size) {
        if (size < 0) { throw new IllegalArgumentException();}
        Item[] copy = (Item[]) new Object[size];
        for (int i = 0; i < n; i++) {
            copy[i] = data[i];
        }
        data = copy;
    }
    
    public void enqueue(Item item){
        if (item == null) {
            throw new IllegalArgumentException();
        }
        
        data[n++] = item;
        
        if (n > 0 && data.length == n) {
            resizeArray(data.length * 2);
        }
    }// add the item
    
    public Item dequeue(){
        if (n == 0) {
            throw new java.util.NoSuchElementException();
        }
        if (n > 0 && data.length / 4 == n) {
            resizeArray(data.length / 2);
        }
        int randomIndex = StdRandom.uniform(0,n);
        
        Item item = data[randomIndex];
        swapOut(randomIndex,n - 1);
        
        n--;
        return item;
    }// remove and return a random item
    
   private void swapOut(int rth, int nth){
        data[rth] = data[nth];
        data[nth] = null;
    } 
    
    public Item sample() {
        if (n == 0) {
            throw new NoSuchElementException ();
        }
        return data[StdRandom.uniform(0, n)];
    }// return (but do not remove) a random item
    
    public Iterator<Item> iterator() {
        return new ListIterator();
    }// return an independent iterator over items in random order
    
    private class ListIterator implements Iterator<Item> {
        private int current;
        int[] index;
        
        public ListIterator(){
            index = new int[n];
            for (int i = 0; i < n; i++) { 
                index[i] = i;
            }
            StdRandom.shuffle(index);
            current = 0;
        }
        
        public boolean hasNext (){return current != index.length;}
        
        public void remove (){
            throw new UnsupportedOperationException();
        }
        
        public Item next (){
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            return  data[index[current++]];
        }
    }
}