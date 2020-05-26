# Nginx 示例8:重写HTTP响应(sub_filter)

用户替换html中的字符

```
  location / {
        root   /opt/app/code/;
        random_index on;
        index  index.html index.htm;
        sub_filter '<h1>Admin' '<h1>ggggg';  //第一个参数是要被替换的，第二个参数是替换后的
        sub_filter_once off;   //替换所有的，默认是on，替换第一个
     }
```



    location / {
            # First attempt to serve request as file, then
            # as directory, then fall back to displaying a 404.
            try_files $uri $uri/ =404;
            sub_filter '{url}' $hostname-http.freeaihub.cn;
    }