
public class Primes
{
	
	//private SundaramExclude ex_generator;

	// Primes()
	// {
	// 	ex_generator = new SundaramExclude();
	// }

	public static long ithprime(long n)
	{
		if (n<3) return n;

		SundaramExclude ex_generator = new SundaramExclude();
		long current = 1;
		long to_exclude = ex_generator.next();

		while (n>2)
		{
			current++;
			if (current<to_exclude)
			{
				n--;
			}
			else
			{
				to_exclude = ex_generator.next();
			}
		}
		return 2*current+1;
	}


	public static void main(String[] args) 
	{
		System.out.println(ithprime(30000));
	}

}