ls $1/*.md | while read line
do
    kernel="<code class="gatsby-kernelname" data-language=""$2""></code>"
    echo -e >> $line;
    echo $kernel >> $line;
    echo $line
done