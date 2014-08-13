/* IMPORTANT: class must not be public. */


import java.io.BufferedReader;
import java.io.InputStreamReader;

class TestClass {
    public static void main(String args[] ) throws Exception {
        List<Integer> primes = sieve(Math.pow(10, 6))

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
        for (int i = 0; i < N; i++) {
            System.out.println("hello world");
        }

        System.out.println("Hello World!");
    }

    public List<Integer> sieve(Integer n) {
 
        List<Integer> primes = new ArrayList<Integer>(n);
 
        boolean[] isComposite = new boolean[n + 1];
 
        for(int i = 2; i <= n; i++) {
 
            if(!isComposite[i]) {
 
                primes.add(i);
 
                for(int j = i * i; j >= 0 && j <= n; j += i) {
                    isComposite[j] = true;
                }
            }
        }
 
        return primes;
    }
 
}
