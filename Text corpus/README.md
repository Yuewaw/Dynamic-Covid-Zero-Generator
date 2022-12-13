# 语料库

## 如何处理

1. 将原始内容复制到 `origin` 文件（此时需要稍做内容清洗，只复制自然段，删除无用信息）。
2. 运行 `main.py`，此时将会把 `origin` 文件中按 `。` 分隔符把所有句子按行分开并写入 `sentence` 文件。
3. 对 `sentence` 文件进行内容清洗。
4. 运行 `tojs.py`，此时将会把 `sentence` 文件中的句子按行改为 JavaScript 适用的数组格式，并写入 `json` 文件。
5. 将 `json` 文件内容放入 `index.html`。

## 内容来源

1.	https://baike.baidu.com/item/%E5%8A%A8%E6%80%81%E6%B8%85%E9%9B%B6
2.	http://health.people.cn/n1/2022/0508/c14739-32416935.html
3.	http://m.people.cn/n4/2022/0413/c3605-15533760.html
4.	http://health.people.cn/n1/2022/0412/c14739-32397266.html
5.	http://health.people.cn/n1/2022/0318/c14739-32378624.html
6.	http://health.people.cn/n1/2022/0427/c14739-32409638.html
7.	http://m.people.cn/n4/2022/0319/c34-15490731.html
8.	http://m.people.cn/n4/2022/0508/c25-20040485.html
9.	http://health.people.cn/n1/2022/0510/c14739-32418376.html
10.	http://health.people.cn/n1/2022/0506/c14739-32415148.html
11.	http://health.people.cn/n1/2022/0416/c14739-32400626.html
12.	http://health.people.cn/n1/2022/0319/c14739-32378791.html
13.	http://health.people.cn/n1/2022/0327/c14739-32385060.html
14.	http://m2.people.cn/news/default.html?s=Ml8yXzQwMDgwMzU4XzE4NjMzMF8xNjYwNTIyOTUx
15.	http://health.people.cn/n1/2022/0207/c14739-32346651.html
16.	http://m.people.cn/n4/2022/0407/c1257-15522491.html