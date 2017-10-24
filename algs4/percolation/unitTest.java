import junit.framework.TestCase;

/**
 * A JUnit test case class.
 * Every method starting with the word "test" will be called when running
 * the test with JUnit.
 */
public class unitTest extends TestCase {
    
    /**
     * A test method.
     * (Replace "X" with a name describing the test.  You may write as
     * many "testSomething" methods in this class as you wish, and each
     * one will be called when running JUnit over this class.)
     */
    public void testInput1() {
        Percolation test = new Percolation(1);
        if(test.percolates()){
            fail();
        }
    }
    
    public void testInput2() {
        Percolation test = new Percolation(2);
        if(test.percolates()){
            fail();
        }
    }
   
}
