import time
start_time=time.time()
f = open("randomparas.txt","r",encoding="UTF-8") 
huge_text = f.read()

chunks = huge_text.split("\n")
for i,chunk in enumerate(chunks):
    # processing each chunk
    # 1. word length
    words = chunk.split()
    sentence = chunk.split(".")
    # other mining elements
    # print(i+1,len(words),len(sentence))

end_time=time.time()
print("\nExecution time: ",end_time-start_time)
f.close() 