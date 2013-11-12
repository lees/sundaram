

merge xlist@(x:xs) ylist@(y:ys)
	| x<y = x : merge xs ylist
	| x>y = y : merge xlist ys
	| otherwise = x : merge xs ys


exclude xlist@(x:xs) ylist@(y:ys) 
	| x < y = x : exclude xs ylist
	| x > y = exclude xlist ys
	| otherwise = exclude xs ys


sundaram_row' i = 
	let start = 2*(i+1)*(i+2);
		step = 2*(i+1)+1
	in start : (merge (igen (start+step) step) $ sundaram_row' (i+1))
	where
		igen current step = current : igen (current+step) step

sundaram_row = sundaram_row' 0

primes = 2: [ 2*i+1 | i <- (exclude [1..] $ sundaram_row)]

--main = do putStrLn.show $ primes !! 100000
main = do putStrLn.show $ sundaram_row !! 400000