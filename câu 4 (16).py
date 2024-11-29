words = input("Nhập một dãy các từ (cách nhau bởi dấu cách): ").split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Các từ dài nhất trong dãy là:", ', '.join(longest_words))
