fn main(){

    let n = 1000;

    for a in 1..n {
        let c = (a*a + 500000 - 1000*a) / (1000 - a);
        let b = (1000 - a - c);

        if (b > a && c > b && (a * a + b * b) == c * c) {
            println!("{}",a*b*c);
        }
    }
}
// TRYING TO UNDERSTAND:
// a cannot be 1000, this follows because a+b+c=1000 -> b=0=c which directly contradicts that a<b<c. Same reasoning goes to a being 999.
// lets try to use algebra: 1) a<b<c, 2) a+b+c=1000, 3) a*a+b*b=c*c. Clearing b from 2) we get 4) b=1000-a-c. Clearing c in 3) we get: 5) c=sqrt(a*a+b*b)
// substituting 4) in 5) we get: c=sqrt(a*a+(1000-a-c)(1000-a-c)), developing a little bit further we get 6) c=sqrt(a*a+(1000000-1000a-1000c-1000a+a*a+a*c-1000c+a*c+c*c))
// which in turn reduces to: c*c=a*a+(1000000-2000a-2000c+2a*c+a*a+c*c), using big step notation ->* leads us where we wanted :p. jk, this in turn reduces to:
// c*c=a*a+1000000-2000a-2000c+2*a*c+a*a+c*c
// => 2*c*c=2*a*a+1000000-2000a-2000c+2*a*c
// => c*c=a*a+500000-1000a-1000c+a*c
// => c*c=(a*a+500000-1000a+(a-1000)c)
// => c*c-(a-1000)c=a*a+500000-1000a
// => c*(c-(a-1000))=a*a+500000-1000a
// => c=(a*a+500000-1000a)/(c-(1000-a))
// => c=(a*a+500000-1000a)/(1000-a-b-1000-a)
// => c=(a*a+500000-1000a)/(-a-b-a)
