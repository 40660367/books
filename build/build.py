#pip3 install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple/
#or
#pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple/

import os,json
import markdown as md
import codecs


def makehtml(path,nav=0,level=0,lessontype="terminal",backendtype='k',datalanguage="python"):
    
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
                title=md_htmlcontent.split('\n')[0]
                title=title.replace('<h1>','')
                title=title.replace('</h1>','')
                title=title+" - FreeAIHub"
                template=template.replace('{topheader}',topheader)
                template=template.replace('{title}',title)
                template=template.replace('{leftnav}', leftnavcontent)
                template=template.replace('{content}',md_htmlcontent)
                template=template.replace('{backendtype}',backendtype)
                template=template.replace('{datalanguage}',datalanguage)
                
                html_file.write(template)
                html_file.close()
                
        for name in dirs:
            makehtml(os.path.join(root,name),nav=leftnavcontent,level=1)
            
            
            
            
            
#lesson config
news=['aboutus']
cell_python=['d2l-mxnet','d2l-pytorch','pandas','numpy','keras','ml','seaborn','scipy','sklearn','python']
cell_ir=['r']
cell_julia=['julia']
terminal=['java','pyqt','turtle','php','jmeter','html','elasticsearch','hive','hbase','redis','scala','c','spark','sqlite','tornado',\
         'vim','go','git','flask','cpp','django','postgresql','ds-in-c','neo4j','ds-in-python','lua','hadoop','mysql','mongodb','nginx','shell',\
         'nodejs','linux','jupyter']

typev=['docker']
typec=['mysql-ms']


#lesson build
for item in typev:
    makehtml('../'+item,lessontype="terminal",backendtype='c')
    
for item in news:
    makehtml('../'+item,lessontype="news")
    
for item in cell_python:
    makehtml('../'+item,lessontype="cell")

for item in cell_ir:
    makehtml('../'+item,lessontype="cell",datalanguage='ir')

for item in cell_julia:
    makehtml('../'+item,lessontype="cell",datalanguage='julia')

for item in terminal:
    makehtml('../'+item,lessontype="terminal")
    
    
    
    
# index config
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


# index build
for coursetype in courses:
    final+=lessontypehtmltemplate.replace('{name}',courses[coursetype]['name'])
    for item in courses[coursetype]['lessons']:
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
print('index.html bulid')