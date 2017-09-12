## 阶段总结

1. 创建 4个HTML页面，home主界面，查询结果，历史，帮助展示相关内容
2. 连接flask和html，怎么把html的请求传递到点py文件中？也就是浏览器请求怎么请求？
2.1  一开始我只知道input元素，后来查询到可以用`<form>` 标签

 **`<form>` 标签**
> - `<form>` 标签用于为用户输入创建 HTML 表单。
> - 表单用于向服务器传输数据。
> - 表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。表单还可以包含 menus、textarea、fieldset、legend 和 label 元素。

**`<input>` 标签**
> - `<input>` 标签用于搜集用户信息。
> - 根据不同的 type 属性值，输入字段拥有很多种形式。输入字段可以是文本字段、复选框、掩码后的文本控件、单选按钮、按钮等等。

2.2  form 标签的属性

属性 | 值 | 描述
|--- | ---|---|
action | URL | 规定当提交表单时向何处发送表单数据
method | get/post | 规定用于发送 form-data 的 HTTP 方法
name | form_name | 规定表单的名称

3. 服务端接收HTML的请求数据，通过 `request.args.get` 可以拿到HTML中的input 的 name的值，拿到城市，请求API并返回数据

4. 怎么把返回数据呈现在HTML上，这点查看了Flask的[Quick Start](http://flask.pocoo.org/docs/0.12/quickstart/)，然后google了好久，走了些弯路，反而增加了认知成本，不如从文档入手，MVP ~ Minimum Viable Product, 最小可行产品，对于不懂的知识点也应该如此，不要迷失在茫茫文档之中。

5. 通过`return render_template('result.html', weather=weather)
`指向点击后的呈现HTML，传递数据，在HTML中通过 `{{weather}}` 拿到数据