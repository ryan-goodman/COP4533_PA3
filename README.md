# COP4533 Programming Assignment 3
Ryan Goodman (UFID: 46759399)
## Instructions to Run
- Navigate to /src and run the following commands. Note that you should use whatever python alias your device has.
> "python inputPreparation.py k c" where $k$ corresponds to the length of the dictionary and $k≤26$ and $c$ corresponds to the length of strings A and B

> "python hclvs.py"
## Other Info
- The input.txt file format should match the format given on the assignment exactly; there is no guarantee that things will work if a different format is used (inputPreparation.py will follow this input format).
- The assignment did not specify which characters could or could not be in the alphabet, so I decided to use the first $k$ lowercase letters in the alphabet and require that $k≤26$ be true
- The weights for any given character in the alphabet are randomly generated between 1 and 10.
- The current input.txt and output.txt files in /src represent running "python inputPreparation.py 26 1000" and "python hclvs.py".
- The responses to the written component are in the file "PA3.pdf".