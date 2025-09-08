from sentiment_analysis import score_paragraph

if __name__ == "__main__":
    f = open("randomparas.txt","r",encoding="utf-8")
    huge_text = f.read()

    chunks = huge_text.split("\n")
    for i,chunk in enumerate(chunks):
        print(f"Para{i} , Score is {score_paragraph(chunk)}")
    
    f.close()