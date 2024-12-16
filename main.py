import time
input = input("Enter a Sentence: ")
allLetters = "qwe8rtyuiopa1s9dfgh5jklzxcvbnm2QWE4RTYU0IOPA7S3DFG6HJKLZXCVBN!@#$%^&*()_+-= "
output = ""
i = 0
while output != input:
  for letter in allLetters:
    if letter == input[i]:
      print("Succeed")
      output += input[i]
      print(output)
      if output == input:
        break
      i += 1
    else:
      print("Failed")
      print(output + letter)
    time.sleep(0.01)