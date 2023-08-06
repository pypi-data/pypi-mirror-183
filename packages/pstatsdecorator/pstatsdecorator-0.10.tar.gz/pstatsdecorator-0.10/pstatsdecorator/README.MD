# Decorator for pstats

```python
$pip install pstatsdecorator

from pstatsdecorator import pstats_check

# Valid parameters for sortby:
# 'calls'
# 'cumulative'
# 'cumtime'
# 'file'
# 'filename'
# 'module'
# 'ncalls'
# 'pcalls'
# 'line'
# 'name'
# 'nfl'
# 'stdname'
# 'time'
# 'tottime'

# if return_stats is enabled, the function will always return a tuple.
# The last element in the tuple is the pstats data

@pstats_check(print_stats=False, return_stats=True, sortby="filename")
def testest1():
    print(isinstance("aaaaaaaaaa", str))
    print("aaaaaaaaaaaaaaaaa")
    x = 20 + 1
    return x



@pstats_check(print_stats=True, return_stats=False, sortby="line")
def testest2():
    import re

    re.findall("b", "bbbbbbbbbbbbbbbbbbbbb")
    print("bbbbbbbbbbbbbbbbbbbbb")
    print("bbbbbbbbbbbbbbbbbbbbb")
    x = 200 + 1
    return x
	


@pstats_check(print_stats=True, return_stats=False, sortby="cumulative")
def testest3():
    print("ccccccccccccccccccccccccc")
    x = 2000 + 1
    return x
	
	
print("k ----------------------------->")

k = testest1()
print(f"xxxxxxxxxxxxxxx\n{k=}")
print("<----------------------------- k")




print("k1 ----------------------------->")

k1 = testest2()
print(f"xxxxxxxxxxxxxxx\n{k1=}")
print("<----------------------------- k1")





print("k2 ----------------------------->")
k2 = testest3()
print(f"xxxxxxxxxxxxxxx\n{k2=}")
print("<----------------------------- k2")



Output:

k ----------------------------->
True
aaaaaaaaaaaaaaaaa
xxxxxxxxxxxxxxx
k=(21, "         7 function calls in 0.000 seconds\n\n   Ordered by: file name\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.000    0.000    0.000    0.000 <ipython-input-2-be27ae79f5ac>:21(testest1)\n        1    0.000    0.000    0.000    0.000 C:\\Users\\Gamer\\anaconda3\\envs\\dfdir\\lib\\cProfile.py:106(runcall)\n        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}\n        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}\n        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}\n        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}\n\n\n")
<----------------------------- k
k1 ----------------------------->
bbbbbbbbbbbbbbbbbbbbb
bbbbbbbbbbbbbbbbbbbbb
         85 function calls (84 primitive calls) in 0.000 seconds
   Ordered by: line number
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'findall' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       13    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__import__}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    13/12    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 C:\Program Files\JetBrains\PyCharm Community Edition 2020.3\plugins\python-ce\helpers\pydev\_pydev_bundle\pydev_import_hook.py:16(do_import)
        1    0.000    0.000    0.000    0.000 <ipython-input-2-be27ae79f5ac>:36(testest2)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:76(__init__)
        2    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:82(groups)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:87(_compile)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\cProfile.py:106(runcall)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:112(__init__)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:161(__len__)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:165(__getitem__)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:173(append)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:175(getwidth)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:225(__init__)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\re.py:233(findall)
        2    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:234(__next)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:250(match)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:255(get)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:287(tell)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\re.py:289(_compile)
        2    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\enum.py:358(__call__)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:436(_parse_sub)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:456(_generate_overlap_table)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:477(_get_iscased)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:485(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:494(_parse)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:560(_compile_info)
        2    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:619(isstring)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:622(_code)
        2    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\enum.py:670(__new__)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_compile.py:783(compile)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:928(fix_flags)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\sre_parse.py:944(parse)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\enum.py:977(__and__)
xxxxxxxxxxxxxxx
k1=201
<----------------------------- k1
k2 ----------------------------->
ccccccccccccccccccccccccc
         5 function calls in 0.000 seconds
   Ordered by: cumulative time
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 C:\Users\Gamer\anaconda3\envs\dfdir\lib\cProfile.py:106(runcall)
        1    0.000    0.000    0.000    0.000 <ipython-input-2-be27ae79f5ac>:54(testest3)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
xxxxxxxxxxxxxxx
k2=2001
<----------------------------- k2


```




