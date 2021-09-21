fn main(){
	let max=10001;
	let mut primes=1;
	let mut n=3;
	let mut is_prime=true;
	/*The very last increase of primes will be max*/
	while primes<max {
		/*Guess you wanted to use rust huh? Yo iterate each number from 2 to sqrt of n
		, if any of those numbers is a multiple of n, it's not a prime*/
		for x in 2..((n as f64).sqrt() as isize)+1{
		    if n%x==0 {
		    	is_prime=false;
		    	break;
		    }
		}
		/*If it managed to iterate all the way without the is_prime flag being false, print it
		and increase number of prime */
		if is_prime{
		    primes+=1;
		    println!("Prime #{}={}",primes,n);
		}
		n+=1;
		is_prime=true;
	}
}