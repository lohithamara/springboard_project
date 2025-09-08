import multitasking
import time
from sentiment_analysis import score_paragraph

start_time = time.time()
@multitasking.task
def process_chunk(i, chunk):
    print(f"Para{i}, Score: {score_paragraph(chunk)}")
if __name__ == "__main__":
    with open("randomparas.txt", "r", encoding="utf-8") as f:
        huge_text = f.read()
    chunks = huge_text.split("\n")
    for i, chunk in enumerate(chunks):
        process_chunk(i, chunk)
    multitasking.wait_for_tasks() 
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")