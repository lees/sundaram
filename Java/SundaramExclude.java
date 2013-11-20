public class SundaramExclude
{

	private MinPQ<Iter> data;
	int last_returned;
	int min_border;
	int i;


	SundaramExclude()
	{
		data = new MinPQ<Iter>();
		data.push(new Iter(0));
		last_returned = 0;
		i = 0;
		min_border = data.peek().peek();
	}

	int next()
	{
		Iter iterator = data.pop();
		int to_return = iterator.peek();

		if (to_return==min_border)
		{
			i++;
			Iter new_iterator = new Iter(i);
			min_border = new_iterator.peek();
			data.push(new_iterator);
		}

		iterator.next();
		data.push(iterator);

		if (to_return == last_returned)
			return next();

		last_returned = to_return;
		return to_return;
	}

	public static void main(String[] args) {
		SundaramExclude ex_iter = new SundaramExclude();

		for (int i=0; i<300000-1; i++) 
		{
			ex_iter.next();
		}
		System.out.println(ex_iter.next());
	}


}
