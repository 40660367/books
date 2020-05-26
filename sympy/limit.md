# SymPy Limit求极限


$$
\lim_{x \to 0} \frac{sin(x)}{x}
$$


```python
limt(sin(x)/x,x,0)
```



```python
expr = Limit((cos(x) - 1)/x, x, 0)
expr
```

```python
expr.doit()
```



要仅在一侧评估极限，请将`'+'`或`'-'`作为第四个参数传递给`limit`。例如，要计算
$$
\lim_{x\to 0^+}\frac{1}{x},
$$


```python
limit(1/x, x, 0, '+')
```
反之则
```python
limit(1/x, x, 0, '-')
```

