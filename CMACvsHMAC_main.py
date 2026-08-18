import hmac
import hashlib
import time
import os
from Crypto.Hash import CMAC
from Crypto.Cipher import AES
import matplotlib.pyplot as plt

####>>>>>>....... plain text sizes
def benchmark_mac(message_sizes=[1, 10, 100, 1024, 10240, 102400]): ##>>>..... from 1kb
    key = b"Secret_key_32_bytes_long!!!!!!!!"  ####>>>>>>> the key used for both macs
    results = {'sizes': [], 'hmac_time': [], 'cmac_time': []}  ###>>..... using it in plots 

    print(">>>>>>.......... HMAC vs CMAC Benchmark ...........<<<<<< \n")
    
    for size_kb in message_sizes:
        size_bytes = size_kb * 1024
        ###>>>>>>>>>................generate random plain txts with the defined sizes
        message = os.urandom(size_bytes)   

        ####>>>>>>>>>>>>>>>.................... HMAC >> SHA512
        start = time.perf_counter()
        h = hmac.new(key, message, hashlib.sha512)
        hmac_tag = h.hexdigest()   ####>>> digest in hexadecimal form
        hmac_time = time.perf_counter() - start  ###>>end time-start time 

        ##>>>>>>>>>>>>>>>>............................CMAC >>  AES 128 bits
        start = time.perf_counter()
        cmac = CMAC.new(key[:16], ciphermod=AES)  #>>>..... 16 bits for AES
        cmac.update(message)
        cmac_tag = cmac.hexdigest()  ####>>> digest in hexadecimal form
        cmac_time = time.perf_counter() - start 
         ####........... append them to the results 
        results['sizes'].append(size_kb)
        results['hmac_time'].append(hmac_time)
        results['cmac_time'].append(cmac_time)

        ####>>>>.......... output .....................<<<<<<<<<<<
        print(f"{size_kb:6}KB | HMAC: {hmac_time:.6f}s | CMAC: {cmac_time:.6f}s | "  ###>>....ta 6 ragham aashare only
              f"HMAC digest: {hmac_tag[:16]}... | CMAC digest: {cmac_tag[:16]}...") ###>>..... ta 16 bit neshun mide

    #####>>>>>>>>>>>>........................... result  Plot  ....................<<<<<<<<<<<<<<<<
    plt.figure(figsize=(10,7))
    plt.plot(results['sizes'], results['hmac_time'], 'r-o', linewidth=2 , label='HMAC-SHA512')
    plt.plot(results['sizes'], results['cmac_time'], 'b-o', linewidth=2 , label='CMAC-AES128')
    plt.xlabel('Message Size (KB)', color='green',fontweight='bold')
    plt.ylabel('Time (seconds)', color='green',fontweight='bold')
    plt.title('HMAC vs CMAC Performance Comparison', color='purple', fontweight='bold',fontsize=24)
    plt.legend()
    plt.grid(True, linestyle='--') ##.....background lines
    ####>>...... x and y start from 0
    plt.xlim(left=0)                    
    plt.ylim(bottom=0)
    plt.savefig('hmac_vs_cmac_performance.png',dpi=300, bbox_inches='tight')
    plt.show()

    return results


if __name__ == "__main__":
    benchmark_mac()
    