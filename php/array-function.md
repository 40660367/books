# PHP 数组函数

PHP提供了各种数组函数来访问和操作数组的元素。 下面给出了重要的PHP数组函数。

## PHP array()函数

PHP `array()`函数创建并返回一个数组。 它允许您创建索引，关联和多维数组。

**语法**

```php
array array ([ mixed $... ] )
```

**示例**

文件名:array-funciton-array.php

```php
<?php    
$season=array("summer","winter","spring","autumn");    
echo "Season are: $season[0], $season[1], $season[2] and $season[3]";    
?>
```

```bash
php /var/www/html/array-funciton-array.php
```

URL预览:`{host0.http_url}array-funciton-array.php`

## PHP array_change_key_case()函数

PHP `array_change_key_case()`函数更改数组的所有键的大小写。

**注意：** 它仅更改键的大小写。

**语法：**

```php
array array_change_key_case ( array $array [, int $case = CASE_LOWER ] )
```

**示例**

文件名:array-funciton-array_change_key_case1.php

```php
<?php    
$salary=array("Maxsu"=>"550000","Vimal"=>"250000","Ratan"=>"200000");    
print_r(array_change_key_case($salary,CASE_UPPER));   
?>
```

```bash
php /var/www/html/array-funciton-array_change_key_case1.php
```

URL预览:`{host0.http_url}array-funciton-array_change_key_case1.php`

**示例**

文件名:array-array_change_key_case2.php

```php
<?php    
$salary=array("Maxsu"=>"550000","Vimal"=>"250000","Ratan"=>"200000");    
print_r(array_change_key_case($salary,CASE_LOWER));   
?>
```

```bash
php /var/www/html/array-array_change_key_case2.php
```

URL预览:`{host0.http_url}array-array_change_key_case2.php`

## PHP array_chunk()函数

PHP `array_chunk()`函数将数组拆分为块。通过使用`array_chunk()`方法，可以将数组分成许多部分。

**语法：**

```php
array array_chunk ( array $array , int $size [, bool $preserve_keys = false ] )
```

**实例**

文件名:array-funciton-array_chunk.php

```php
<?php    
$salary=array("Maxsu"=>"550000","Vimal"=>"250000","Ratan"=>"200000");    
print_r(array_chunk($salary,2));   
?>
```

```bash
php /var/www/html/array-funciton-array_chunk.php
```

URL预览:`{host0.http_url}array-funciton-array_chunk.php`

## PHP count()函数

PHP `count()`函数计算数组中的所有元素的数量。

**语法**

```php
int count ( mixed $array_or_countable [, int $mode = COUNT_NORMAL ] )
```

**示例**

文件名:array-funciton-count.php

```php
<?php    
$season=array("summer","winter","spring","autumn");    
echo count($season);    
?>
```

```bash
php /var/www/html/array-funciton-count.php
```

URL预览:`{host0.http_url}array-funciton-count.php`

## PHP sort()函数

PHP `sort()`函数排序数组中的所有元素。

**语法**

```php
bool sort ( array &$array [, int $sort_flags = SORT_REGULAR ] )
```

**实例**

文件名:array-funciton-sort.php

```php
<?php    
$season=array("summer","winter","spring","autumn");    
sort($season);  
foreach( $season as $s )    
{    
  echo "$s<br />";    
}    
?>
```

```bash
php /var/www/html/array-funciton-sort.php
```

URL预览:`{host0.http_url}array-funciton-sort.php`

## PHP array_reverse()函数

PHP `array_reverse()`函数返回一个包含相反顺序的元素的数组。

**语法**

```
array array_reverse ( array $array [, bool $preserve_keys = false ] )
```

**示例**

文件名:array-funciton-array_reverse.php

```php
<?php    
$season=array("summer","winter","spring","autumn");    
$reverseseason=array_reverse($season);  
foreach( $reverseseason as $s )    
{    
  echo "$s<br />";    
}    
?>
```

```bash
php /var/www/html/array-funciton-array_reverse.php
```

URL预览:`{host0.http_url}array-funciton-array_reverse.php`

## PHP array_search()函数

PHP `array_search()`函数搜索数组中的指定值。 如果搜索成功，则返回键。

**语法**

```php
mixed array_search ( mixed $needle , array $haystack [, bool $strict = false ] )
```

**示例**

文件名:array-funciton-array_search.php

```php
<?php    
$season=array("summer","winter","spring","autumn");    
$key=array_search("spring",$season);  
echo $key;    
?>
```

```bash
php /var/www/html/array-funciton-array_search.php
```

URL预览:`{host0.http_url}array-funciton-array_search.php`

## PHP array_intersect()函数

PHP `array_intersect()`函数返回两个数组的交集。 换句话说，它返回两个数组的匹配元素。

语法

```php
array array_intersect ( array $array1 , array $array2 [, array $... ] )
```

**示例**

文件名:array-funciton-array_intersect.php

```php
<?php    
$name1=array("maxsu","john","vivek","minsu");    
$name2=array("umesh","maxsu","kartik","minsu");    
$name3=array_intersect($name1,$name2);  
foreach( $name3 as $n )    
{    
  echo "$n<br />";    
}    
?>
```

```bash
php /var/www/html/array-funciton-array_intersect.php
```

URL预览:`{host0.http_url}array-funciton-array_intersect.php`