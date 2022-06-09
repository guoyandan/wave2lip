import random
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

from tqdm import tqdm
import traceback


def mp_handler(job):
    try:
        sleep(random.randint(1,20))
        print(job)
    except KeyboardInterrupt:
        exit(0)
    except:
        traceback.print_exc()


p = ThreadPoolExecutor(2)
futures = [p.submit(mp_handler, j) for j in range(100)]
_ = [r.result() for r in tqdm(as_completed(futures), total=len(futures))]
