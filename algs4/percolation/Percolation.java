import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdRandom;
 
public class Percolation {    
    
    private final WeightedQuickUnionUF wQUF;
    private final int gridSize;
    private final int nN;
    private int openSiteCount = 0;
    private boolean percolates;
    private int[] status; // 0 - blocked, 1 - Open, 2 - Connected top, 4 - Connected Bottom
    
    
    private final int blocked = 1 << 0; //1
    private final int open = 1 << 1; //2
    private final int top = 1 << 2; //4
    private final int bottom = 1 << 3; //8
    
   
    // create n-by-n grid, with all sites blocked
    public Percolation(int n) {
        if (n <= 0) {
            throw new IllegalArgumentException("n out of bounds");
        }
        gridSize = n * n;
        nN = n;
        wQUF  = new WeightedQuickUnionUF(gridSize);
        status = new int[gridSize];

        for (int i = 0; i < gridSize; i++) {
            status[i] = blocked; 
        }
        for (int i = 0; i < nN; i++) {
            status[i] = status[i] | top;
        }
        
        for (int x = gridSize - nN; x < gridSize; x++) {
            status[x] = status[x] | bottom;
        }  
    } //end constructor
    
    // open site (row, col) if it is not open already
    public void open(int row, int col) {    
        if (row <= 0 || col <= 0 || row > nN || col > nN) {
            throw new IllegalArgumentException("Out of bounds");
        }
        if (!isOpen(row, col)) {
            int site = (row - 1) * nN + (col - 1);
            status[site] = (status[site] ^ blocked) | open;
            int iStatus = status[site];
            openSiteCount++;
            
            if (row - 1 > 0 && isOpen(row - 1, col)) {
                iStatus = iStatus | status[wQUF.find(site - nN)];
                wQUF.union(site, site - nN);
            } //up      
            if (row + 1 <= nN && isOpen(row + 1, col)) {
                iStatus = iStatus | status[wQUF.find(site + nN)];
                wQUF.union(site, site + nN);
            } //down
            if (col + 1 <= nN && isOpen(row, col + 1)) {

                iStatus = iStatus | status[wQUF.find(site + 1)];
                wQUF.union(site, site + 1);
            } //right
            if (col - 1 > 0 && isOpen(row, col - 1)) {
                iStatus = iStatus | status[wQUF.find(site - 1)];
                wQUF.union(site, site - 1); 
            } //left
            
            status[wQUF.find(site)] = status[wQUF.find(site)] | iStatus;
            if((status[wQUF.find(site)] & (top | bottom)) == (top + bottom)){
                percolates = true;
            }
        } //if(!Open)
    } //end open
    
    // is site (row, col) open?
    public boolean isOpen(int row, int col) {
        if (row <= 0 || col <= 0 || row > nN || col > nN) {
            throw new IllegalArgumentException("row or col out of bounds");
        }     
        boolean isOpen = false;
        int siteNumber = (row - 1) * nN + (col - 1);
        if ((status[siteNumber] & open) == open) {
            return true;
        }
        return isOpen;
    } //end isOpen
    
    // is site (row, col) full?
    public boolean isFull(int row, int col) {
        if (row <= 0 || col <= 0 || row > nN || col > nN) {
            throw new IllegalArgumentException("row or col out of bounds");
        }     
        boolean full = false; 
        int siteNumber = (row - 1) * nN + (col - 1);
        if (isOpen(row, col) && (status[wQUF.find(siteNumber)] & top) == top) {
            return true;
        }
        return full;
    } //end isFull
    
    // number of open sites
    public int numberOfOpenSites() {
        return openSiteCount;
    } //end numberOfOpenSites
    
    // does the system percolate?
    public boolean percolates() { 
        return percolates;
    } //end percolates()
      
} //end class