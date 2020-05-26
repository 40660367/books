function getdir(){
    for element in `ls $1`
    do  
        dir_or_file=$1"/"$element
        if [ -d $dir_or_file ]
        then
	    echo '## '$dir_or_file  >> $1/nav.md
            getdir $dir_or_file
        else
	    basename=`basename $dir_or_file`
	    filename="${dir_or_file%.*}"
	    extension="${dir_or_file#*.}"
	    suffix=${dir_or_file##*.}

	    echo $basename
	    if [ $suffix == 'md' ]
	    then
		    #echo $basename
		    #echo $filename
		    title=`cat $dir_or_file | head -n 1`
		    title=${title/\# /}
		    echo '<li><a href=./'$filename'.html>'$title'</a></li>' >> $1/nav.html

			#将md文件中所有的md链接都换为.html
		    sed -i "s/.md)/.html)/g" $dir_or_file
	    fi
        fi  
    done
}
getdir $1
sed -i 's/
//g' $1/nav.html
