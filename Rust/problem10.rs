fn main() {
	let n = 2000000;
	let mut sum:usize=0;
	let sieve = create_sieve(n);
	for i in 2..n {
		if sieve[i]==true{
			sum+=i;
		}
	}
	println!("{:?}",sum);
}

//creates sieve of numbers less than n (from 1..n-1)
fn create_sieve(n:usize) -> Vec<bool>{
	let mut bv = vec![true; n];
	for i in 2..((n as f64).sqrt() as usize)+1 {
		if bv[i]==true {
			let mut j=2*i;
			while j < n {
				bv[j]=false;
				j+=i;
			}
		}
	}
	bv
}

/*
		let i = 1
		let step = 1

		while i < 10 {
		    println!("{}", i);
		    i += step;
		    step *= 2;
		}
*/