# Jupyter 简介



![Jupyter-Logo](./images/logo.png)

Jupyter notebook（又称IPython notebook）是一个交互式的笔记本，支持运行超过40种编程语言。本文中，我们将介绍Jupyter notebook的主要特点，了解为什么它能成为人们创造优美的可交互式文档和教育资源的一个强大工具。

Jupyter Notebook 的本质是一个 Web 应用程序，便于创建和共享文学化程序文档，支持实时代码，数学方程，可视化和 [markdown](./markdown.html)。 用途包括：数据清理和转换，数值模拟，统计建模，机器学习等等。

jupyter官网：https://jupyter.org/

## Jupyter 架构

**Jupyter组件**

Jupyter包含以下组件：

Jupyter Notebook 和 Notebook 文件格式

Jupyter Qt 控制台

内核消息协议 (kernel messaging protocol)

许多其他组件

## Jupyter 内核

Jupyter Notebook 与 IPython终端 共享同一个内核 [3] 。

内核进程可以同时连接到多个前端。 在这种情况下，不同的前端访问的是同一个变量 [3] 。

这个设计可以满足以下两种需求：

- 相同内核不同前端，用以支持，快速开发新的前端
- 相同前端不同内核，用以支持，新的开发语言