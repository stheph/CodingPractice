import java.util.*;
import java.util.function.Function;

class Map
{
    public static void main(String[] args)
    {
        List<Integer> test = new ArrayList<>();
        test.add(1);
        test.add(2);
        test.add(3);
        test.add(4);
        test.add(5);

        List<Integer> mapped = map(x -> x + 1, test);
        System.out.println(printList(mapped));

    }

    private static <T, R> List<R> map(Function<T,R> f, List<T> l)
    {
        if (l.size() == 0)
        {
            return new ArrayList<R>();
        }
        else
        {
            T hd = l.get(0);
            List<T> tl = l.subList(1, l.size());

            List<R> out = new ArrayList<R>();
            out.add(f.apply(hd));
            out.addAll(map(f, tl));

            return out;
        }
    }

    private static String printList(List<Integer> l)
    {
        List<String> outs = new ArrayList<>();
        for (int i = 0; i < l.size(); i++)
        {
            outs.add(Integer.toString(l.get(i)));
        }
        return "[" + String.join(", ", outs) +  "]";
    }

}