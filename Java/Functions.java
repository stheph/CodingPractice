import java.util.*;
import java.util.function.*;

class Functions
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
        System.out.println(fold_right((x, y) -> x - y, test, 0));

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

    private static <A, B> A fold_left(BiFunction<A,B,A> f, A acc, List<B> l)
    {
        if (l.size() == 0)
        {
            return acc;
        }
        else
        {
            B hd = l.get(0);
            List<B> tl = l.subList(1, l.size());

            return fold_left(f, f.apply(acc, hd), tl);
        }
    }

    private static <A, B> B fold_right(BiFunction<A,B,B> f, List<A> l, B acc)
    {
        if (l.size() == 0)
        {
            return acc;
        }
        else
        {
            A hd = l.get(0);
            List<A> tl = l.subList(1, l.size());

            return f.apply(hd, fold_right(f, tl, acc));
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