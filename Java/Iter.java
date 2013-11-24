public class Iter implements Comparable<Iter>
{
	private long current;
	private long step;
	
	public Iter(long i)
	{
		current = 2*(i+1)*(i+2);
		step = 2*(i+1)+1;
	}

	public long peek()
	{
		return current;
	}

	public long next()
	{
		current += step;
		return current;
	}

	@Override
    public int compareTo(Iter other)
    {
    	if (current<other.current)
    		return -1;
    	if (current>other.current) 
    		return 1;
    	return 0;
    }

    public static void main(String[] args) {
    	Iter ff = new Iter(0);
    	for (int i=0; i<30; i++) 
    	{
    		System.out.println(ff.next());
    	}
    }

}