
// Класс-контейнер реализующий очередь с приоритетами

public class MinPQ<Key extends Comparable<Key>>
{

	private Key[] data;
	private int len = 0;

	MinPQ()
	{
		data = (Key[]) new Comparable[10000];
	}

	void push(Key key)
	{
		len++;
		data[len] = key;
		swim(len);
	}

	Key peek()
	{
		return (Key) data[1];
	}

	Key pop()
	{
		Key to_return = (Key) data[1];
		exchange(1,len);
		data[len]=null;
		len--;
		sink(1);
		return to_return;
	}

	boolean less(int i, int j)
	{
		return (data[i].compareTo(data[j]) < 0);
	}

	void exchange(int i, int j)
	{
		Key temp = data[i];
		data[i] = data[j];
		data[j] = temp;
	}

	void swim(int k)
	{
		while (k>1 && !less(k/2,k))
		{
			exchange(k/2,k);
			k /= 2;
		}
	}

	void sink(int k)
	{
		int j = 2 * k;
		while (j <= len)
		{
			if (j<len && !less(j,j+1))
				j++;
			if (!less(j,k))
				break;
			exchange(k,j);
			k = j;
			j *= 2;

		}
	}


	public static void main(String[] args) 
	{
		MinPQ<Integer> queue = new MinPQ();
		for(int i = 30; i>0;i--)
			queue.push(i);

		for(int i=0;i<30;i++)
			System.out.println(queue.pop());

	}

}