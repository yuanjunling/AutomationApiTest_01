import claude

# 创建一个 ChatGPT 模型的实例
model = claude.load_model()
# 将问题以字符串的形式传递给 model,然后调用 generate 方法获取响应
question = "Hello, how are you today?"
response = model.generate(question)
# 输出响应结果
print(response)
