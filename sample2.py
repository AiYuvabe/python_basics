input_str = input("Please enter a string for reversing: ")
len_str = len(input_str)
reverse_str = ""
i=1
while (i < len_str) :
  reverse_str = reverse_str + input_str[len_str-i-1]
  print(f"reverse : {reverse_str} value {-i}")
  i+=1
print(reverse_str)
