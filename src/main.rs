use std::collections::HashSet;

fn a(n: usize, list_of_prime_gaps: &Vec::<usize>) -> usize {
    let mut saved: HashSet<Vec::<usize>> = HashSet::new();
    for i in 1..(list_of_prime_gaps.len()-n) {
		let sequence = list_of_prime_gaps[i..i+n].to_vec();
        if saved.contains(&sequence) {
            return i + n - 1
        }
        saved.insert(sequence);
    }
    0
}

fn main() {
	let primes: Vec<usize> = primal::Primes::all().take(10252043).collect();
	let mut list_of_prime_gaps = Vec::<usize>::new();
	for i in 1..primes.len() {
		list_of_prime_gaps.push(primes[i] - primes[i-1]);
	}
	for n in 1..15 {
		print!("{}, ", a(n, &list_of_prime_gaps));
	}
	println!("");
}
