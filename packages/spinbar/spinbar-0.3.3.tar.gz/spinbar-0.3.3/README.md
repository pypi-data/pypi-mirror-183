<h1>its Literally just a progress bar with a spinning end</h1>
<h1>Example:</h1>

```
import time
import spinbar
sbar = spinbar.SpinBar()
for _ in range(100):
    sbar.next()
    time.sleep(0.2)
```
