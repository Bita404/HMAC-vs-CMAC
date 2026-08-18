## Requirements
• Windows and Linux operating systems
• Python 3.8 or higher
# For HMAC Implementation: 
o Use Python standard libraries: hmac and hashlib
o Support at least HMAC-SHA512 and HMAC-SHA256
# For CMAC Implementation: 
o Use pycryptodomelibrary (Crypto.Hash.CMAC and Crypto.Cipher.AES)
o Support CMAC-AES128 (primary) and CMAC-AES256 (optional)
# For Benchmarking & Visualization:
•time module for performance measurement
•os and random for generating test messages
•matplotlib for generating performance comparison charts (optional but recommended)
## Functional Code Requirements
•The program shall have a main function to run performance benchmarks
•The system shall support testing with variable message sizes (1 KB to 10 MB)
•The code shall measure and compare execution time of HMAC and CMAC
•The code shall generate and display MAC tags for both algorithms
•The program shall output a clear comparison table in the console
•The code must be modular(separate functions for HMAC, CMAC, 
benchmarking, and visualization
## Output Requirements
• Message size
• HMAC execution time
• CMAC execution time
• Generated tags (shortened)
•Save performance chart as hmac_vs_cmac_performance.png

## Conclusion
both HMAC and CMAC demonstrated strong performance in 
generating message authentication tags. While HMAC-SHA512 was 
generally faster than CMAC-AES128 across different message sizes, 
the performance difference was not significant enough to declare one 
clearly superior. This shows that speed is not the only important 
factor when choosing a MAC. HMAC offers greater flexibility and 
excellent software performance, making it ideal for web applications, 
APIs, and general-purpose systems. On the other hand, CMAC 
provides robust security and performs very well in hardware 
environments where AES acceleration is available. Ultimately, the 
choice between HMAC and CMAC should be based on the specific 
requirements of the application, such as deployment environment, 
hardware support, key management needs, and security properties.


