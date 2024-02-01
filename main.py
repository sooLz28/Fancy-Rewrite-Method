import time
input = input("Enter a Sentence: ")
allLetters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBN!@#$%^&*()_+-= "
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