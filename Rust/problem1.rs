fn main(){
	let n=1000;
	let mut sum=0;
	for x in 1..n {
	    match (x%3,x%5) {
	        (0,_) => sum+=x,
	        (_,0) => sum+=x,
	        (_,_) => sum=sum
	    }
	}
	println!("{}",sum);
}