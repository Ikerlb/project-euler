use std::collections::HashSet;
//The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
//1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

//intuition: the number of factors is equal to the multiplication of the succesor of the exponents

fn main(){
	//10000000000000000000 => 398
	// too lazy to write a function to get prime factors, so this is what we will do:
	// since we know the numbers  
	//println!("{}", get_factors(10000000000000000000).len());
	for facts in nth_triangle_number_factors(7){
		println!("{}",facts)
	}

}

fn nth_triangle_number(n:usize)-> usize{
	n*(n+1)>>1
}

fn nth_triangle_number_factors(n:usize)->std::collections::hash_set::Union<usize, std::collections::hash_map::RandomState>{
	let mut even=0;
	let mut odd=0;
	let factors: HashSet<usize> = [1, nth_triangle_number(n)].iter().cloned().collect();	
	
	if n%2==0 {
		even=(n/2) as usize;
		odd=n+1;
	}
	else{
		even=((n+1)/2) as usize;
		odd=n;
	}
	//factors.union(&get_factors(even)).collect().union(&get_factors(odd)).collect()
	factors.union(&get_factors(odd))

	//factors.union(&get_factors(even)).union(&get_factors(odd))
	
}

fn get_factors(n:usize)->HashSet<usize>{	
	let mut fs = HashSet::new();
	for i in 2..((n as f64).sqrt() as usize)+1{
		if n%i==0 {
			fs.insert(i);
			fs.insert((n/i) as usize);
		}
	}
	fs
}


