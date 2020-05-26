# Tornado 第五章：异步Web服务

到目前为止，我们已经看到了许多使Tornado成为一个Web应用强有力框架的功能。它的简单性、易用性和便捷性使其有足够的理由成为许多Web项目的不错的选择。然而，Tornado受到最多关注的功能是其异步取得和提供内容的能力，它有着很好的理由：它使得处理非阻塞请求更容易，最终导致更高效的处理以及更好的可扩展性。在本章中，我们将看到Tornado异步请求的基础，以及一些推送技术，这种技术可以使你使用更少的资源来提供更多的请求以编写更简单的Web应用。

## 5.1 异步Web请求

大部分Web应用（包括我们之前的例子）都是阻塞性质的，也就是说当一个请求被处理时，这个进程就会被挂起直至请求完成。在大多数情况下，Tornado处理的Web请求完成得足够快使得这个问题并不需要被关注。然而，对于那些需要一些时间来完成的操作（像大数据库的请求或外部API），这意味着应用程序被有效的锁定直至处理结束，很明显这在可扩展性上出现了问题。

不过，Tornado给了我们更好的方法来处理这种情况。应用程序在等待第一个处理完成的过程中，让I/O循环打开以便服务于其他客户端，直到处理完成时启动一个请求并给予反馈，而不再是等待请求完成的过程中挂起进程。

为了实现Tornado的异步功能，我们构建一个向Twotter搜索API发送HTTP请求的简单Web应用。这个Web应用有一个参数q作为查询字符串，并确定多久会出现一条符合搜索条件的推文被发布在Twitter上（"每秒推数"）。确定这个数值的方法非常粗糙，但足以达到例子的目的。图5-1展示了这个应用的界面。

![图5-1](https://atts.w3cschool.cn/attachments/image/cimg/2015-09-04_55e96e96df91e.jpg)

图5-1 异步HTTP示例：推率

我们将展示这个应用的三个不同版本：首先，是一个使用同步HTTP请求的版本，然后是一个使用带有回调函数的Tornado异步HTTP客户端版本。最后，我们将展示如何使用Tornado 2.1版本新增的gen模块来使异步HTTP请求更加清晰和易实现。为了理解这些例子，你不需要成为关于Twitter搜索API的专家，但一定的熟悉不会有害。你可以在https://dev.twitter.com/docs/api/1/get/search阅读关于搜索API的开发者文档。

### 5.1.1 从同步开始

代码清单5-1包含我们的推率计算器的同步版本的代码。记住我们在顶部导入了Tornado的httpclient模块：我们将使用这个模块的HTTPClient类来执行HTTP请求。之后，我们将使用这个模块的AsyncHTTPClient。

代码清单5-1 同步HTTP请求：

文件名:tweet_rate.py

```python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

这个程序的结构现在对你而言应该已经很熟悉了：我们有一个RequestHandler类和一个处理到应用根路径请求的IndexHandler。在IndexHandler的get方法中，我们从查询字符串中抓取参数q，然后用它执行一个到Twitter搜索API的请求。下面是最相关的一部分代码：

```
client = tornado.httpclient.HTTPClient()
response = client.fetch("http://search.twitter.com/search.json?" + \
        urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
body = json.loads(response.body)
```

这里我们实例化了一个Tornado的HTTPClient类，然后调用结果对象的fetch方法。fetch方法的同步版本使用要获取的URL作为参数。这里，我们构建一个URL来抓取Twitter搜索API的相关搜索结果（rpp参数指定我们想获得搜索结果首页的100个推文，而result_type参数指定我们只想获得匹配搜索的最近推文）。fetch方法会返回一个HTTPResponse对象，其 body属性包含我们从远端URL获取的任何数据。Twitter将返回一个JSON格式的结果，所以我们可以使用Python的json模块来从结果中创建一个Python数据结构。

fetch方法返回的HTTPResponse对象允许你访问HTTP响应的任何部分，不只是body。可以在[官方文档](http://www.tornadoweb.org/en/stable/httpclient.html)[1]阅读更多相关信息。

处理函数的其余部分关注的是计算每秒推文数。我们使用搜索结果中最旧推文与最新推文时间戳之差来确定搜索覆盖的时间，然后使用这个数值除以搜索取得的推文数来获得我们的最终结果。最后，我们编写了一个拥有这个结果的简单HTML页面给浏览器。

### 5.1.2 阻塞的困扰

到目前为止，我们已经编写了 一个请求Twitter API并向浏览器返回结果的简单Tornado应用。尽管应用程序本身响应相当快，但是向Twitter发送请求到获得返回的搜索数据之间有相当大的滞后。在同步（到目前为止，我们假定为单线程）应用，这意味着同时只能提供一个请求。所以，如果你的应用涉及一个2秒的API请求，你将每间隔一秒才能提供（最多！）一个请求。这并不是你所称的高可扩展性应用，即便扩展到多线程和/或多服务器 。

为了更具体的看出这个问题，我们对刚编写的例子进行基准测试。你可以使用任何基准测试工具来验证这个应用的性能，不过在这个例子中我们使用优秀的[Siege utility](http://www.joedog.org/siege-home/)工具进行测试。它可以这样使用：

```
$ siege http://localhost:8000/?q=pants -c10 -t10s
```

在这个例子中，Siege对我们的应用在10秒内执行大约10个并发请求，输出结果如图5-2所示。我们可以很容易看出，这里的问题是无论每个请求自身返回多么快，API往返都会以至于产生足够大的滞后，因为进程直到请求完成并且数据被处理前都一直处于强制挂起状态。当一两个请求时这还不是一个问题，但达到100个（甚至10个）用户时，这意味着整体变慢。

![图5-2](https://atts.w3cschool.cn/attachments/image/cimg/2015-09-04_55e96e9752d9b.jpg)

图5-2 同步推率获取

此时，不到10秒时间10个相似用户的平均响应时间达到了1.99秒，共计29次。请记住，这个例子只提供了一个非常简单的网页。如果你要添加其他Web服务或数据库的调用的话，结果会更糟糕。这种代码如果被 用到网站上，即便是中等强度的流量都会导致请求增长缓慢，甚至发生超时或失败。

### 5.1.3 基础异步调用

幸运的是，Tornado包含一个AsyncHTTPClient类，可以执行异步HTTP请求。它和代码清单5-1的同步客户端实现有一定的相似性，除了一些我们将要讨论的重要区别。代码清单5-2是其源代码。

代码清单5-2 异步HTTP请求：tweet_rate_async.py

```
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        client.fetch("http://search.twitter.com/search.json?" + \
                urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}),
                callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (self.get_argument('q'), tweets_per_second))
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

AsyncHTTPClient的fetch方法并不返回调用的结果。取而代之的是它指定了一个callback参数；你指定的方法或函数将在HTTP请求完成时被调用，并使用HTTPResponse作为其参数。

```
client = tornado.httpclient.AsyncHTTPClient()
client.fetch("http://search.twitter.com/search.json?" + »
urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}),
        callback=self.on_response)
```

在这个例子中，我们指定on_response方法作为回调函数。我们之前使用期望的输出转化Twitter搜索API请求到网页中的所有逻辑被搬到了on_response函数中。还需要注意的是@tornado.web.asynchronous装饰器的使用（在get方法的定义之前）以及在回调方法结尾处调用的self.finish()。我们稍后将简要的讨论他们的细节。

这个版本的应用拥有和之前同步版本相同的外观，但其性能更加优越。有多好呢？让我们看看基准测试的结果吧。

正如你在图5-3中所看到的，我们从同步版本的每秒3.20个事务提升到了12.59，在相同的时间内总共提供了118次请求。这真是一个非常大的改善！正如你所想象的，当扩展到更多用户和更长时间时，它将能够提供更多连接，并且不会遇到同步版本遭受的变慢的问题。

![图5-3](https://atts.w3cschool.cn/attachments/image/cimg/2015-09-04_55e96e97cd23f.jpg)

图5-3 异步推率获取

### 5.1.4 异步装饰器和finish方法

Tornado默认在函数处理返回时关闭客户端的连接。在通常情况下，这正是你想要的。但是当我们处理一个需要回调函数的异步请求时，我们需要连接保持开启状态直到回调函数执行完毕。你可以在你想改变其行为的方法上面使用@tornado.web.asynchronous装饰器来告诉Tornado保持连接开启，正如我们在异步版本的推率例子中IndexHandler的get方法中所做的。下面是相关的代码片段：

```
class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument('q')
        [... other request handler code here...]
```

记住当你使用@tornado.web.asynchonous装饰器时，Tornado永远不会自己关闭连接。你必须在你的RequestHandler对象中调用finish方法来显式地告诉Tornado关闭连接。（否则，请求将可能挂起，浏览器可能不会显示我们已经发送给客户端的数据。）在前面的异步示例中，我们在on_response函数的write后面调用了finish方法：

```
    [... other callback code ...]
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (self.get_argument('q'), tweets_per_second))
        self.finish()
```

### 5.1.5 异步生成器

现在，我们的推率程序的异步版本运转的不错并且性能也很好。不幸的是，它有点麻烦：为了处理请求 ，我们不得不把我们的代码分割成两个不同的方法。当我们有两个或更多的异步请求要执行的时候，编码和维护都显得非常困难，每个都依赖于前面的调用：不久你就会发现自己调用了一个回调函数的回调函数的回调函数。下面就是一个构想出来的（但不是不可能的）例子：

```
def get(self):
    client = AsyncHTTPClient()
    client.fetch("http://example.com", callback=on_response)

def on_response(self, response):
    client = AsyncHTTPClient()
    client.fetch("http://another.example.com/", callback=on_response2)

def on_response2(self, response):
    client = AsyncHTTPClient()
    client.fetch("http://still.another.example.com/", callback=on_response3)

def on_response3(self, response):
    [etc., etc.]
```

幸运的是，Tornado 2.1版本引入了tornado.gen模块，可以提供一个更整洁的方式来执行异步请求。代码清单5-3就是使用了tornado.gen版本的推率应用源代码。让我们先来看一下，然后讨论它是如何工作的。

代码清单5-3 使用生成器模式的异步请求：tweet_rate_gen.py

```
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch,
                "http://search.twitter.com/search.json?" + \
                urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (query, tweets_per_second))
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

正如你所看到的，这个代码和前面两个版本的代码非常相似。主要的不同点是我们如何调用Asynchronous对象的fetch方法。下面是相关的代码部分：

```
client = tornado.httpclient.AsyncHTTPClient()
response = yield tornado.gen.Task(client.fetch,
        "http://search.twitter.com/search.json?" + \
        urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
body = json.loads(response.body)
```

我们使用Python的yield关键字以及tornado.gen.Task对象的一个实例，将我们想要的调用和传给该调用函数的参数传递给那个函数。这里，yield的使用返回程序对Tornado的控制，允许在HTTP请求进行中执行其他任务。当HTTP请求完成时，RequestHandler方法在其停止的地方恢复。这种构建的美在于它在请求处理程序中返回HTTP响应，而不是回调函数中。因此，代码更易理解：所有请求相关的逻辑位于同一个位置。而HTTP请求依然是异步执行的，所以我们使用tornado.gen可以达到和使用回调函数的异步请求版本相同的性能，正如我们在图5-4中所看到的那样。