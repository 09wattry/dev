import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;

//import edu.princeton.cs.algs4.Stopwatch;

public class PercolationStats {
    
    private double []trialResults;
    private double mean;
    private double stddev;
    private double confidenceLo;
    private double confidenceHi;
      
    //perform trials independent experiments on an n-by-n grid 
    public PercolationStats(int n, int trials) {
        if (n <= 0 || trials <= 0) {
            throw new IllegalArgumentException("row or col out of bounds");
        }
        
        trialResults = new double[trials];
        
        for (int i = 0; i < trials; i++) {
            Percolation trial = new Percolation(n);
            while (!trial.percolates()) {
                trial.open(StdRandom.uniform(1, n + 1), StdRandom.uniform(1, n + 1));
            }
            trialResults[i] = (double) trial.numberOfOpenSites() / (n * n);
        } //for(i)
        
        mean = StdStats.mean(trialResults);
        stddev = StdStats.stddev(trialResults);
        confidenceLo = mean - stddev * 1.96 / Math.sqrt(trials);
        confidenceHi = mean + stddev * 1.96 / Math.sqrt(trials);
        
    } //end constructor
    
    // sample mean of percolation threshold
    public double mean() {
        return mean;
    } //end mean()
    
    //sample standard deviation of percolation threshold    
    public double stddev() {
        if(trialResults.length <=1){
             stddev = Double.NaN;
        }else{
            return stddev;
        }
        return stddev;
    } //end stddev()
    
    // low  endpoint of 95% confidence interval
    public double confidenceLo() {
        return confidenceLo;
    } //end confidenceLo()
    
    // high endpoint of 95% confidence interval
    public double confidenceHi() {
        return confidenceHi;
    } // end confidenceHi()
    
    // test client (described below)
    public static void main(String[] args) {
        PercolationStats testStats = new PercolationStats(Integer.parseInt(args[0]), Integer.parseInt(args[0]));     
        System.out.println("mean = " + testStats.mean());
        System.out.println("stddev = " + testStats.stddev());
        System.out.println("95% confidence interval = [" + testStats.confidenceLo() + "," + testStats.confidenceHi() + "]");
        
    } //end main() 
}