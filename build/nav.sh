cd $1
ls *.md | while read line
do

	#echo $line
	title=`cat $line | head -n 1`
	#title=`echo $title`
	#title=${title/\# /}
	title=(${title////})
	title=${title[1]}${title[2]}

	echo $title


	filename=(${line//./ })
	filename=${filename[0]}
	htmllink=$filename.html
	
	echo '- [' $title ]\(./$htmllink\) >> nav.md

done
sed -i 's///g' nav.md
