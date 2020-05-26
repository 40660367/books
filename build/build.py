#pip3 install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple/
#or
#pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple/
import os,json
import markdown as md
import codecs
from lxml import etree

def makehtml(path,lessonname,nav=0,level=0,lessontype="terminal",backendtype='k',datalanguage="python"):
    
    templatefilepath='./template/{templatefilename}.html'
    templatefilepath=templatefilepath.replace('{templatefilename}',lessontype)
    htmltemplatefile=open(templatefilepath,'r',encoding="utf-8")
    htmltemplate=htmltemplatefile.read()
    htmltemplatefile.close()


    if level!=0:
        leftnavcontent=nav
    else:
        navfilefile=open(os.path.join(path,"nav.html"), mode="r", encoding="utf-8")
        leftnavcontent=navfilefile.read()
        leftnavcontent=leftnavcontent.replace('./',"/"+lessonname+"/")
        navfilefile.close()
    
    
    topheadertemplate=open('./template/topheader.html','r',encoding="utf-8")
    topheader=topheadertemplate.read()
    
    for root,dirs,files in os.walk(path):
        for name in files:
            abs_path=os.path.join(root,name)
            print(abs_path)
            (filename,extension)=os.path.splitext(name)
            print("filename",filename,"   extension",extension)
            
            if extension==".md":
                md_file = codecs.open(abs_path, mode="r", encoding="utf-8")
                md_htmlcontent = md.markdown(md_file.read(),extensions=['fenced_code','tables'])
                md_file.close()
                

                html_filename=os.path.join(os.path.dirname(abs_path),filename+".html")
                print(html_filename)
                html_file = codecs.open(html_filename, mode="w", encoding="utf-8")
                
                
                template=htmltemplate
                
                

                #TDK
                domtree = etree.HTML(md_htmlcontent)
                #Title
                title=domtree.xpath(".//h1/text()")[0]
                template=template.replace('{title}',title+" - FreeAIHub")
                #用用p做D,二级三级标题做为K
                descriptions=domtree.xpath(".//p/text()")
                description=''.join(descriptions)[:200]
                description=description.replace("\"","")
                template=template.replace('{description}',description)
                
                keywords2=domtree.xpath(".//h2/text()")
                keywords3=domtree.xpath(".//h3/text()")
                keywords=','.join(keywords2)+','.join(keywords3)[:-60]
                template=template.replace('{keyword}',keywords)
                
                
                template=template.replace('{topheader}',topheader)
                template=template.replace('{content}',md_htmlcontent)
                
                #leftnav+当前链接样式
                currentlink=filename+".html"
                print(leftnavcontent)
                thisleftnavcontent=leftnavcontent.replace('href="/'+lessonname+'/'+currentlink+'"','class="current"')
                template=template.replace('{leftnav}', thisleftnavcontent)
                
                #上一页，下一页
                domtree = etree.HTML(leftnavcontent)
                article_text_list=domtree.xpath(".//a/text()")
                article_link_list=domtree.xpath(".//a/@href")
                
                if '/'+lessonname+'/'+currentlink in domtree.xpath(".//a/@href"):
                    current_article_id=domtree.xpath(".//a/@href").index('/'+lessonname+'/'+currentlink)
                    
                    prev_article_id=current_article_id-1
                    next_article_id=current_article_id+1

                    prev_article="<a href="+article_link_list[prev_article_id]+" class='prev_article'>"+article_text_list[prev_article_id]+"</a>"
                    if current_article_id==0:prev_article="无"
                    if next_article_id<=len(article_text_list)-1:
                        next_article="<a href="+article_link_list[next_article_id]+" class='next_article'>"+article_text_list[next_article_id]+"</a>"
                    else:
                        next_article="无"

                    prev_next_nav="< 上一篇:"+prev_article+"       |       下一篇："+next_article+"  >"
                    template=template.replace('{prev_next_nav}',prev_next_nav)
                
                
                
                
                template=template.replace('{backendtype}',backendtype)
                template=template.replace('{datalanguage}',datalanguage)
                
                html_file.write(template)
                html_file.close()
                
        for name in dirs:
            makehtml(os.path.join(root,name),lessonname,nav=leftnavcontent,level=1)
            
            
news=['aboutus']
cell_python=['pandas','numpy','ml','seaborn','scipy','sklearn','python','ds-in-python']
cell_ir=['r']
cell_julia=['julia']
terminal=['java','pyqt','turtle','php','jmeter','html','elasticsearch','hive','hbase','redis','scala','c','spark','sqlite','tornado',\
         'vim','go','git','flask','cpp','django','postgresql','ds-in-c','neo4j','lua','hadoop','mysql','mongodb','nginx','shell',\
         'node.js','linux','jupyter']

typev=['docker']
typec=['mysql-replication']
typek8sv=['kubernetes']

for item in typev:
    makehtml('../'+item,item,lessontype="terminal",backendtype='v')

for item in typec:
    makehtml('../'+item,item,lessontype="terminal",backendtype='c')
    
for item in typek8sv:
    makehtml('../'+item,item,lessontype="terminal",backendtype='k8sv')

for item in terminal:
    makehtml('../'+item,item,lessontype="terminal")
for item in news:
    makehtml('../'+item,item,lessontype="news")
for item in cell_python:
    makehtml('../'+item,item,lessontype="cell")

for item in cell_ir:
    makehtml('../'+item,item,lessontype="cell",datalanguage='ir')

for item in cell_julia:
    makehtml('../'+item,item,lessontype="cell",datalanguage='julia-1.3')
    

    
#index
indexjson=json.loads(open('./template/index.json',encoding='utf-8').read())

lessontypehtmltemplate='''
            <div class="row clearfix">
                <div class="index-title"><h4>{name}</h4></div>
                <!--Service Style Three-->
'''
lessontypehtmltemplateend='''
            </div>
'''

lessonhtmltemplate='''
                    <div class="service-style-three col-md-4 col-sm-6 col-xs-12">
                        <div class="inner-box">
                            <div class="icon"><figure class="image"><a href="{link}"><img src="{img}" alt="{name}"></a></figure></div>
                            <h3><a href="{link}">{name}</a></h3>
                            <div class="text">{des}</div>
                        </div>
                    </div>
'''

final=''
courses=indexjson['Course']['CourseList']
for coursetype in courses:
    final+=lessontypehtmltemplate.replace('{name}',courses[coursetype]['name'])
    for item in courses[coursetype]['lessons']:
#         print(item)
        temp=lessonhtmltemplate.replace('{link}',item['link'])
        temp=temp.replace('{name}',item['name'])
        temp=temp.replace('{des}',item['des'])
        temp=temp.replace('{img}',item['img'])
        final+=temp
        temp=''
    final+=lessontypehtmltemplateend
    
index_file = codecs.open("../index.html", mode="w", encoding="utf-8")
index_template = codecs.open("./template/index.template", mode="r", encoding="utf-8").read()

index_template=index_template.replace('{lessonlists}',final)
index_file.write(index_template)
index_file.close()