# Flask 简介

## 什么是Web框架？

Web应用程序框架或简单的Web框架表示一组库和模块，它们使Web应用程序开发人员能够编写应用程序，而不必担心如协议，线程管理等低层细节。

## 什么是Flask？

Flask是一个用Python编写的Web应用程序框架。 它由Armin Ronacher开发，他领导着一个名为Pocco的Python爱好者的国际组织。 Flask基于Werkzeug WSGI工具包和Jinja2模板引擎。 这两个都是Pocco项目。

## WSGI

Web服务器网关接口(WSGI)已被采纳为Python Web应用程序开发的标准。 WSGI是Web服务器和Web应用程序之间通用接口的规范。

## WERKZEUG

它是一个WSGI工具包，它实现了请求，响应对象和其他实用程序功能。 这可以在其上构建Web框架。 Flask框架使用Werkzeug作为其一个基础模块之一。

## Jinja2

jinja2是Python的流行模板引擎。 网页模板系统将模板与特定的数据源结合起来呈现动态网页。

Flask通常被称为**微框架**。 它旨在保持应用程序的核心简单且可扩展。 Flask没有用于数据库处理的内置抽象层，也没有形成验证支持。 相反，Flask支持扩展以将这些功能添加到应用程序中。部分流行的Flask扩展将在本教程后续章节中讨论。
