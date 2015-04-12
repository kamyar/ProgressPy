# ProgressPy
Simple Command Line Progress Bar for Python



Usage:
```python  
import progress  
import time  
progressBar = progress.Progress(total=150, title="Task in progress")  
for i in range(150):  
    progressBar.update(count=i+1, suffix="Currently doing task {0}".format(i+1))  
    time.sleep(0.05)  
```