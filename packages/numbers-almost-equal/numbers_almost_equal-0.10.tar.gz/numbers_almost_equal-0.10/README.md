# Checks if 2 numbers (int) are almost equal

```python

allowed_difference will be set to 1 if the number that you pass is not in [1000000,100000,10000,1000,100,10]
That means 1 is the minimum difference you can check for. I wrote this function especially to compare ints.
It works with floats too, but you can't go below 1 without changing the source code 

$pip install numbers-almost-equal
from numbers_almost_equal import are_numbers_equal

(are_numbers_equal(number1=70, number2=71, allowed_difference=1))
Out[4]: True
(are_numbers_equal(number1=70, number2=72, allowed_difference=1))
Out[5]: False
(are_numbers_equal(number1=60, number2=59, allowed_difference=1))
Out[6]: True
(are_numbers_equal(number1=60, number2=58, allowed_difference=1))
Out[7]: False
(are_numbers_equal(number1=60, number2=58, allowed_difference=10))
Out[8]: True
(are_numbers_equal(number1=60, number2=71, allowed_difference=10))
Out[10]: False
(are_numbers_equal(number1=60, number2=70, allowed_difference=10))
Out[11]: True
(are_numbers_equal(number1=60, number2=70, allowed_difference=100))
Out[12]: True

(are_numbers_equal(number1=60, number2=159, allowed_difference=100))
Out[13]: True

(are_numbers_equal(number1=60, number2=161, allowed_difference=100))
Out[15]: False

(are_numbers_equal(number1=60, number2=161, allowed_difference=1000))
Out[16]: True

(are_numbers_equal(number1=60, number2=1059, allowed_difference=1000))
Out[17]: True

(are_numbers_equal(number1=60, number2=1061, allowed_difference=1000))
Out[18]: False

(are_numbers_equal(number1=60, number2=1061, allowed_difference=10000))
Out[19]: True

(are_numbers_equal(number1=60, number2=10059, allowed_difference=10000))
Out[20]: True
(are_numbers_equal(number1=60, number2=10061, allowed_difference=10000))
Out[22]: False

(are_numbers_equal(number1=60, number2=10061, allowed_difference=100000))
Out[24]: True

(are_numbers_equal(number1=60, number2=100059, allowed_difference=100000))
Out[26]: True
(are_numbers_equal(number1=60, number2=100061, allowed_difference=100000))
Out[27]: False
(are_numbers_equal(number1=60, number2=1000061, allowed_difference=1000000))
Out[29]: False
(are_numbers_equal(number1=60, number2=1000059, allowed_difference=1000000))
Out[30]: True


```


