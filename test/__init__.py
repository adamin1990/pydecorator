from filecmp import cmp
import functools
# sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))   python2 的写法
sorted_ignore_case = functools.partial(sorted, key=lambda a:a.upper())
print (sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))