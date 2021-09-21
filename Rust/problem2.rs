fn main(){
	let n=100;
	let sum_till_n=(n*(n+1))/2;
	let square_of_sum=sum_till_n*sum_till_n;
	let sum_of_squares=(n*(n+1)*((2*n)+1))/6;
	let diff=sum_of_squares-square_of_sum;
	println!("{}",diff.abs());
}